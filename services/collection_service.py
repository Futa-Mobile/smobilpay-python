import requests
import json
from models.collection_model import CollectionModel
from s3_api_auth import S3ApiAuth
from configuration import Configuration
import logging

class CollectionService:
    def __init__(self, public_token=None, secret_key=None):
        self.config = Configuration()  # Create a configuration instance
        self.public_token = public_token if public_token else self.config.get_api_key()
        self.secret_key = secret_key if secret_key else self.config.get_api_secret()
        self.api_version = self.config.api_version
        self.base_url = f"{self.config.get_api_url()}/collectstd"
        self.api_auth = S3ApiAuth(self.base_url, self.public_token, self.secret_key)

        # Configure logging based on the debug setting from Configuration
        logging_level = logging.DEBUG if self.config.debug_enabled else logging.INFO
        logging.basicConfig(level=logging_level, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.debug(f"Initialized CollectionService with URL: {self.base_url}")

    def execute_collection(self, data):
        headers = self.api_auth.create_authorization_header('POST')
        headers.update({
            'x-api-version': self.api_version,
            'Content-Type': 'application/json'
        })
        payload = json.dumps(data)
        logging.debug(f"Sending collection request with payload: {data}")
        return self._make_request(payload, headers)

    def _make_request(self, payload, headers):
        try:
            response = requests.post(self.base_url, headers=headers, data=payload)
            logging.debug(f"Received HTTP status: {response.status_code} for collection request")
            if response.status_code == 200:
                collection_data = response.json()
                return CollectionModel(**collection_data)
            elif response.status_code == 401:
                logging.error("Request could not be authenticated: %s", response.text)
                return "Request could not be authenticated."
            elif response.status_code == 498:
                logging.error("Quote has expired: %s", response.text)
                return "Quote has expired."
            else:
                logging.error("An unexpected error occurred with status code: %s", response.status_code)
                return "An unexpected error occurred."
        except requests.RequestException as e:
            logging.error("Network error occurred: %s", str(e))
            return f"Network error occurred: {str(e)}"
