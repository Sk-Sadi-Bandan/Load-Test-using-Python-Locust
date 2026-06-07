# Load Testing for Supplier Connect API

This project contains load testing scripts for the Supplier Connect API using Python and Locust.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

```
.
├── locustfile.py              # Main Locust file (imports all API classes)
├── locust.conf                # Configuration (host, users, run-time, reports)
├── requirements.txt           # Python dependencies
├── run_tests.py               # Test runner script
├── apis/                      # API test classes
│   ├── base_user.py
│   ├── authentication_api.py
│   ├── supplier_orders_api.py
│   ├── supplier_requests_api.py
│   ├── inventory_api.py
│   └── home_api.py
├── config/                    # global_login.py, load_profiles.py
└── README.md                  # This file
```

## Running the Tests

### Basic Usage

To run Locust with the web UI:

```bash
locust -f locustfile.py --host=http://52.220.47.3
```

Then open your browser and navigate to `http://localhost:8089` to access the Locust web interface.

### Headless Mode

To run Locust without the web UI (headless mode):

```bash
locust -f locustfile.py --host=http://52.220.47.3 --headless -u 10 -r 2 -t 60s
```

Parameters:
- `-u 10`: Number of users to simulate (10 users)
- `-r 2`: Spawn rate (2 users per second)
- `-t 60s`: Test duration (60 seconds)

### Advanced Options

Run with specific number of users and spawn rate:

```bash
locust -f locustfile.py --host=http://52.220.47.3 -u 50 -r 5
```

Run with HTML report generation:

```bash
locust -f locustfile.py --host=http://52.220.47.3 --headless -u 10 -r 2 -t 60s --html=report.html
```

Run with CSV output:

```bash
locust -f locustfile.py --host=http://52.220.47.3 --headless -u 10 -r 2 -t 60s --csv=results
```

## Test Scenarios

The load testing suite includes the following test scenarios:

### ✅ Authentication (সম্পূর্ণ)
1. **Login** - phone + PIN দিয়ে লগইন
2. **Bearer Token** - Bearer token handling
3. **X-API-Token** - API key handling

### ✅ Supplier Orders (মূল features)
1. **List Orders** - সব অর্ডার দেখা
2. **Order Details** - নির্দিষ্ট অর্ডারের ডিটেইলস

### ✅ Supplier Requests (মূল features)
1. **List Requests** - সব রিকোয়েস্ট দেখা
2. **Request Details** - নির্দিষ্ট রিকোয়েস্টের ডিটেইলস

### ✅ Inventory (সম্পূর্ণ CRUD)
1. **List** - সব inventory আইটেম
2. **Create** - নতুন আইটেম যোগ
3. **Update** - বিদ্যমান আইটেম আপডেট
4. **Detail** - নির্দিষ্ট আইটেমের তথ্য
5. **Delete** - আইটেম মুছে ফেলা

### ✅ Dashboard (মূল features)
1. **Main Dashboard** - ড্যাশবোর্ড ডেটা
2. **Top Companies** - শীর্ষ কোম্পানি তালিকা

## Configuration

### API Token

The API token is currently hardcoded in the script:
```python
"X-API-Token": "crzw188ZmS-lvJzb2tWq7lUfuBlCzbjfQyunP1vjZq4"
```

### Test User Credentials

Default test user credentials:
- Phone: `01567839606`
- PIN: `0000`

**Note:** For production load testing, you should use test accounts and update these credentials.

## Customization

### Adjusting Wait Time

Modify the `wait_time` in the API classes (in `apis/`):

```python
wait_time = between(1, 3)  # Wait 1-3 seconds between tasks
```

### Changing Task Weights

Each API class sets weights on its own `@task` methods. To make an endpoint run more or less often, edit the relevant file in `apis/`:

```python
# apis/supplier_orders_api.py
@task(5)  # run more often
def list_orders(self):
    ...

@task(1)  # run less often
def order_details(self):
    ...
```

### Running a Specific API

Each API is its own class, so you can run just one by passing its class name:

```bash
locust -f locustfile.py SupplierOrdersAPI --host=http://52.220.47.3
```

Replace `SupplierOrdersAPI` with `AuthenticationAPI`, `SupplierRequestAPI`, `InventoryAPI`, or `HomeAPI` as needed.

## Monitoring and Results

### Web UI Metrics

When using the web UI, you can monitor:
- Number of users
- Requests per second (RPS)
- Response times (min, max, median, average)
- Failure rate
- Charts and graphs

### Report Files

Generated reports include:
- HTML report: Visual representation of test results
- CSV files: Raw data for further analysis
  - `results_stats.csv`: Request statistics
  - `results_failures.csv`: Failed requests
  - `results_exceptions.csv`: Exceptions encountered

## Best Practices

1. **Start Small**: Begin with a small number of users and gradually increase
2. **Monitor Server**: Keep an eye on server resources during testing
3. **Test Environment**: Use a dedicated test environment, not production
4. **Realistic Scenarios**: Ensure test scenarios match real user behavior
5. **Data Cleanup**: Clean up test data after load testing (especially Inventory Create/Delete)

## Troubleshooting

### Common Issues

1. **Connection Errors**
   - Verify the host URL is correct
   - Check network connectivity
   - Ensure the API is running

2. **Authentication Failures**
   - Verify API token is valid
   - Check user credentials
   - Ensure the authentication endpoint is correct

3. **High Failure Rate**
   - Reduce the number of concurrent users
   - Increase wait time between requests
   - Check server capacity

## Example Commands

### Quick Test (10 users, 1 minute)
```bash
locust -f locustfile.py --host=http://52.220.47.3 --headless -u 10 -r 2 -t 60s
```

### Medium Test (50 users, 5 minutes)
```bash
locust -f locustfile.py --host=http://52.220.47.3 --headless -u 50 -r 5 -t 300s --html=report.html
```

### Stress Test (100 users, 10 minutes)
```bash
locust -f locustfile.py --host=http://52.220.47.3 --headless -u 100 -r 10 -t 600s --html=stress_report.html --csv=stress_results
```

### Interactive Web UI
```bash
locust -f locustfile.py --host=http://52.220.47.3
```

## Additional Resources

- [Locust Documentation](https://docs.locust.io/)
- [Locust Best Practices](https://docs.locust.io/en/stable/writing-a-locustfile.html)
- [Performance Testing Guide](https://docs.locust.io/en/stable/quickstart.html)

## License

This project is for testing purposes only.
