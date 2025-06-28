import requests
from typing import List
from models.cashin_model import CashinModel
from s3_api_auth import S3ApiAuth
from configuration import Configuration  # Import the configuration class
import logging
import os

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CashinService:
    CHANNEL_PAYITEMID_MAP = {
        "ORANGE": os.environ.get("SMOBILE_PAY_CASH_IN_ORANGE_MONEY_PAY_ID"),
        "MTN": os.environ.get("SMOBILE_PAY_CASH_IN_MTN_MOMO_PAY_ID")
    }

    def __init__(self, public_token=None, secret_key=None):
        self.config = Configuration()  # Create a configuration instance
        self.public_token = public_token if public_token else self.config.get_api_key()
        self.secret_key = secret_key if secret_key else self.config.get_api_secret()
        self.api_version = self.config.api_version
        self.base_url = f"{self.config.get_api_url()}/cashin"
        self.api_auth = S3ApiAuth(self.base_url, self.public_token, self.secret_key)

    def fetch_cashins(self, service_id: int = None):
        params = {'serviceid': service_id} if service_id is not None else {}
        headers = {
            'Authorization': self.api_auth.create_authorization_header('GET', params),
            'x-api-version': self.api_version
        }
        logging.info(f"Payload to sign: {params}")
        logging.info(f"Generated signature: {headers['Authorization']}")
        logging.info(f"Headers: {headers}")
        return self._make_request(params, headers)

    def _send_request(self, url, payload, method='POST'):
        # Set the api_url on the auth object to the correct endpoint
        self.api_auth.api_url = url
        headers = {
            'Authorization': self.api_auth.create_authorization_header(method, payload),
            'x-api-version': self.api_version,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        logging.info(f"Payload to sign: {payload}")
        logging.info(f"Generated signature: {headers['Authorization']}")
        logging.info(f"Headers: {headers}")
        try:
            if method == 'POST':
                response = requests.post(url, data=payload, headers=headers)
            else:
                response = requests.get(url, headers=headers, params=payload)
            logging.info(f"{method} response: status={response.status_code}, body={response.text}")
            if response.status_code in (200, 201):
                return {"success": True, "data": response.json()}
            else:
                return {"success": False, "error": response.text, "status_code": response.status_code}
        except requests.RequestException as e:
            logging.error(f"Network error occurred during {method}: {str(e)}")
            return {"success": False, "error": f"Network error occurred: {str(e)}"}

    def process_cashin(self, cashin_data: dict) -> dict:
        """
        Process a cashin request using SmobilPay's two-step process.
        Args:
            cashin_data (dict): The cashin data from the request
        Returns:
            dict: Response containing the cashin status and details
        """
        required_fields = [
            'channel', 'amount', 'serviceNumber', 'customerPhonenumber', 'customerEmailaddress', 'trid'
        ]
        missing = [f for f in required_fields if f not in cashin_data]
        if missing:
            return {"status": "error", "message": f"Missing required fields: {', '.join(missing)}"}
        channel = cashin_data['channel']
        payItemId = self.CHANNEL_PAYITEMID_MAP.get(channel)
        if not payItemId:
            return {"status": "error", "message": f"Invalid or unsupported channel: {channel}"}
        try:
            # Step 1: Request a quote (POST, x-www-form-urlencoded)
            quote_payload = {
                'payItemId': payItemId,
                'amount': cashin_data['amount']
            }
            quote_url = f"{self.config.get_api_url()}/quotestd"
            quote_result = self._send_request(quote_url, quote_payload, method='POST')
            if not quote_result["success"]:
                return {"status": "error", "message": "Quote request failed", "details": quote_result.get("error")}
            quote_json = quote_result["data"]
            quote_id = quote_json.get('quoteId')
            if not quote_id:
                return {"status": "error", "message": "No quoteId returned from quote step", "details": quote_json}

            # Step 2: Confirm the order (POST, x-www-form-urlencoded)
            collect_payload = {
                'quoteId': quote_id,
                'serviceNumber': cashin_data['serviceNumber'],
                'customerPhonenumber': cashin_data['customerPhonenumber'],
                'customerEmailaddress': cashin_data['customerEmailaddress'],
                'trid': cashin_data['trid']
            }
            collect_url = f"{self.config.get_api_url()}/collectstd"
            collect_result = self._send_request(collect_url, collect_payload, method='POST')
            if not collect_result["success"]:
                return {"status": "error", "message": "Collect request failed", "details": collect_result.get("error")}
            return {
                "status": "success",
                "message": "Cashin processed successfully",
                "result": collect_result["data"]
            }
        except Exception as e:
            logging.error(f"Error processing cashin: {str(e)}")
            return {"status": "error", "message": f"Failed to process cashin: {str(e)}"}

    def _make_request(self, params, headers):
        try:
            response = requests.get(self.base_url, headers=headers, params=params)
            if response.status_code == 200:
                cashins_data = response.json()
                return [CashinModel(**cashin) for cashin in cashins_data]
            elif response.status_code == 401:
                logging.error("Request could not be authenticated: %s", response.text)
                return "Request could not be authenticated."
            else:
                logging.error("An error occurred with status code: %s and payload %s", response.status_code, response.content)
                return "An error occurred."
        except requests.RequestException as e:
            logging.error("Network error occurred: %s", str(e))
            return f"Network error occurred: {str(e)}"
