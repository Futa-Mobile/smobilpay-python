# InitiateApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_bills**](InitiateApi.md#billget) | **GET** /bill | Get bill payment handler
[**request_quote**](InitiateApi.md#quotestdpost) | **POST** /quotestd | Request quote with price details about the payment
[**fetch_subscriptions**](InitiateApi.md#subscriptionget) | **GET** /subscription | Get subscription payment handler

# **fetch_bills**
> def fetch_bills(self, merchant: str, serviceId: int, service_number: str) -> List[BillModel]:

Get bill payment handler

A request to this endpoint returns bill payment handler records for a service by a service number and retrieves its details if available. Bill payments come in 2 flavors – which are determined by the related service’s type: 1.  **SEARCHABLE_BILL** – When calling the endpoint for searchable bills, the result set will contain a list of all open bills for the selected service number. Each bill has its own Payment Item Identifier. 2.  **NON_SEARCHABLE_BILL** – When calling the endpoint for non-searchable bills, the result set will always contain a single bill item with a Payment Item ID to perform the collection for the provided service number.

### Example
```python
from services.bill_service import BillService

def main():
    # Initialize the Bill service with test credentials or from .env configuration
    bill_service = BillService()

    # Define the merchant code, service ID, and service number for which to fetch bills
    merchant = '12345'  # Example merchant code
    serviceid = 101  # Example service ID
    service_number = '20210430001'  # Example service number

    # Fetch bills using the Bill service
    bills = bill_service.fetch_bills(merchant, serviceid, service_number)

    # Check if the response is a list of BillModel instances or an error message
    if isinstance(bills, list):
        for bill in bills:
            print(f"Bill Number: {bill.billNumber}, Amount: {bill.amountLocalCur} {bill.localCur}")
            print(f"Due Date: {bill.billDueDate}, Type: {bill.billType}")
            print("-" * 40)
    else:
        print("Failed to fetch bills:", bills)

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

[**List[BillModel]**](../Model/Bill.md)

### Authorization

Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`

All headers necessary for the API call are automatically managed by the SDK.

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **request_quote**
> def request_quote(self, payment_item_id: str, amount: float) -> [QuoteModel]:

Request a quote with price details about the payment

Calling this web-service requests a quote from the system for the payment collection of the selected payment item and the specified payment amount in the system. The amount is to be chosen based on the services amountType, so can either be fixed or a custom entered value. The third parameter specifies the payment method that the customer has chosen in order to pay for the collection, as there may be additional charges depending on the selected method. A quote will only remain available for short time (a few minutes) and will expire. A quote will return the actual costs involved in collecting the payment. A quote always needs to be requested before making a collection.\"

### Example
```python
from services.quote_service import QuoteService

def main():
    # Initialize the Quote service
    quote_service = QuoteService()

    # Define the payment item ID and amount for which the quote is requested
    payment_item_id = "12345"
    amount = 100.00  # Assume the amount needs to be provided based on the service's amountType

    # Request a quote using the payment item ID and amount
    quote_response = quote_service.request_quote(payment_item_id, amount)

    # Check if the response is an instance of QuoteModel or an error message
    if isinstance(quote_response, QuoteModel):
        print("Quote Retrieved Successfully:")
        print(f"Quote ID: {quote_response.quoteId}")
        print(f"Expires At: {quote_response.expiresAt}")
        print(f"Pay Item ID: {quote_response.payItemId}")
        print(f"Amount in Local Currency: {quote_response.amountLocalCur}")
        print(f"Price in Local Currency: {quote_response.priceLocalCur}")
        print(f"Price in System Currency: {quote_response.priceSystemCur}")
        print(f"Local Currency: {quote_response.localCur}")
        print(f"System Currency: {quote_response.systemCur}")
        print(f"Promotion: {quote_response.promotion}")
    else:
        print("Failed to retrieve quote:")
        print(quote_response)  # Print the error message

if __name__ == "__main__":
    main()

```

### Parameters

Name | Type                                                                      | Description     | Notes
------------- |---------------------------------------------------------------------------|-----------------| -------------
 **payment_item_id** | **string**                                                                | payment item Id | 
 **amount** | **float**                                                                 | Item amount     | 

### Return type

[**QuoteModel**](../Model/Quote.md)

### Authorization

Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`

All headers necessary for the API call are automatically managed by the SDK.

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **fetch_subscriptions**
> def fetch_subscriptions(self, merchant: str, serviceId: int, service_number: str) -> List[SubscriptionModel]:

Get subscription payment handler

A request to this endpoint looks up a subscription record for a service by either service number or customer number and retrieves its details if available. When calling the endpoint the result set will contain a list of all available subscriptions found under the provided search criteria. Each subscription has its own Payment Item Identifier.

### Example
```python
from services.subscription_service import SubscriptionService

def main():
    # Initialize the Subscription service
    subscription_service = SubscriptionService()

    # Define the merchant code, service identifier, and optional service and customer numbers
    merchant = "12345"
    serviceid = "67890"
    service_number = "service123"  # Optional: service number
    customer_number = "customer123"  # Optional: customer number

    # Fetch subscriptions based on the defined parameters
    subscriptions = subscription_service.fetch_subscriptions(merchant, serviceid, service_number, customer_number)

    # Print details of each subscription or error messages
    for subscription in subscriptions:
        if isinstance(subscription, SubscriptionModel):
            print(f"Subscription Name: {subscription.name}")
            print(f"Service Number: {subscription.serviceNumber}")
            print(f"Customer Name: {subscription.customerName}")
            print(f"Start Date: {subscription.startDate}")
            print(f"Due Date: {subscription.dueDate}")
            print(f"End Date: {subscription.endDate}")
            print(f"Amount Local Currency: {subscription.amountLocalCur}")
        else:
            print(subscription)  # In case of error, print the error message

if __name__ == "__main__":
    main()

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant** | **string**| Unique merchant code |
 **serviceid** | **string**| Unique service Identifier |
 **serviceNumber** | **string**| service number with merchant (e.g. policy number with an insurance company or tax number for a governmental institution) | [optional]
 **customerNumber** | **string**| customer number with merchant (e.g. customer number with an insurance company or account number for a governmental institution) | [optional]

### Return type

[**List[SubscriptionModel]**](../Model/Subscription.md)

### Authorization

Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`

All headers necessary for the API call are automatically managed by the SDK.

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

