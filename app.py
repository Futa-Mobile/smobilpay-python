import logging
import os

from flask import Flask, jsonify, request
from dotenv import load_dotenv

from models.account_model import AccountModel
from models.ping_model import PingModel
from services.account_service import AccountService
from services.ping_service import PingService
from services.transaction_service import TransactionService
from services.cashin_service import CashinService
# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize services
ping_service = PingService()
account_service = AccountService()
transaction_service = TransactionService()
cashin_service = CashinService()

# Routes
@app.route('/api/ping', methods=['GET'])
def ping():
     """
     Check the availability of the Smobilpay API.
     """
     logging.info("Received request on /api/ping")
     response = ping_service.ping()

     if isinstance(response, PingModel):
         logging.info(f"Ping successful: {response}")
         return jsonify({
             "status": "success",
             "time": response.time,
             "version": response.version,
             "nonce": response.nonce,
             "key": response.key
         }), 200
     else:
         logging.error(f"Ping failed: {response}")
         return jsonify({"status": "error", "message": "Ping to Smobilpay API failed"}), 500

@app.route('/api/account', methods=['GET'])
def get_account_info():
     """
     Retrieve account information from the Smobilpay API.
     """
     logging.info("Received request on /api/account")
     account_info = account_service.fetch_account_info()

     if isinstance(account_info, AccountModel):
         logging.info(f"Account information fetched: {account_info}")
         return jsonify({
             "status": "success",
             "balance": account_info.balance,
             "currency": account_info.currency
         }), 200
     else:
         logging.error(f"Failed to fetch account information: {account_info}")
         return jsonify({"status": "error", "message": "Failed to fetch account information"}), 500

@app.route('/api/cashin', methods=['POST'])
def create_cashin():
    """
    Create and process a new cashin request.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "Invalid request format"}), 400
        result = cashin_service.process_cashin(data)
        if result['status'] == 'success':
            return jsonify(result), 201
        else:
            return jsonify(result), 400
    except Exception as e:
        logging.error(f"Error processing cashin request: {str(e)}")
        return jsonify({"status": "error", "message": "An error occurred while processing the cashin"}), 500

@app.errorhandler(500)
def internal_server_error(e):
     logging.error(f"An internal error occurred: {e}")
     return jsonify({"status": "error", "message": "An internal server error occurred."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
