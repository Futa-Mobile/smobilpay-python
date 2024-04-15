# AccountService

All URIs are relative to `/v2`.

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_account_info**](HealthcheckApi.md#pingget) | **GET** /ping | Check on the availability of the api

## `fetch_account_info`
> from services.account_service import AccountService

Retrieve account information and remaining account balance

This endpoint returns the user’s account information – most notably the current balance of the user. Calling this service before and after each collection in order to retrieve the current limits and/or balance is highly discouraged. The recommended approach is as follows: 1. Only a successful payment collection transaction will affect the account balance. The corresponding endpoint will also return the current account balance after the collection in its result payload. 2. For unsuccessful payment transactions, the account balance will not be affected. The error message returns a verbose message as to why the transaction failed. There is no need to recheck the account after each error.

### Example Usage
```python
from services.account_service import AccountService

def main():
    # Initialize the Account service
    account_service = AccountService()
    account = account_service.fetch_account_info()
    print(account)

if __name__ == "__main__":
    main()
```

### Parameters

Name | Type        | Description | Notes
------------- |-------------|-------------| -------------
 **public_token** | **?string** | api key     | [default to defined .env]
 **secret_key** | **?string** | api secret  | [default to defined .env]

### Return type

Returns an instance of [**AccountModel**](../Model/Account.md)

### Authorization

No authorization required for this endpoint. Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`


All headers necessary for the API call are automatically managed by the SDK.


[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

