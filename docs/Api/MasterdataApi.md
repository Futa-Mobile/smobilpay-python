# Master data Apis

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_cashins**](MasterdataApi.md#cashinget) | **GET** /cashin | Retrieve available cashin packages
[**fetch_cashouts**](MasterdataApi.md#cashoutget) | **GET** /cashout | Retrieves available cashout packages
[**fetch_merchants**](MasterdataApi.md#merchantget) | **GET** /merchant | Retrieve list of merchants supported by the system.
[**fetch_products**](MasterdataApi.md#productget) | **GET** /product | Retrieve list of available products
[**fetch_services**](MasterdataApi.md#serviceget) | **GET** /service | Retrieve list of services supported by the system.
[**fetch_service_by_id**](MasterdataApi.md#serviceidget) | **GET** /service/{id} | Retrieve single service
[**fetch_topups**](MasterdataApi.md#topupget) | **GET** /topup | Retrieve available topup packages
[**fetch_vouchers**](MasterdataApi.md#voucherget) | **GET** /voucher | Retrieve list of available vouchers to purchase

# **fetch_cashins**
> def fetch_cashins(self, serviceId: int) -> List[CashinModel]:

Retrieve available cashin packages

This service provides available cashin packages to be made to the system.

### Example
```python
from services.cashin_service import CashinService

def main():
    # Initialize the Cashin service with API credentials
    cashin_service = CashinService()

    # Fetch cashin packages for a specific service ID
    service_id = 123  # Example service ID
    cashins = cashin_service.fetch_cashins(serviceid=service_id)

    # Check if the response is a list (successful fetch) or a string (error message)
    if isinstance(cashins, list):
        print("Fetched Cashin Packages:")
        for cashin in cashins:
            print(f"Name: {cashin.name}, Amount: {cashin.amountLocalCur} {cashin.localCur}")
    else:
        print("Failed to fetch cashin packages:", cashins)

if __name__ == "__main__":
    main()

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceId** | **int**| Filter cashin packages for only the selected service | [optional]

### Return type

[**List[CashinModel]**](../Model/Cashin.md)

### Authorization

No authorization required for this endpoint. Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`


All headers necessary for the API call are automatically managed by the SDK.

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **fetch_cashouts**

> def fetch_cashouts(self, serviceId: int) -> List[CashoutModel]:

Retrieves available cashout packages

This service provides available cashout packages to be made to the system.

### Example
```python
from services.cashout_service import CashoutService

def main():
    # Initialize the Cashout service with API credentials
    cashout_service = CashoutService()

    # Optional: Specify a service ID to filter cashout packages
    service_id = 101  # Example service ID

    # Fetch cashout packages for the specified service ID
    cashouts = cashout_service.fetch_cashouts(service_id=service_id)

    # Check if the response is a list (successful fetch) or a string (error message)
    if isinstance(cashouts, list):
        print("Fetched Cashout Packages:")
        for cashout in cashouts:
            print(f"Name: {cashout.name}, Amount: {cashout.amountLocalCur} {cashout.localCur}")
    else:
        print("Failed to fetch cashout packages:", cashouts)

if __name__ == "__main__":
    main()

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceId** | **int**| Filter cashout packages for only the selected service | [optional]

### Return type

[**List[CashoutModel]**](../Model/Cashout.md)

### Authorization

No authorization required for this endpoint. Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`


All headers necessary for the API call are automatically managed by the SDK.

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **fetch_merchants**
> def fetch_merchants(self) -> List[MerchantModel]:

Retrieve a list of merchants supported by the system.

Provides merchants supported by the system. Every service is assigned to a merchant.

### Example
```python
from services.merchant_service import MerchantService

def main():
    # Initialize the Merchant service
    merchant_service = MerchantService()

    # Fetch merchant information
    merchants = merchant_service.fetch_merchants()

    # Check the type of response and handle accordingly
    if isinstance(merchants, list):
        print("Fetched Merchants:")
        for merchant in merchants:
            print(f"Merchant Name: {merchant.name}, Country: {merchant.country}")
    else:
        print("Error:", merchants)

if __name__ == "__main__":
    main()

```

### Parameters

Name | Type | Description | Notes
------------- | ------------- |-------------| -------------
 **public_token** | **string**| api key     | [optional]
 **secret_key** | **string**| api secret  | [optional]

### Return type

[**List[MerchantModel]**](../Model/Merchant.md)

### Authorization

No authorization required for this endpoint. Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`


All headers necessary for the API call are automatically managed by the SDK.

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **fetch_products**

> def fetch_products(self, service_id: int = None) -> List[ProductModel]:

Retrieve a list of available products

This service provides a list of all available products for all services.

### Example
```python
from services.product_service import ProductService

def main():
    # Initialize the Product service with your API credentials
    product_service = ProductService(public_token="your_public_token", secret_key="your_secret_key")

    # Optionally, specify a service ID
    service_id = 123  # Replace with a valid service ID or remove if not filtering by service

    # Fetch product information
    products = product_service.fetch_products(service_id)

    # Check the type of response and handle accordingly
    if isinstance(products, list):
        print("Fetched Products:")
        for product in products:
            print(f"Product Name: {product.name}, Price: {product.amountLocalCur} {product.localCur}")
    else:
        print("Error:", products)

if __name__ == "__main__":
    main()

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **int**| Filter products to only the selected service | [optional]

### Return type

[**List[ProductModel]**](../Model/Product.md)

### Authorization

No authorization required for this endpoint. Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`


All headers necessary for the API call are automatically managed by the SDK.

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **fetch_services**
> def fetch_services(self) -> List[ServiceModel]:

Retrieve a list of services supported by the system.

This service endpoint provides information about the services supported by.
Each service has its own set of required input parameters which need to be provided during the collection request—starting with the prefix “isReq”.
It is recommended that the application UI is configured based on the response values provided here.
The service response will also specify the type of the service
and thus detail how the related payment items can be retrieved and collected.

### Example
```python
from services.service_api import ServiceApi

def main():
    # Initialize the Service API with your API credentials
    service_api = ServiceApi(public_token="your_public_token", secret_key="your_secret_key")

    # Fetch and display all services
    services = service_api.fetch_services()
    if isinstance(services, list):
        print("Available Services:")
        for service in services:
            print(f"Service Title: {service.title}, Type: {service.type}")
    else:
        print("Error fetching services:", services)

    # Optionally, fetch and display details for a specific service ID
    service_id = 101  # Replace with a valid service ID
    service_details = service_api.fetch_service_by_id(service_id)
    if isinstance(service_details, ServiceModel):
        print(f"\nService Details for ID {service_id}:")
        print(f"Title: {service_details.title}")
        print(f"Description: {service_details.description}")
        print(f"Category: {service_details.category}")
    else:
        print(f"Error fetching service details for ID {service_id}:", service_details)

if __name__ == "__main__":
    main()

```

### Parameters

Name | Type    | Description                                                     | Notes
------------- |---------|-----------------------------------------------------------------| -------------
 **service_id** | **int** | Unique  service Identifier. Only needed for fetch_service_by_id | 

### Return type

[**List[ServiceModel]**](../Model/Service.md)

### Authorization

No authorization required for this endpoint. Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`


All headers necessary for the API call are automatically managed by the SDK.

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **fetch_service_by_id**
> def fetch_service_by_id(self, service_id: int) -> [ServiceModel]:

Retrieve single service

This service endpoint provides information about the selected service. Each service has its own set of required input parameters which need to be provided during the collection request - starting with the prefix “isReq”. It is recommended that the application UI is configured based on the response values provided here. The service response will also specify the type of the service and thus detail how the related payment items can be retrieved and collected.

### Example
see above.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **int**| Unique  service Identifier. |

### Return type

[**[ServiceModel]**](../Model/Service.md)

### Authorization

No authorization required for this endpoint. Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`


All headers necessary for the API call are automatically managed by the SDK.

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **fetch_topups**
> def fetch_topups(self, service_id: int = None) -> List[TopupModel]:

Retrieve available topup packages

This service provides a list of all available topup packages.
DEPRECATED: Some providers will return a digital code for manual redeeming.
This code will be provided in the response object of a successful collection.
This functionality has been moved into the /voucher endpoint and will be removed in the next version of this API

### Example
```python
from services.topup_service import TopupService

def main():
    # Initialize the Topup service with API credentials
    topup_service = TopupService(public_token="your_public_token", secret_key="your_secret_key")

    # Optionally specify a service ID to filter topups
    service_id = 123  # Use None if you want to fetch all topups
    topups = topup_service.fetch_topups(service_id)

    if isinstance(topups, list):
        print("Available Topup Packages:")
        for topup in topups:
            print(f"Topup Name: {topup.name}, Amount: {topup.amountLocalCur} {topup.localCur}")
    else:
        print("Error:", topups)  # Print the error message

if __name__ == "__main__":
    main()

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **int**| Filter topups to only the selected service | [optional]

### Return type

[**List[TopupModel]**](../Model/Topup.md)

### Authorization

No authorization required for this endpoint. Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`


All headers necessary for the API call are automatically managed by the SDK.

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **fetch_vouchers**
> def fetch_vouchers(self, service_id: int = None) -> List[VoucherModel]:

Retrieve a list of available vouchers to purchase

This service provides a list of all available vouchers for all services. A purchase of a voucher will return a digital code for manual redeeming. This code will be provided in the response object of a successful collection.

### Example
```python
from services.voucher_service import VoucherService

def main():
    # Initialize the Voucher service with API credentials
    voucher_service = VoucherService(public_token="your_public_token", secret_key="your_secret_key")

    # Optionally specify a service ID to filter vouchers
    service_id = 123  # Use None if you want to fetch all vouchers
    vouchers = voucher_service.fetch_vouchers(service_id)

    if isinstance(vouchers, list):
        print("Available Vouchers:")
        for voucher in vouchers:
            print(f"Voucher Name: {voucher.name}, Amount: {voucher.amountLocalCur} {voucher.localCur}")
    else:
        print("Error:", vouchers)  # Print the error message

if __name__ == "__main__":
    main()

```

### Parameters

Name | Type | Description                                  | Notes
------------- | ------------- |----------------------------------------------| -------------
 **service_id** | **int**| Filter vouchers to only the selected service | [optional]

### Return type

[**List[VoucherModel]**](../Model/Product.md)

### Authorization

No authorization required for this endpoint. Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`


All headers necessary for the API call are automatically managed by the SDK.

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

