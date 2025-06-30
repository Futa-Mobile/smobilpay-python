#!/usr/bin/env python3
"""
Example script demonstrating how to use the SmobilPay verifytx endpoint
to check transaction status using the PaymentStatusService directly.

This example shows how to:
1. Initialize the PaymentStatusService
2. Verify transactions using PTN (Payment Transaction Number)
3. Verify transactions using TRID (Transaction Reference ID)
4. Handle different response scenarios
5. Process the transaction status data

Usage:
    python examples/verify_transaction_example.py
"""

import sys
import os
import logging
from datetime import datetime

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.payment_status_service import PaymentStatusService
from models.payment_status_model import PaymentStatusModel

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def display_transaction_status(transaction: PaymentStatusModel):
    """
    Display transaction status information in a formatted way.
    
    Args:
        transaction (PaymentStatusModel): The transaction status model
    """
    print("=" * 60)
    print("📋 TRANSACTION STATUS DETAILS")
    print("=" * 60)
    print(f"🔢 PTN (Payment Transaction Number): {transaction.ptn}")
    print(f"🏢 Merchant: {transaction.merchant}")
    print(f"🆔 Service ID: {transaction.serviceid}")
    print(f"📅 Timestamp: {transaction.timestamp}")
    print(f"🧾 Receipt Number: {transaction.receiptNumber}")
    print(f"🔐 Verification Code: {transaction.veriCode}")
    print(f"💰 Amount (Local): {transaction.priceLocalCur} {transaction.localCur}")
    print(f"💵 Amount (System): {transaction.priceSystemCur} {transaction.systemCur}")
    print(f"📊 Status: {transaction.status}")
    print(f"🏷️  TRID: {transaction.trid}")
    print(f"📌 PIN: {transaction.pin}")
    print(f"🆔 Payment Item ID: {transaction.payItemId}")
    print(f"📝 Payment Description: {transaction.payItemDescr}")
    print(f"❌ Error Code: {transaction.errorCode}")
    print(f"🏷️  Tag: {transaction.tag}")
    
    if transaction.clearingDate:
        print(f"📅 Clearing Date: {transaction.clearingDate}")
    
    # Display status-specific information
    print("\n" + "=" * 60)
    print("📊 STATUS ANALYSIS")
    print("=" * 60)
    
    if transaction.status == "SUCCESS":
        print("✅ Transaction completed successfully!")
        print("💡 The payment has been processed and confirmed.")
    elif transaction.status == "PENDING":
        print("⏳ Transaction is pending processing...")
        print("💡 The payment is being processed. Check again later.")
    elif transaction.status == "FAILED":
        print("❌ Transaction failed!")
        print("💡 The payment could not be processed. Check error details.")
    elif transaction.status == "CANCELLED":
        print("🚫 Transaction was cancelled!")
        print("💡 The payment was cancelled by the user or system.")
    elif transaction.status == "EXPIRED":
        print("⏰ Transaction expired!")
        print("💡 The payment session has expired. A new transaction is needed.")
    elif transaction.status == "REFUNDED":
        print("↩️  Transaction was refunded!")
        print("💡 The payment has been refunded to the customer.")
    else:
        print(f"❓ Unknown status: {transaction.status}")
        print("💡 Contact support for more information.")
    
    print("=" * 60)

def verify_transaction_with_ptn():
    """
    Example: Verify transaction using PTN (Payment Transaction Number).
    """
    logger.info("🔍 Verifying transaction with PTN")
    
    try:
        # Initialize the PaymentStatusService
        payment_status_service = PaymentStatusService()
        
        # Example PTN - replace with actual PTN for testing
        ptn = "1234567890"
        
        logger.info(f"Checking transaction status for PTN: {ptn}")
        
        # Call the service to get transaction status
        result = payment_status_service.fetch_payment_status(ptn=ptn)
        
        # Check if the result is a list of PaymentStatusModel objects
        if isinstance(result, list) and all(isinstance(item, PaymentStatusModel) for item in result):
            logger.info(f"✅ Successfully retrieved {len(result)} transaction(s)")
            
            for i, transaction in enumerate(result):
                print(f"\n📋 Transaction {i + 1}:")
                display_transaction_status(transaction)
                
        else:
            logger.error(f"❌ Failed to retrieve transaction status: {result}")
            print(f"Error: {result}")
            
    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")
        print(f"Unexpected error: {str(e)}")

def verify_transaction_with_trid():
    """
    Example: Verify transaction using TRID (Transaction Reference ID).
    """
    logger.info("🔍 Verifying transaction with TRID")
    
    try:
        # Initialize the PaymentStatusService
        payment_status_service = PaymentStatusService()
        
        # Example TRID - replace with actual TRID for testing
        trid = "eabd12-7494984-494044-d0"
        
        logger.info(f"Checking transaction status for TRID: {trid}")
        
        # Call the service to get transaction status
        result = payment_status_service.fetch_payment_status(trid=trid)
        
        # Check if the result is a list of PaymentStatusModel objects
        if isinstance(result, list) and all(isinstance(item, PaymentStatusModel) for item in result):
            logger.info(f"✅ Successfully retrieved {len(result)} transaction(s)")
            
            for i, transaction in enumerate(result):
                print(f"\n📋 Transaction {i + 1}:")
                display_transaction_status(transaction)
                
        else:
            logger.error(f"❌ Failed to retrieve transaction status: {result}")
            print(f"Error: {result}")
            
    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")
        print(f"Unexpected error: {str(e)}")

def verify_transaction_with_both():
    """
    Example: Verify transaction using both PTN and TRID.
    """
    logger.info("🔍 Verifying transaction with both PTN and TRID")
    
    try:
        # Initialize the PaymentStatusService
        payment_status_service = PaymentStatusService()
        
        # Example values - replace with actual values for testing
        ptn = "1234567890"
        trid = "eabd12-7494984-494044-d0"
        
        logger.info(f"Checking transaction status for PTN: {ptn}, TRID: {trid}")
        
        # Call the service to get transaction status
        result = payment_status_service.fetch_payment_status(ptn=ptn, trid=trid)
        
        # Check if the result is a list of PaymentStatusModel objects
        if isinstance(result, list) and all(isinstance(item, PaymentStatusModel) for item in result):
            logger.info(f"✅ Successfully retrieved {len(result)} transaction(s)")
            
            for i, transaction in enumerate(result):
                print(f"\n📋 Transaction {i + 1}:")
                display_transaction_status(transaction)
                
        else:
            logger.error(f"❌ Failed to retrieve transaction status: {result}")
            print(f"Error: {result}")
            
    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")
        print(f"Unexpected error: {str(e)}")

def test_error_handling():
    """
    Example: Test error handling with missing parameters.
    """
    logger.info("🔍 Testing error handling with missing parameters")
    
    try:
        # Initialize the PaymentStatusService
        payment_status_service = PaymentStatusService()
        
        logger.info("Attempting to verify transaction without providing PTN or TRID")
        
        # Call the service without any parameters (should fail)
        result = payment_status_service.fetch_payment_status()
        
        # This should return an error message
        logger.info(f"Expected error message: {result}")
        print(f"Error handling test result: {result}")
        
    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")
        print(f"Unexpected error: {str(e)}")

def main():
    """
    Main function to run all examples.
    """
    print("🚀 SmobilPay Transaction Verification Examples")
    print("=" * 60)
    print("This example demonstrates how to use the PaymentStatusService")
    print("to verify transaction status using PTN or TRID.")
    print("=" * 60)
    
    # Example 1: Verify with PTN
    print("\n📋 Example 1: Verify transaction with PTN")
    print("-" * 40)
    verify_transaction_with_ptn()
    
    # Example 2: Verify with TRID
    print("\n📋 Example 2: Verify transaction with TRID")
    print("-" * 40)
    verify_transaction_with_trid()
    
    # Example 3: Verify with both parameters
    print("\n📋 Example 3: Verify transaction with both PTN and TRID")
    print("-" * 40)
    verify_transaction_with_both()
    
    # Example 4: Test error handling
    print("\n📋 Example 4: Test error handling")
    print("-" * 40)
    test_error_handling()
    
    print("\n" + "=" * 60)
    print("✅ All examples completed!")
    print("\n💡 Tips:")
    print("   - Replace the example PTN and TRID values with real transaction IDs")
    print("   - Check the logs for detailed information about API calls")
    print("   - Handle different status values appropriately in your application")
    print("   - Always validate the response before processing transaction data")

if __name__ == "__main__":
    main() 