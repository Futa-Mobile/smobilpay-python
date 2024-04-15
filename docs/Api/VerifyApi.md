# Verify Apis

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_payment_history**](VerifyApi.md#historystdget) | **GET** /historystd | Retrieve list of historic payment collection.
[**fetch_payment_status**](VerifyApi.md#verifytxget) | **GET** /verifytx | Get the current payment collection status

# **fetch_payment_history**
> def fetch_payment_history(self, timestamp_from = None, timestamp_to = None) -> List[PaymentHistoryModel]:

Retrieve a list of historic payment collection.

This endpoint allows the search for historic payment collection records by time
that was provided during a payment collection.
Both parameters have to be provided!

### Example
```python
import datetime
from services.payment_history_service import PaymentHistoryService

def main():
    # Initialize the PaymentHistory service with API credentials
    payment_history_service = PaymentHistoryService(public_token="your_public_token", secret_key="your_secret_key")

    # Define the date range
    timestamp_from = datetime.datetime(2023, 1, 1)
    timestamp_to = datetime.datetime(2023, 4, 1)

    # Fetch payment history within the specified date range
    history = payment_history_service.fetch_payment_history(timestamp_from, timestamp_to)

    if isinstance(history, list):
        print("Payment History:")
        for record in history:
            print(f"Transaction Number: {record.ptn}, Merchant: {record.merchant}, Amount: {record.priceLocalCur} {record.localCur}")
    else:
        print("Error:", history)  # Print the error message

if __name__ == "__main__":
    main()

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp_from** | **\DateTime**| Start date of transactions in result set (ISO 8601) | [optional]
 **timestamp_to** | **\DateTime**| End date of transactions in result set (ISO 8601) | [optional]

### Return type

[**List[PaymentHistoryModel]**](../Model/PaymentStatus.md)

### Authorization

No authorization required for this endpoint. Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`


All headers necessary for the API call are automatically managed by the SDK.

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **fetch_payment_status**
> def fetch_payment_status(self, ptn = None, trid = None) -> [PaymentStatusModel]:

Get the current payment collection status

Call this endpoint to retrieve the current payment status by either transaction number (PTN)
or the custom transaction reference (TRID) that was provided during a payment collection.
At least one of these parameters has to be provided!

### Example
```python
from services.payment_status_service import PaymentStatusService

def main():
    # Initialize the PaymentStatus service with API credentials
    payment_status_service = PaymentStatusService(public_token="your_public_token", secret_key="your_secret_key")

    # Define PTN or TRID
    ptn = "1234567890"
    trid = None  # Assuming no TRID is available

    # Fetch payment status using PTN or TRID
    payment_status = payment_status_service.fetch_payment_status(ptn=ptn, trid=trid)

    if isinstance(payment_status, PaymentStatusModel):
        print("Payment Status Details:")
        print(f"PTN: {payment_status.ptn}")
        print(f"Merchant: {payment_status.merchant}")
        print(f"Amount: {payment_status.priceLocalCur} {payment_status.localCur}")
        print(f"Status: {payment_status.status}")
        print(f"Timestamp: {payment_status.timestamp}")
        print(f"Clearing Date: {payment_status.clearingDate}")
    else:
        print("Error:", payment_status)  # Print the error message

if __name__ == "__main__":
    main()

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ptn** | **string**| Unique payment collection transaction number | [optional]
 **trid** | **string**| custom external transaction reference provided during payment collection | [optional]

### Return type

[**[PaymentStatusModel]**](../Model/PaymentStatus.md)

### Authorization

No authorization required for this endpoint. Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`


All headers necessary for the API call are automatically managed by the SDK.

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

