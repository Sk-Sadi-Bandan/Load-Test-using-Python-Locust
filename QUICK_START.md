# Quick Start Guide - Locust Load Testing (Supplier Connect)

## What Was Fixed?

Your Locust codebase had several critical errors that have been fixed:

1. **Empty requirements.txt** - Added Locust and requests dependencies
2. **Missing locustfile.py** - Created main entry point for tests
3. **Empty home_api.py** - Implemented dashboard (Home) API tests
4. **Wrong run command** - Fixed to use locustfile.py
5. **Inefficient code** - Removed redundant CSV loading

## How to Run Tests

### Step 1: Verify Setup (Recommended)
```bash
python validate_setup.py
```

This will check that everything is configured correctly.

### Step 2: Run Load Tests

**Option A: Using the batch file (Easiest)**
```bash
run_tests.bat
```

**Option B: Using command line**
```bash
locust -f locustfile.py --config locust.conf
```

**Option C: With Web UI (for interactive testing)**
```bash
locust -f locustfile.py
```
Then open http://localhost:8089 in your browser.

## Understanding Your Setup

### One-Time Login (Your Requirement)

Your setup now implements **one-time login** correctly:

```
Before Test Starts:
  └─> global_login.py runs ONCE
      └─> Makes 1 login request
          └─> Saves token to GLOBAL_TOKEN

When 50 Users Spawn:
  └─> Each user uses the SAME token
      └─> No individual logins needed
          └─> All users share authentication
```

### Multiple APIs Running Concurrently (Your Requirement)

All users will randomly execute tasks from these APIs:

- **Supplier Orders API** - `/api/v3/supplier_orders/`
- **Supplier Requests API** - `/api/v3/supplier_requests/`
- **Inventory API** - `/api/v1/inventory/` (full CRUD)
- **Dashboard (Home) API** - `/api/v1/dashboard/`, `/api/v1/dashboard/top_companies/`

This simulates realistic mixed workload.

## Current Configuration

From `locust.conf`:
- **Target:** http://52.220.47.3
- **Users:** 50 concurrent users
- **Spawn Rate:** 5 users per second
- **Duration:** 3 minutes
- **Reports:** HTML and CSV formats

## Customizing Your Tests

### Change Login Credentials

Edit `config/global_login.py`:
```python
login_payload = {
    "phone": "01567839606",
    "pin": "0000"
}
```

### Adjust Load Parameters

Edit `locust.conf`:
```ini
users=100          # Number of concurrent users
spawn-rate=10      # Users spawned per second
run-time=5m        # Test duration
```

### Add New API Tests

1. Create `apis/new_api.py`:
```python
from locust import task, between
from apis.base_user import BaseUser

class NewAPI(BaseUser):
    wait_time = between(1, 2)
    
    @task
    def test_endpoint(self):
        self.client.get("/api/endpoint/", name="Endpoint Name")
```

2. Import it in `locustfile.py`:
```python
from apis.new_api import NewAPI
```

`locustfile.py` already imports all the API classes, so once you add the import, `NewAPI` will run alongside the existing ones (Supplier Orders, Supplier Requests, Inventory, Dashboard).

## Viewing Results

After tests complete, check:

- **HTML Report:** `reports/html_reports/report.html`
- **CSV Data:** `reports/json_reports/locust_report_*.csv`

## Troubleshooting

### "Login failed" message
- Check credentials in `config/global_login.py`
- Verify the API endpoint is correct
- Check if the server is accessible

### Import errors
```bash
pip install -r requirements.txt
```

### Reports not generated
- Ensure `reports/html_reports/` and `reports/json_reports/` directories exist
- Check write permissions

## Need Help?

1. Run validation: `python validate_setup.py`
2. Check `FIXES_SUMMARY.md` for detailed information
3. Read `README.md` for comprehensive documentation

## Summary

✅ **One-time login** - Implemented correctly  
✅ **Multiple APIs** - Running concurrently  
✅ **All errors fixed** - Ready to use  
✅ **Validated** - All checks passed  

**You're ready to run load tests!**
