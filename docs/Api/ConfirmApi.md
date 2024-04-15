# CollectionService

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_payment_collection**](ConfirmApi.md#collectstdpost) | **POST** /collectstd | Execute payment collection

# **execute_payment_collection**
> from services.collection_service import CollectionService

Execute payment collection

This endpoint executes a payment collection. Any collection will reduce the agent balance by service amount plus the service fee. Each collection must include a reference to corresponding quote and payment authorization token. Whether or not fields are mandatory depends on the service configuration

### Example

```python
from services.collection_service import CollectionService

def main():
    # Initialize the Collection service
    collection_service = CollectionService()
    data = {
        "quoteId": "03879033-303930",
        "customerPhonenumber": "691201123",
        "customerEmailaddress": "customer@email.com",
        "serviceNumber": "691201123",
        "trid": "eabd12-7494984-494044-d0",
    }

    # Execute the collection process
    collection_entity = collection_service.execute_collection(data)

    # Check if the collection was successful and print relevant information
    if isinstance(collection_entity, CollectionModel):
        print("Transaction Number:", collection_entity.ptn)
        print("Receipt Number:", collection_entity.receiptNumber)
        print("Verification Code:", collection_entity.veriCode)
        print("Status:", collection_entity.status)
    else:
        print("Failed to execute collection:", collection_entity)

if __name__ == "__main__":
    main()
```

### Parameters

Name | Type                                         | Description  | Notes
------------- |----------------------------------------------| ------------- | -------------
 **data** | [**payload**](../Model/CollectionRequest.md) | Collection Request | [optional]

### Return type

[**CollectionModel**](../Model/CollectionResponse.md)

### Authorization

Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`

All headers necessary for the API call are automatically managed by the SDK.

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

