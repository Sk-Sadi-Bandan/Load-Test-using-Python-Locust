# Project Structure — Supplier Connect

```
Supplier connect load test using Locust/
│
├── 📄 locustfile.py              # Main load testing file (imports all API classes)
├── 📄 locust.conf                # Configuration settings (host, users, run-time, reports)
├── 📄 run_tests.py               # Convenient test runner script
├── 📄 run_tests.bat              # Windows test runner
├── 📄 requirements.txt           # Python dependencies
│
├── 📁 apis/                      # API test classes
│   ├── base_user.py              # Base class (authentication handling)
│   ├── authentication_api.py     # Login (phone + PIN)
│   ├── supplier_orders_api.py    # Supplier Orders tests
│   ├── supplier_requests_api.py  # Supplier Requests tests
│   ├── inventory_api.py          # Inventory CRUD tests
│   └── home_api.py               # Dashboard ও Top Companies tests
│
├── 📁 config/                    # Configuration
│   ├── global_login.py           # One-time login setup
│   └── load_profiles.py          # Load test profiles
│
├── 📁 data/                      # Test data
│   ├── users.csv                 # Test users
│   └── test_payloads.json        # Sample payloads
│
├── 📁 utils/                     # Utilities
│   ├── csv_loader.py             # CSV loader
│   └── report_generator.py       # Report generator
│
├── 📚 Documentation
│   ├── README.md                 # Comprehensive documentation
│   ├── QUICKSTART.md             # Quick start guide
│   └── PROJECT_SUMMARY.md        # Project summary
│
├── 🔧 .gitignore                # Git ignore rules
│
└── 📊 reports/ (after running tests)
    ├── html_reports/*.html       # HTML test reports
    └── json_reports/*.csv        # Statistics / failures / exceptions CSV
```

## File Descriptions

### Core Files

- **locustfile.py**: Imports and coordinates all API test classes:
  - AuthenticationAPI
  - SupplierOrdersAPI
  - SupplierRequestAPI
  - InventoryAPI
  - HomeAPI

- **locust.conf**: Centralized configuration for:
  - Target host
  - Users / spawn-rate / run-time
  - Headless mode
  - HTML and CSV report paths

- **config/global_login.py**: One-time login (phone + PIN), Bearer token, X-API-Token

- **config/load_profiles.py**: Multi-stage ramp-up shapes (LoadTestShape)

- **run_tests.py**: Python script to run tests with:
  - Preset configurations (--quick, --medium, --stress)
  - Custom parameters
  - Automatic report generation

- **requirements.txt**: Python dependencies:
  - locust>=2.15.0
  - requests>=2.31.0

### Documentation

- **README.md**: Full documentation with installation, usage, and customization
- **QUICKSTART.md**: Quick setup guide
- **PROJECT_SUMMARY.md**: Complete project overview

### Configuration

- **.gitignore**: Excludes test reports, Python cache, and IDE files

## API Class Architecture

```
locustfile.py — imports all API classes (each is an HttpUser, inheriting BaseUser)
│
├── AuthenticationAPI
│   └── login()                       # phone + PIN
│
├── SupplierOrdersAPI
│   ├── list_orders()        @task(3)
│   └── order_details()      @task(2)
│
├── SupplierRequestAPI
│   ├── list_requests()      @task(3)
│   └── request_details()    @task(2)
│
├── InventoryAPI
│   ├── list_inventory()     @task(3)
│   ├── create_inventory()   @task(2)
│   ├── inventory_details()  @task(1)
│   ├── update_inventory()   @task(1)
│   └── delete_inventory()   @task(1)
│
└── HomeAPI
    ├── get_dashboard()      @task(3)
    └── get_top_companies()  @task(2)

```

## Test Flow

```
1. User starts test
   ↓
2. global_login.py runs ONCE → fetches & saves Bearer token
   ↓
3. Locust spawns users (based on -u parameter)
   ↓
4. Each user uses the shared token and runs the API class tasks (weighted)
   ↓
5. User waits 1-3 seconds
   ↓
6. Repeat from step 4
   ↓
7. Test ends (based on -t parameter or manual stop)
   ↓
8. Generate reports
```

## API Endpoint Coverage

```
Supplier Connect API (http://52.220.47.3)
│
├── /api/v1/auth/
│   └── login/                    ✅ Tested
│
├── /api/v3/supplier_orders/
│   ├── /                         ✅ Tested (List)
│   └── {id}/                     ✅ Tested (Details)
│
├── /api/v3/supplier_requests/
│   ├── /                         ✅ Tested (List)
│   └── {id}/                     ✅ Tested (Details)
│
├── /api/v1/inventory/
│   ├── /          (GET)          ✅ Tested (List)
│   ├── /          (POST)         ✅ Tested (Create)
│   ├── {id}/      (GET)          ✅ Tested (Details)
│   ├── {id}/      (PUT)          ✅ Tested (Update)
│   └── {id}/      (DELETE)       ✅ Tested (Delete)
│
└── /api/v1/dashboard/
    ├── /                         ✅ Tested (Dashboard)
    └── top_companies/            ✅ Tested (Top Companies)

```

## Usage Workflow

```
┌─────────────────────────────────────────┐
│  1. Install Dependencies                │
│  python3 -m pip install -r requirements │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  2. Choose Test Type                    │
│  • Web UI: python3 run_tests.py         │
│  • Quick:  python3 run_tests.py --quick │
│  • Custom: python3 run_tests.py -u 50   │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  3. Locust Runs Tests                   │
│  • Spawns users                         │
│  • Executes tasks                       │
│  • Collects metrics                     │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  4. View Results                        │
│  • HTML report                          │
│  • CSV data                             │
│  • Web UI (if applicable)               │
└─────────────────────────────────────────┘
```

## Quick Reference

### Run Commands

```bash
# Web UI (interactive)
python3 run_tests.py

# Quick test (10 users, 1 min)
python3 run_tests.py --quick

# Medium test (50 users, 5 min)
python3 run_tests.py --medium

# Stress test (100 users, 10 min)
python3 run_tests.py --stress

# Custom test
python3 run_tests.py --headless -u 25 -r 5 -t 120s --html report.html
```

### Direct Locust Commands

```bash
# Web UI
python3 -m locust -f locustfile.py --host=http://52.220.47.3

# Headless
python3 -m locust -f locustfile.py --host=http://52.220.47.3 --headless -u 10 -r 2 -t 60s

# With reports
python3 -m locust -f locustfile.py --host=http://52.220.47.3 --headless -u 10 -r 2 -t 60s --html=report.html --csv=results
```

### Key Metrics

- **RPS**: Requests per second (higher is better)
- **Response Time**: Average response time (lower is better)
- **Failure Rate**: Percentage of failed requests (should be 0%)
- **95th Percentile**: 95% of requests complete within this time

### Configuration Files

- **API Token**: `config/global_login.py` → `API_KEY`
- **Test Credentials**: `config/global_login.py` → phone / pin (অথবা `data/users.csv`)
- **Task Weights**: `apis/*.py` → `@task(weight)` decorators
- **Wait Time**: `apis/*.py` → `wait_time = between(1, 3)`
- **Host / Users / Run-time**: `locust.conf`