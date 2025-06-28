import logging
from models.transaction_model import Transaction, Amount, TransactionMetadata, TransactionType

class TransactionService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def process_transaction(self, transaction_data: dict) -> dict:
        """
        Process a transaction request.
        
        Args:
            transaction_data (dict): The transaction data from the request
            
        Returns:
            dict: Response containing the transaction status and details
        """
        try:
            # Validate transaction type
            if 'transaction_type' not in transaction_data:
                return {
                    "status": "error",
                    "message": "Transaction type is required"
                }
                
            try:
                transaction_type = TransactionType(transaction_data['transaction_type'].lower())
            except ValueError:
                return {
                    "status": "error",
                    "message": "Invalid transaction type. Must be either 'credit' or 'debit'"
                }

            # Create transaction model from request data
            transaction = Transaction(
                reference=transaction_data['reference'],
                amount=Amount(
                    value=transaction_data['amount']['value'],
                    currency=transaction_data['amount']['currency']
                ),
                description=transaction_data['description'],
                metadata=TransactionMetadata(
                    order_id=transaction_data['metadata']['order_id'],
                    customer_reference=transaction_data['metadata']['customer_reference']
                ),
                transaction_type=transaction_type
            )

            # Log the transaction
            self.logger.info(f"Processing {transaction.transaction_type.value} transaction: {transaction.reference}")
            
            # TODO: Implement actual transaction processing logic here
            # This could include:
            # - Validating the transaction
            # - Processing payment
            # - Updating account balances based on transaction type
            # - Recording transaction history
            
            return {
                "status": "success",
                "message": "Transaction processed successfully",
                "transaction": {
                    "reference": transaction.reference,
                    "amount": {
                        "value": transaction.amount.value,
                        "currency": transaction.amount.currency
                    },
                    "description": transaction.description,
                    "transaction_type": transaction.transaction_type.value,
                    "metadata": {
                        "order_id": transaction.metadata.order_id,
                        "customer_reference": transaction.metadata.customer_reference
                    }
                }
            }
            
        except Exception as e:
            self.logger.error(f"Error processing transaction: {str(e)}")
            return {
                "status": "error",
                "message": f"Failed to process transaction: {str(e)}"
            } 