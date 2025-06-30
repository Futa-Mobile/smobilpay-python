import requests
from models.payment_status_model import PaymentStatusModel
from s3_api_auth import S3ApiAuth
from configuration import Configuration  # Import the configuration class
import logging
from datetime import datetime

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PaymentStatusService:
    def __init__(self, public_token=None, secret_key=None):
        self.config = Configuration()  # Create a configuration instance
        self.public_token = public_token if public_token else self.config.get_api_key()
        self.secret_key = secret_key if secret_key else self.config.get_api_secret()
        self.api_version = self.config.api_version
        self.base_url = f"{self.config.get_api_url()}/verifytx"
        self.api_auth = S3ApiAuth(self.base_url, self.public_token, self.secret_key)

    def fetch_payment_status(self, ptn=None, trid=None):
        if not ptn and not trid:
            logging.error("PTN or TRID must be provided.")
            return "PTN or TRID must be provided."
        
        params = {}
        if ptn:
            params['ptn'] = ptn
        if trid:
            params['trid'] = trid

        headers = {
            'Authorization': self.api_auth.create_authorization_header('GET', params),
            'x-api-version': self.api_version
        }

        return self._make_request(params, headers)

    def _parse_datetime(self, date_string):
        """
        Parse datetime string to datetime object.
        
        Args:
            date_string: String representation of datetime
            
        Returns:
            datetime object or None if parsing fails
        """
        if not date_string:
            return None
            
        try:
            # Try parsing ISO format first
            return datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        except ValueError:
            try:
                # Try parsing common datetime formats
                for fmt in ['%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d']:
                    try:
                        return datetime.strptime(date_string, fmt)
                    except ValueError:
                        continue
                return None
            except Exception:
                return None

    def _make_request(self, params, headers):
        try:
            response = requests.get(self.base_url, headers=headers, params=params)
            if response.status_code == 200:
                try:
                    payment_status_data = response.json()
                    payment_status_models = []
                    
                    for status in payment_status_data:
                        try:
                            # Parse datetime fields
                            if 'timestamp' in status and status['timestamp']:
                                status['timestamp'] = self._parse_datetime(status['timestamp'])
                            
                            if 'clearingDate' in status and status['clearingDate']:
                                status['clearingDate'] = self._parse_datetime(status['clearingDate'])
                            
                            # Create the model
                            payment_status_model = PaymentStatusModel(**status)
                            payment_status_models.append(payment_status_model)
                            
                        except Exception as e:
                            logging.error(f"Error creating PaymentStatusModel: {str(e)}")
                            logging.error(f"Status data: {status}")
                            # Return the raw data if model creation fails
                            return f"Data parsing error for transaction: {str(e)}"
                    
                    return payment_status_models
                    
                except Exception as e:
                    logging.error(f"Error parsing response JSON: {str(e)}")
                    return f"Data parsing error: {str(e)}"
            elif response.status_code == 401:
                logging.error(f"Authentication failed: {response.text}")
                return "Request could not be authenticated."
            else:
                logging.error(f"Unexpected status {response.status_code}: {response.text}")
                return f"An unexpected error occurred with status code: {response.status_code}"
        except requests.RequestException as e:
            logging.error(f"Network error occurred: {str(e)}")
            return f"Network error occurred: {str(e)}"
