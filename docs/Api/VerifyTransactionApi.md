# Verify Transaction API

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_transaction_status**](VerifyTransactionApi.md#verifytxget) | **GET** /verifytx | Check the current status of a transaction using PTN or TRID

# **verify_transaction_status**
> def verify_transaction_status(self, ptn = None, trid = None) -> dict:

Check the current status of a transaction using PTN (Payment Transaction Number) or TRID (Transaction Reference ID).

This endpoint allows you to retrieve the current payment status by either:
- **PTN (Payment Transaction Number)**: Unique payment collection transaction number
- **TRID (Transaction Reference ID)**: Custom external transaction reference provided during payment collection

At least one of these parameters must be provided.

## Example Usage

### Using PTN (Payment Transaction Number)
```python
import requests

def verify_with_ptn():
    # Initialize the API endpoint
    url = "http://localhost:5001/api/verifytx"
    
    # Define the PTN
    ptn = "1234567890"
    
    # Make the request
    response = requests.get(url, params={'ptn': ptn})
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Transaction status retrieved successfully")
        print(f"Status: {data['data'][0]['status']}")
        print(f"Amount: {data['data'][0]['priceLocalCur']} {data['data'][0]['localCur']}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(f"Message: {response.json()['message']}")

if __name__ == "__main__":
    verify_with_ptn()
```

### Using TRID (Transaction Reference ID)
```python
import requests

def verify_with_trid():
    # Initialize the API endpoint
    url = "http://localhost:5001/api/verifytx"
    
    # Define the TRID
    trid = "eabd12-7494984-494044-d0"
    
    # Make the request
    response = requests.get(url, params={'trid': trid})
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Transaction status retrieved successfully")
        print(f"PTN: {data['data'][0]['ptn']}")
        print(f"Status: {data['data'][0]['status']}")
        print(f"Merchant: {data['data'][0]['merchant']}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(f"Message: {response.json()['message']}")

if __name__ == "__main__":
    verify_with_trid()
```

### Using Both Parameters
```python
import requests

def verify_with_both():
    # Initialize the API endpoint
    url = "http://localhost:5001/api/verifytx"
    
    # Define both parameters
    ptn = "1234567890"
    trid = "eabd12-7494984-494044-d0"
    
    # Make the request
    response = requests.get(url, params={'ptn': ptn, 'trid': trid})
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Transaction status retrieved successfully")
        print(json.dumps(data, indent=2))
    else:
        print(f"❌ Error: {response.status_code}")
        print(f"Message: {response.json()['message']}")

if __name__ == "__main__":
    verify_with_both()
```

## Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **ptn** | **string** | Payment Transaction Number - unique payment collection transaction number | [optional]
 **trid** | **string** | Transaction Reference ID - custom external transaction reference provided during payment collection | [optional]

**Note**: At least one of `ptn` or `trid` must be provided. If both are provided, the system will use both for verification.

## Response Format

### Success Response (200)
```json
{
  "status": "success",
  "message": "Transaction status retrieved successfully",
  "data": [
    {
      "ptn": "1234567890",
      "serviceid": "service_123",
      "merchant": "merchant_code",
      "timestamp": "2023-12-01T10:30:00Z",
      "receiptNumber": "REC123456",
      "veriCode": "VER789",
      "clearingDate": "2023-12-01T10:35:00Z",
      "trid": "eabd12-7494984-494044-d0",
      "priceLocalCur": 1000.00,
      "priceSystemCur": 1.50,
      "localCur": "XAF",
      "systemCur": "USD",
      "pin": "123456",
      "status": "SUCCESS",
      "payItemId": "item_123",
      "payItemDescr": "Payment for electricity bill",
      "errorCode": 0,
      "tag": "tag_value"
    }
  ]
}
```

### Error Response (400) - Missing Parameters
```json
{
  "status": "error",
  "message": "Either 'ptn' (Payment Transaction Number) or 'trid' (Transaction Reference ID) must be provided"
}
```

### Error Response (500) - Server Error
```json
{
  "status": "error",
  "message": "An unexpected error occurred while verifying transaction status"
}
```

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| **ptn** | string | Unique payment collection transaction number |
| **serviceid** | string | Unique service identifier |
| **merchant** | string | Merchant code |
| **timestamp** | datetime | Timestamp of processing in system (ISO 8601) |
| **receiptNumber** | string | Receipt number - alternative identifier of payment |
| **veriCode** | string | Verification code for receipt number |
| **clearingDate** | datetime | Date when payment information was sent to merchant (ISO 8601) |
| **trid** | string | Custom external transaction reference |
| **priceLocalCur** | float | Price paid in local currency |
| **priceSystemCur** | float | Price paid in system currency |
| **localCur** | string | Local currency of service (e.g., XAF) |
| **systemCur** | string | Currency of billing by system |
| **pin** | string | Digital code to display to customer (if supplied by service) |
| **status** | string | Payment processing status |
| **payItemId** | string | Unique payment item ID for payment item identification |
| **payItemDescr** | string | Description about payment details |
| **errorCode** | int | Error code (0 for success) |
| **tag** | string | Additional tag information |

## Status Values

The `status` field can contain various values indicating the transaction state:

- **SUCCESS**: Transaction completed successfully
- **PENDING**: Transaction is being processed
- **FAILED**: Transaction failed
- **CANCELLED**: Transaction was cancelled
- **EXPIRED**: Transaction expired
- **REFUNDED**: Transaction was refunded

## Error Codes

| Error Code | Description |
|------------|-------------|
| 0 | Success |
| 1001 | Invalid PTN format |
| 1002 | Invalid TRID format |
| 2001 | Transaction not found |
| 2002 | Transaction expired |
| 3001 | Authentication failed |
| 3002 | Authorization failed |
| 5001 | Internal server error |

## Authentication

This endpoint uses the same authentication mechanism as other SmobilPay API endpoints:

- **Authorization Header**: Contains the signed request signature
- **x-api-version**: API version header
- **Content-Type**: application/json

## Rate Limiting

The endpoint follows the same rate limiting policies as other SmobilPay API endpoints. Please refer to the main API documentation for specific limits.

## Testing

You can test this endpoint using the provided test script:

```bash
python test_verifytx.py
```

The test script includes examples for:
- Testing with PTN only
- Testing with TRID only
- Testing with both parameters
- Testing error handling (missing parameters)

## Integration Examples

### cURL Example
```bash
# Verify with PTN
curl -X GET "http://localhost:5001/api/verifytx?ptn=1234567890" \
  -H "Accept: application/json"

# Verify with TRID
curl -X GET "http://localhost:5001/api/verifytx?trid=eabd12-7494984-494044-d0" \
  -H "Accept: application/json"

# Verify with both parameters
curl -X GET "http://localhost:5001/api/verifytx?ptn=1234567890&trid=eabd12-7494984-494044-d0" \
  -H "Accept: application/json"
```

### JavaScript/Node.js Example
```javascript
const axios = require('axios');

async function verifyTransaction(ptn, trid) {
  try {
    const params = {};
    if (ptn) params.ptn = ptn;
    if (trid) params.trid = trid;
    
    const response = await axios.get('http://localhost:5001/api/verifytx', {
      params: params,
      headers: {
        'Accept': 'application/json'
      }
    });
    
    console.log('Transaction status:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error verifying transaction:', error.response?.data || error.message);
    throw error;
  }
}

// Usage
verifyTransaction('1234567890', null); // With PTN only
verifyTransaction(null, 'eabd12-7494984-494044-d0'); // With TRID only
verifyTransaction('1234567890', 'eabd12-7494984-494044-d0'); // With both
```

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md) 