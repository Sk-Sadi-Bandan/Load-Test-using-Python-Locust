# Supplier Connect — Locust Load Testing: Error Fixes & Improvements

## Summary
Fixed multiple critical errors in the Supplier Connect Locust codebase and implemented proper one-time login with concurrent API testing.

---

## Issues Found & Fixed

### 1. ❌ Missing `requirements.txt` Dependencies
**Problem:** The `requirements.txt` file was empty, causing import errors.

**Fix:** Added required dependencies:
```txt
locust>=2.15.0
requests>=2.31.0
```

---

### 2. ❌ Missing Main `locustfile.py`
**Problem:** No main entry point for Locust. The project structure had API files but no coordinator.

**Fix:** Created `locustfile.py` that:
- Coordinates all API test classes (Authentication, Supplier Orders, Supplier Requests, Inventory, Dashboard)
- Implements one-time login pattern
- Uses shared global authentication token
- Runs multiple APIs concurrently

---

### 3. ❌ Empty `home_api.py`
**Problem:** The file existed but had no implementation.

**Fix:** Implemented `HomeAPI` class with tasks:
```python
@task
def get_dashboard(self):
    self.client.get("/api/v1/dashboard/", name="Dashboard")

@task
def get_top_companies(self):
    self.client.get("/api/v1/dashboard/top_companies/", name="Top Companies")
```

---

### 4. ❌ Incorrect Run Command
**Problem:** `run_tests.bat` referenced `apis/` directory instead of a proper locustfile.

**Before:**
```batch
locust -f apis/ --config locust.conf
```

**After:**
```batch
locust -f locustfile.py --config locust.conf
```

---

### 5. ⚠️ Inefficient CSV Loading
**Problem:** `base_user.py` loaded CSV data for every user, but the data wasn't being used.

**Fix:** Removed redundant CSV loading from `BaseUser.on_start()` to improve performance.

---

## How the One-Time Login Works

### Architecture Flow

```
1. Test Start Event (Before any users spawn)
   └─> global_login.py executes
       └─> Makes ONE login request (phone + PIN)
           └─> Stores token in GLOBAL_TOKEN variable

2. Users Spawn (50 concurrent users)
   └─> Each user's on_start() method runs
       └─> Sets headers with GLOBAL_TOKEN
           └─> No individual login required

3. Load Testing Begins
   └─> All users make API calls with shared token
       ├─> SupplierOrdersAPI tasks
       ├─> SupplierRequestAPI tasks
       ├─> InventoryAPI tasks
       └─> HomeAPI tasks
```

### Key Components

#### `config/global_login.py`
- Uses Locust's `@events.test_start.add_listener` decorator
- Executes ONCE before any users spawn
- Makes a single login request (phone + PIN)
- Stores the Bearer token globally

#### `apis/base_user.py`
- Base class for all API test classes
- Sets authentication headers using `GLOBAL_TOKEN`
- All API classes inherit from this

#### `locustfile.py`
- Main entry point
- Defines `MultiAPIUser` class
- Coordinates multiple API test classes
- Each user randomly executes tasks from all APIs

---

## File Structure

```
Supplier connect load test using Locust/
├── locustfile.py                  ✅ NEW - Main entry point
├── requirements.txt               ✅ FIXED - Added dependencies
├── locust.conf                    ✓ Configuration file
├── run_tests.bat                  ✅ FIXED - Updated command
├── README.md                      ✅ NEW - Documentation
├── apis/
│   ├── base_user.py               ✅ IMPROVED - Removed redundant code
│   ├── authentication_api.py      ✓ Login (phone + PIN)
│   ├── supplier_orders_api.py     ✓ Already working
│   ├── supplier_requests_api.py   ✓ Already working
│   ├── inventory_api.py           ✓ Already working (full CRUD)
│   └── home_api.py                ✅ FIXED - Added implementation
├── config/
│   ├── global_login.py            ✓ Already working (one-time login)
│   └── load_profiles.py           ✓ Load test shapes
├── data/
│   ├── users.csv                  ✓ User credentials
│   └── test_payloads.json         ✓ Test data
└── utils/
    ├── csv_loader.py              ✓ CSV utility
    └── report_generator.py        ✓ Report utility
```

---

## Running the Tests

### Option 1: Batch Script (Recommended)
```bash
run_tests.bat
```

### Option 2: Command Line
```bash
locust -f locustfile.py --config locust.conf
```

### Option 3: With Web UI
```bash
locust -f locustfile.py
# Open http://localhost:8089
```

---

## Test Configuration

Current settings in `locust.conf`:
- **Host:** http://52.220.47.3
- **Users:** 50 concurrent users
- **Spawn Rate:** 5 users/second
- **Duration:** 3 minutes
- **Mode:** Headless (no UI)
- **Reports:** HTML and CSV formats

---

## Verification

✅ All dependencies installed successfully  
✅ All Python imports working correctly  
✅ One-time login implemented properly  
✅ Multiple APIs configured to run concurrently  
✅ Shared authentication token across all users  

---

## Benefits of This Implementation

1. **Efficient Login:** Only 1 login request instead of 50 (one per user)
2. **Realistic Load:** Simulates real-world scenario where users share sessions
3. **Better Performance:** Reduces authentication overhead
4. **Concurrent Testing:** Multiple APIs tested simultaneously
5. **Easy Configuration:** Simple config file for test parameters
6. **Comprehensive Reports:** HTML and CSV reports generated automatically

---

## Next Steps

To customize for your needs:

1. **Update Login Credentials** in `config/global_login.py`
2. **Add More APIs** by creating new files in `apis/` directory
3. **Adjust Load Profile** in `locust.conf` or use `config/load_profiles.py`
4. **Add Test Data** in `data/` directory if needed

---

## Testing Checklist

- [x] Fixed missing dependencies
- [x] Created main locustfile.py
- [x] Implemented home_api.py
- [x] Fixed run command
- [x] Optimized base_user.py
- [x] Verified all imports work
- [x] Documented the setup
- [x] One-time login working
- [x] Multiple APIs configured
- [x] Ready to run tests

---

**Status:** ✅ All errors fixed and ready for load testing!