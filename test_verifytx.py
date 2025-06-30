#!/usr/bin/env python3
"""
Test script for the SmobilPay /verifytx endpoint implementation.

This script demonstrates how to use the transaction verification endpoint
to check the status of transactions using either PTN (Payment Transaction Number)
or TRID (Transaction Reference ID).

Usage:
    python test_verifytx.py
"""

import requests
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration
BASE_URL = "http://localhost:5001"
VERIFYTX_ENDPOINT = f"{BASE_URL}/api/verifytx"

def test_verifytx_with_ptn():
    """
    Test the verifytx endpoint using a PTN (Payment Transaction Number).
    """
    logger.info("Testing verifytx endpoint with PTN parameter")
    
    # Example PTN - replace with actual PTN for testing
    ptn = "1234567890"
    
    try:
        response = requests.get(VERIFYTX_ENDPOINT, params={'ptn': ptn})
        
        logger.info(f"Response Status Code: {response.status_code}")
        logger.info(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            logger.info("✅ Success! Transaction status retrieved:")
            logger.info(json.dumps(data, indent=2))
            
            # Extract and display key information
            if 'data' in data and data['data']:
                transaction = data['data'][0]  # Assuming single transaction
                logger.info(f"Transaction Details:")
                logger.info(f"  PTN: {transaction.get('ptn')}")
                logger.info(f"  Status: {transaction.get('status')}")
                logger.info(f"  Merchant: {transaction.get('merchant')}")
                logger.info(f"  Amount: {transaction.get('priceLocalCur')} {transaction.get('localCur')}")
                logger.info(f"  Receipt Number: {transaction.get('receiptNumber')}")
                logger.info(f"  Verification Code: {transaction.get('veriCode')}")
        else:
            logger.error(f"❌ Error: {response.status_code}")
            logger.error(f"Response: {response.text}")
            
    except requests.RequestException as e:
        logger.error(f"❌ Network error: {str(e)}")
    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")

def test_verifytx_with_trid():
    """
    Test the verifytx endpoint using a TRID (Transaction Reference ID).
    """
    logger.info("Testing verifytx endpoint with TRID parameter")
    
    # Example TRID - replace with actual TRID for testing
    trid = "eabd12-7494984-494044-d0"
    
    try:
        response = requests.get(VERIFYTX_ENDPOINT, params={'trid': trid})
        
        logger.info(f"Response Status Code: {response.status_code}")
        logger.info(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            logger.info("✅ Success! Transaction status retrieved:")
            logger.info(json.dumps(data, indent=2))
            
            # Extract and display key information
            if 'data' in data and data['data']:
                transaction = data['data'][0]  # Assuming single transaction
                logger.info(f"Transaction Details:")
                logger.info(f"  TRID: {transaction.get('trid')}")
                logger.info(f"  PTN: {transaction.get('ptn')}")
                logger.info(f"  Status: {transaction.get('status')}")
                logger.info(f"  Merchant: {transaction.get('merchant')}")
                logger.info(f"  Amount: {transaction.get('priceLocalCur')} {transaction.get('localCur')}")
        else:
            logger.error(f"❌ Error: {response.status_code}")
            logger.error(f"Response: {response.text}")
            
    except requests.RequestException as e:
        logger.error(f"❌ Network error: {str(e)}")
    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")

def test_verifytx_missing_parameters():
    """
    Test the verifytx endpoint without providing any parameters (should return 400).
    """
    logger.info("Testing verifytx endpoint without parameters (should fail)")
    
    try:
        response = requests.get(VERIFYTX_ENDPOINT)
        
        logger.info(f"Response Status Code: {response.status_code}")
        
        if response.status_code == 400:
            data = response.json()
            logger.info("✅ Correctly handled missing parameters:")
            logger.info(json.dumps(data, indent=2))
        else:
            logger.error(f"❌ Expected 400 status code, got {response.status_code}")
            logger.error(f"Response: {response.text}")
            
    except requests.RequestException as e:
        logger.error(f"❌ Network error: {str(e)}")
    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")

def test_verifytx_with_both_parameters():
    """
    Test the verifytx endpoint with both PTN and TRID parameters.
    """
    logger.info("Testing verifytx endpoint with both PTN and TRID parameters")
    
    # Example values - replace with actual values for testing
    ptn = "1234567890"
    trid = "eabd12-7494984-494044-d0"
    
    try:
        response = requests.get(VERIFYTX_ENDPOINT, params={'ptn': ptn, 'trid': trid})
        
        logger.info(f"Response Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            logger.info("✅ Success! Transaction status retrieved with both parameters:")
            logger.info(json.dumps(data, indent=2))
        else:
            logger.error(f"❌ Error: {response.status_code}")
            logger.error(f"Response: {response.text}")
            
    except requests.RequestException as e:
        logger.error(f"❌ Network error: {str(e)}")
    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")

def main():
    """
    Main function to run all tests.
    """
    logger.info("🚀 Starting SmobilPay verifytx endpoint tests")
    logger.info("=" * 60)
    
    # Test 1: Verify with PTN
    logger.info("\n📋 Test 1: Verify transaction with PTN")
    test_verifytx_with_ptn()
    
    # Test 2: Verify with TRID
    logger.info("\n📋 Test 2: Verify transaction with TRID")
    test_verifytx_with_trid()
    
    # Test 3: Verify with both parameters
    logger.info("\n📋 Test 3: Verify transaction with both PTN and TRID")
    test_verifytx_with_both_parameters()
    
    # Test 4: Test missing parameters
    logger.info("\n📋 Test 4: Test missing parameters (error handling)")
    test_verifytx_missing_parameters()
    
    logger.info("\n" + "=" * 60)
    logger.info("✅ All tests completed!")

if __name__ == "__main__":
    main() 