# SmobilPay Python SDK Examples

This directory contains example scripts demonstrating how to use the SmobilPay Python SDK for various payment operations.

## Available Examples

### 1. Transaction Verification Example
**File**: `verify_transaction_example.py`

This example demonstrates how to use the `PaymentStatusService` to verify transaction status using either PTN (Payment Transaction Number) or TRID (Transaction Reference ID).

**Features**:
- Verify transactions using PTN
- Verify transactions using TRID
- Verify transactions using both parameters
- Error handling demonstration
- Detailed transaction status display
- Status analysis and recommendations

**Usage**:
```bash
python examples/verify_transaction_example.py
```

**What you'll learn**:
- How to initialize the PaymentStatusService
- How to handle different response scenarios
- How to process and display transaction status data
- How to handle errors gracefully
- Best practices for transaction verification

## Prerequisites

Before running the examples, make sure you have:

1. **Environment Configuration**: Set up your `.env` file with valid SmobilPay API credentials:
   ```bash
   SMOBIL_PAY_API_KEY=your_api_key
   SMOBIL_PAY_API_SECRET=your_api_secret
   SMOBIL_PAY_LIVE_MODE=True
   SMOBIL_PAY_API_URL=https://s3papidoc.smobilpay.maviance.info/v2
   SMOBIL_PAY_API_VERSION=3.0.0
   ```

2. **Dependencies**: Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Valid Transaction Data**: Replace the example PTN and TRID values in the scripts with real transaction identifiers for meaningful results.

## Running Examples

### From the project root:
```bash
# Run the transaction verification example
python examples/verify_transaction_example.py
```

### From the examples directory:
```bash
cd examples
python verify_transaction_example.py
```

## Expected Output

The examples will provide detailed output including:

- **Transaction Details**: PTN, merchant, amounts, timestamps, etc.
- **Status Analysis**: Interpretation of transaction status
- **Error Handling**: Proper error messages and handling
- **Logging**: Detailed logs for debugging

## Customization

To use these examples with your own data:

1. **Replace Example Values**: Update the PTN and TRID values in the scripts with real transaction identifiers
2. **Modify Error Handling**: Adjust error handling logic based on your application needs
3. **Customize Display**: Modify the `display_transaction_status` function to show only relevant information
4. **Add Validation**: Include additional validation logic for your specific use case

## Troubleshooting

### Common Issues:

1. **Import Errors**: Make sure you're running from the project root or have the correct Python path
2. **Authentication Errors**: Verify your API credentials in the `.env` file
3. **Network Errors**: Check your internet connection and API endpoint accessibility
4. **Invalid Transaction IDs**: Ensure you're using valid PTN or TRID values

### Debug Mode:

Enable debug logging by setting in your `.env` file:
```bash
SMOBIL_PAY_API_DEBUG=True
```

## Contributing

When adding new examples:

1. Follow the existing code structure and style
2. Include comprehensive documentation
3. Add proper error handling
4. Include usage examples in the README
5. Test with both valid and invalid data

## Support

For issues with the examples or SDK:

1. Check the main project README for general information
2. Review the API documentation at https://apidocs.smobilpay.com
3. Check the logs for detailed error information
4. Ensure your API credentials and configuration are correct 