# PingService

All URIs are relative to `/v2`.

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping**](HealthcheckApi.md#pingget) | **GET** /ping | Check on the availability of the api

## `ping`
> from services.ping_service import PingService

Check out the availability of the api

This endpoint checks the availability of the API by returning a valid response object or an error message.
Its primary function is to verify the server's existence and operational status,
and it provides the current server time and time zone.

### Example Usage
```python
from services.ping_service import PingService

# Initialize the Ping service
ping_service = PingService()

# Call the ping method
response = ping_service.ping()

# Print the response details
print("Response Time:", getattr(response, 'time', 'N/A'))
print("Response Version:", getattr(response, 'version', 'N/A'))
print("Response Nonce:", getattr(response, 'nonce', 'N/A'))
print("Response Key:", getattr(response, 'key', 'N/A'))
print("Error:", getattr(response, 'error', 'No error'))
```

### Parameters

Name | Type        | Description | Notes
------------- |-------------|-------------| -------------
 **public_token** | **?string** | api key     | [default to defined .env]
 **secret_key** | **?string** | api secret  | [default to defined .env]

### Return type

Returns an instance of [**PingModel**](../Model/Ping.md)

### Authorization

No authorization required for this endpoint. Credentials and headers are handled internally by the SDK.

### HTTP request headers
- `Content-Type: application/json`
- `Accept: application/json`


All headers necessary for the API call are automatically managed by the SDK.


[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

