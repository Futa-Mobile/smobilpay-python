import logging
import os

from flask import Flask, jsonify, request
from dotenv import load_dotenv

from models.account_model import AccountModel
from models.ping_model import PingModel
from models.payment_status_model import PaymentStatusModel
from services.account_service import AccountService
from services.ping_service import PingService
from services.transaction_service import TransactionService
from services.cashin_service import CashinService
from services.payment_status_service import PaymentStatusService
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
payment_status_service = PaymentStatusService()

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

@app.route('/api/verifytx', methods=['GET'])
def verify_transaction_status():
    """
    Check the current status of a transaction using PTN (Payment Transaction Number) or TRID (Transaction Reference ID).
    
    Query Parameters:
    - ptn: Payment Transaction Number (optional if trid is provided)
    - trid: Transaction Reference ID (optional if ptn is provided)
    
    Returns:
    - JSON response with transaction status details
    """
    try:
        # Get query parameters
        ptn = request.args.get('ptn')
        trid = request.args.get('trid')
        
        # Validate that at least one parameter is provided
        if not ptn and not trid:
            return jsonify({
                "status": "error",
                "message": "Either 'ptn' (Payment Transaction Number) or 'trid' (Transaction Reference ID) must be provided"
            }), 400
        
        logging.info(f"Verifying transaction status - PTN: {ptn}, TRID: {trid}")
        
        # Call the payment status service
        result = payment_status_service.fetch_payment_status(ptn=ptn, trid=trid)
        
        # Check if the result is a list of PaymentStatusModel objects (success case)
        if isinstance(result, list) and all(isinstance(item, PaymentStatusModel) for item in result):
            # Convert PaymentStatusModel objects to dictionaries for JSON serialization
            status_data = []
            for status in result:
                try:
                    status_dict = {
                        "ptn": status.ptn,
                        "serviceid": status.serviceid,
                        "merchant": status.merchant,
                        "timestamp": status.timestamp.isoformat() if status.timestamp and hasattr(status.timestamp, 'isoformat') else str(status.timestamp) if status.timestamp else None,
                        "receiptNumber": status.receiptNumber,
                        "veriCode": status.veriCode,
                        "clearingDate": status.clearingDate.isoformat() if status.clearingDate and hasattr(status.clearingDate, 'isoformat') else str(status.clearingDate) if status.clearingDate else None,
                        "trid": status.trid,
                        "priceLocalCur": status.priceLocalCur,
                        "priceSystemCur": status.priceSystemCur,
                        "localCur": status.localCur,
                        "systemCur": status.systemCur,
                        "pin": status.pin,
                        "status": status.status,
                        "payItemId": status.payItemId,
                        "payItemDescr": status.payItemDescr,
                        "errorCode": status.errorCode,
                        "tag": status.tag
                    }
                    status_data.append(status_dict)
                except Exception as e:
                    logging.error(f"Error serializing transaction status: {str(e)}")
                    # Continue with other transactions if one fails
                    continue
            
            if status_data:
                logging.info(f"Successfully retrieved transaction status for {len(status_data)} transaction(s)")
                return jsonify({
                    "status": "success",
                    "message": "Transaction status retrieved successfully",
                    "data": status_data
                }), 200
            else:
                logging.error("No valid transaction data could be serialized")
                return jsonify({
                    "status": "error",
                    "message": "Failed to process transaction data"
                }), 500
        
        # Handle error cases where the service returns an error message
        elif isinstance(result, str):
            logging.error(f"Service returned error: {result}")
            return jsonify({
                "status": "error",
                "message": result
            }), 500
        
        # Handle unexpected result types
        else:
            logging.error(f"Unexpected result type from service: {type(result)}")
            return jsonify({
                "status": "error",
                "message": "Unexpected response format from service"
            }), 500
            
    except Exception as e:
        logging.error(f"Unexpected error in verify_transaction_status: {str(e)}")
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred while verifying transaction status"
        }), 500

@app.errorhandler(500)
def internal_server_error(e):
     logging.error(f"An internal error occurred: {e}")
     return jsonify({"status": "error", "message": "An internal server error occurred."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
