# Smobilpay S3P API Client for Python

This Python SDK provides a convenient interface to the Smobilpay S3P API. It supports Python version 3.7 and above, making it easy to integrate into your Python applications to interact with Smobilpay services.

## Getting Started

### Prerequisites

Ensure you have Python 3.7+ installed on your system. You can check your Python version by running:

```bash
python --version
```

# Installation

Setting up the environment
Start by creating a .env file at the root of your project to store your Smobilpay API credentials securely:

```sh
touch .env
```

Edit the .env file to add your Smobilpay API credentials and configuration settings:

```bash
# SMOBILPAY API credentials
SMOBIL_PAY_API_KEY=Your-api-Key
SMOBIL_PAY_API_SECRET=Your-top-secret-key
SMOBIL_PAY_LIVE_MODE=True
SMOBIL_PAY_API_URL=https://s3papidoc.smobilpay.maviance.info/v2
SMOBIL_PAY_API_URL_STAGING=https://s3p.smobilpay.staging.maviance.info/v2
SMOBIL_PAY_API_VERSION=3.0.0
SMOBIL_PAY_API_DEBUG=False
```

Install dependencies
Ensure all required dependencies are installed by running:
```bash
pip install -r requirements.txt
```

# Docker Setup
To containerize the Smobilpay S3P API Client, use the following Dockerfile:

```bash
docker build -t smobilpay-sdk .

docker run -it smobilpay-sdk /bin/bash

# Within the docker 
# run
python main.py
```
## Usage

The official API documentation can be found at: https://apidocs.smobilpay.com

Here's a simple example to get you started with fetching account information using the SDK:

```py
from services.account_service import AccountService

def main():
    # Initialize the Account service
    account_service = AccountService()
    account = account_service.fetch_account_info()
    print(account)

if __name__ == "__main__":
    main()

```

Please visit https://apidocs.smobilpay.com for usage documentation


## Documentation for API Endpoints

All URIs are relative to */v2*

Class | Method                                                                  | HTTP request | Description
------------ |-------------------------------------------------------------------------| ------------ | -------------
*AccountService* | [**fetch_account_info**](docs/Api/AccountApi.md#accountget)             | **GET** /account | Retrieve account information and remaining account balance
*ServiceNumberVerificationApi* | [**verify_service_number**](docs/Api/AccountValidationApi.md#verifyget) | **GET** /verify | Verify service number
*CollectionService* | [**execute_payment_collection**](docs/Api/ConfirmApi.md#collectstdpost) | **POST** /collectstd | Execute payment collection
*PingService* | [**ping**](docs/Api/HealthcheckApi.md#pingget)                          | **GET** /ping | Check on the availability of the api
*BillService* | [**fetch_bills**](docs/Api/InitiateApi.md#billget)                      | **GET** /bill | Get bill payment handler
*QuoteService* | [**request_quote**](docs/Api/InitiateApi.md#quotestdpost)               | **POST** /quotestd | Request quote with price details about the payment
*SubscriptionService* | [**fetch_subscriptions**](docs/Api/InitiateApi.md#subscriptionget)      | **GET** /subscription | Get subscription payment handler
*CashinService* | [**fetch_cashins**](docs/Api/MasterdataApi.md#cashinget)                | **GET** /cashin | Retrieve available cashin packages
*CashoutService* | [**fetch_cashouts**](docs/Api/MasterdataApi.md#cashoutget)              | **GET** /cashout | Retrieves available cashout packages
*MerchantService* | [**fetch_merchants**](docs/Api/MasterdataApi.md#merchantget)                | **GET** /merchant | Retrieve list of merchants supported by the system.
*ProductService* | [**fetch_products**](docs/Api/MasterdataApi.md#productget)                  | **GET** /product | Retrieve list of available products
*ServiceApi* | [**fetch_services**](docs/Api/MasterdataApi.md#serviceget)                  | **GET** /service | Retrieve list of services supported by the system.
*ServiceApi* | [**fetch_service_by_id**](docs/Api/MasterdataApi.md#serviceidget)              | **GET** /service/{id} | Retrieve single service
*TopupService* | [**fetch_topups**](docs/Api/MasterdataApi.md#topupget)                      | **GET** /topup | Retrieve available topup packages
*VoucherService* | [**fetch_vouchers**](docs/Api/MasterdataApi.md#voucherget)                  | **GET** /voucher | Retrieve list of available vouchers to purchase
*PaymentHistoryService* | [**fetch_payment_history**](docs/Api/VerifyApi.md#historystdget)                | **GET** /historystd | Retrieve list of historic payment collection.
*PaymentStatusService* | [**fetch_payment_status**](docs/Api/VerifyApi.md#verifytxget)                    | **GET** /verifytx | Get the current payment collection status

## Flask API Endpoints

The Flask application provides REST API endpoints for easy integration:

Endpoint | Method | Description | Parameters
---------|--------|-------------|------------
`/api/ping` | GET | Check API availability | None
`/api/account` | GET | Get account information | None
`/api/cashin` | POST | Create cashin transaction | JSON payload
`/api/verifytx` | GET | Check transaction status | `ptn` or `trid` (query parameters)

## Documentation For Models

 - [Account](docs/Model/Account.md)
 - [Bill](docs/Model/Bill.md)
 - [Cashin](docs/Model/Cashin.md)
 - [Cashout](docs/Model/Cashout.md)
 - [CollectionRequest](docs/Model/CollectionRequest.md)
 - [CollectionResponse](docs/Model/CollectionResponse.md)
 - [Error](docs/Model/Error.md)
 - [I18nText](docs/Model/I18nText.md)
 - [Merchant](docs/Model/Merchant.md)
 - [PaymentStatus](docs/Model/PaymentStatus.md)
 - [Ping](docs/Model/Ping.md)
 - [Product](docs/Model/Product.md)
 - [Quote](docs/Model/Quote.md)
 - [QuoteRequest](docs/Model/QuoteRequest.md)
 - [Service](docs/Model/Service.md)
 - [Subscription](docs/Model/Subscription.md)
 - [Topup](docs/Model/Topup.md)


Testing Your Endpoints:

Open your web browser or use a tool like curl or Postman.
Test the /api/ping endpoint:
URL: http://127.0.0.1:5001/api/ping
Expected Response (Success):
 json 
{
  "key": "some_key",
  "nonce": "some_nonce",
  "status": "success",
  "time": "2023-10-27T10:00:00Z",
  "version": "3.0.0"
}
Expected Response (Error):
 json 
{
  "message": "Ping to Smobilpay API failed",
  "status": "error"
}
Test the /api/account endpoint:
URL: http://127.0.0.1:5001/api/account
Expected Response (Success):
 json 
{
  "balance": 1000.00,
  "currency": "XAF",
  "status": "success"
}
Expected Response (Error):
 json 
{
  "message": "Failed to fetch account information",
  "status": "error"
}

Test the /api/verifytx endpoint:
URL: http://127.0.0.1:5001/api/verifytx?ptn=1234567890
Expected Response (Success):
 json 
{
  "status": "success",
  "message": "Transaction status retrieved successfully",
  "data": [
    {
      "ptn": "1234567890",
      "status": "SUCCESS",
      "merchant": "merchant_code",
      "priceLocalCur": 1000.00,
      "localCur": "XAF",
      "receiptNumber": "REC123456",
      "veriCode": "VER789"
    }
  ]
}
Expected Response (Error - Missing Parameters):
 json 
{
  "status": "error",
  "message": "Either 'ptn' (Payment Transaction Number) or 'trid' (Transaction Reference ID) must be provided"
}

You can also test using the provided test script:
```bash
python test_verifytx.py
```

If you visit the terminal you will see the log messages.
7. Extending with Other Endpoints:

To add more endpoints:
Refer to the "Documentation for API Endpoints" in README.md.
Create a new route (e.g., /api/bills).
Import the relevant service class (e.g., BillService).
Create an instance of the service.
Call the appropriate method (e.g., fetch_bills).
Handle the response and return JSON.