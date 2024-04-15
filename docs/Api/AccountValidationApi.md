# ServiceNumberVerificationApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_service_number**](AccountValidationApi.md#verifyget) | **GET** /verify | Verify service number

# **verify_service_number**
> from services.service_number_verification_api import ServiceNumberVerificationApi

Verify service number

For services that support verification (indicated by the \"is_valid\" flag),
the service number can be provided to this endpoint.
The system will verify whether the service number is valid with the selected service.

### Example
```python
from services.service_number_verification_api import ServiceNumberVerificationApi

def main():
    # Initialize the Account service
    account_validation = ServiceNumberVerificationApi()
    merchant = "merchant_example"
    serviceId = 56
    serviceNumber = "serviceNumber_example"
    result = account_service.verify_service_number(merchant, serviceid, serviceNumber)
    print(result)

if __name__ == "__main__":
    main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant** | **string**| Unique  merchant code |
 **serviceid** | **int**| Unique  service Identifier |
 **serviceNumber** | **string**| Service number with merchant (e.g. meter number in bills from a utility provider) for which to perform the bill payment |


### Return type

Returns an instance of [**VerificationResult**](../Model/VerificationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

