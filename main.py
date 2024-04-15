import logging
from models.account_model import AccountModel
from models.ping_model import PingModel
from services.account_service import AccountService
from services.ping_service import PingService

def main():
    # Setup basic configuration for logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Initialize the services
    ping_service = PingService()
    account_service = AccountService()

    # Perform a ping test
    response = ping_service.ping()
    if isinstance(response, PingModel):
        print("Ping successful:")
        print("Response Time:", getattr(response, 'time', 'N/A'))
        print("Response Version:", getattr(response, 'version', 'N/A'))
        print("Response Nonce:", getattr(response, 'nonce', 'N/A'))
        print("Response Key:", getattr(response, 'key', 'N/A'))
    else:
        print("Ping Error:", response)
        return  # Stop execution if ping fails

    # Fetch account information only if ping succeeds
    account_info = account_service.fetch_account_info()
    if isinstance(account_info, AccountModel):
        print("Account information:")
        print(f"Account Balance: {account_info.balance}")
        print(f"Account Currency: {account_info.currency}")
    else:
        print(f"Error fetching account information: {account_info}")

if __name__ == "__main__":
    main()
