# ✅ Supplier Connect API - Locust Load Testing

## 📋 Project Overview

এই প্রজেক্টটি **Supplier Connect** এর জন্য Locust-based load testing setup।

## ✅ কি আছে?

আপনার project এ ইতিমধ্যে সম্পূর্ণ Supplier Connect load testing structure আছে:

### 📁 APIs Structure:
```
apis/
├── base_user.py              ← Base class (সব API এটা use করে)
├── authentication_api.py     ← Login with phone + PIN
├── supplier_orders_api.py    ← Supplier Orders management
├── supplier_requests_api.py  ← Supplier Requests
├── inventory_api.py          ← Inventory management
└── home_api.py               ← Dashboard/Home API
```

## 🎯 কোন API তে কি আছে?

### AuthenticationAPI (authentication_api.py)
- ✅ Login: `/api/v1/auth/login/`
- ✅ Phone + PIN authentication
- ✅ Bearer Token handling

### SupplierOrdersAPI (supplier_orders_api.py)
- ✅ List Orders: `/api/v3/supplier_orders/`
- ✅ Order Details: `/api/v3/supplier_orders/{id}/`

### SupplierRequestAPI (supplier_requests_api.py)
- ✅ List Requests: `/api/v3/supplier_requests/`
- ✅ Request Details: `/api/v3/supplier_requests/{id}/`

### InventoryAPI (inventory_api.py)
- ✅ List Inventory: `/api/v1/inventory/`
- ✅ Create Inventory: POST `/api/v1/inventory/`
- ✅ Update Inventory: PUT `/api/v1/inventory/{id}/`
- ✅ Delete Inventory: DELETE `/api/v1/inventory/{id}/`

### HomeAPI (home_api.py)
- ✅ Dashboard: `/api/v1/dashboard/`
- ✅ Top Companies: `/api/v1/dashboard/top_companies/`

## 🚀 Test চালানোর উপায়

### সব API একসাথে test:
```bash
python run_tests.py --quick
python run_tests.py --medium
python run_tests.py --stress
```

### শুধু Supplier Orders test:
```bash
locust -f locustfile.py --host=http://52.220.47.3 --headless -u 10 -r 2 -t 60s SupplierOrdersAPI
```

### শুধু Inventory test:
```bash
locust -f locustfile.py --host=http://52.220.47.3 --headless -u 10 -r 2 -t 60s InventoryAPI
```

### শুধু Authentication test:
```bash
locust -f locustfile.py --host=http://52.220.47.3 --headless -u 5 -r 1 -t 30s AuthenticationAPI
```

## 📊 Configuration

### Credentials
- Phone: `01567839606`
- PIN: `0000`
- Host: `http://52.220.47.3`

### Default Load Test Configs
| Type | Users | Spawn Rate | Duration | CSV Output |
|------|-------|-----------|----------|-----------|
| **Quick** | 5 | 5/s | 15s | `quick_test_results_*.csv` |
| **Medium** | 10 | 10/s | 30s | `medium_test_results_*.csv` |
| **Stress** | 15 | 15/s | 45s | `stress_test_results_*.csv` |

## 📈 Reports দেখবেন কোথায়

Test চালানোর পর:
- **HTML Report**: `quick_test_report.html`, `medium_test_report.html`, `stress_test_report.html`
- **CSV Data**: 
  - `results_stats.csv` - Performance stats
  - `results_failures.csv` - Failed requests
  - `results_exceptions.csv` - Errors

## 🔧 নতুন Endpoint যোগ করতে চান?

যেকোনো API file খুলে নতুন `@task` যোগ করুন। যেমন `supplier_orders_api.py` এ:

```python
@task(2)
def create_order(self):
    """Test order creation"""
    payload = {
        "supplier_id": 123,
        "items": [{"product": "item1", "qty": 10}]
    }
    self.client.post(
        "/api/v3/supplier_orders/",
        json=payload,
        name="Supplier Orders - Create"
    )
```

## 📚 File Structure

```
├── locustfile.py             ← Main file (সব API import করে)
├── run_tests.py              ← Test runner script
├── locust.conf               ← Configuration file
├── requirements.txt          ← Python dependencies
│
├── apis/
│   ├── base_user.py          ← Base class with auth
│   ├── authentication_api.py  
│   ├── supplier_orders_api.py 
│   ├── supplier_requests_api.py
│   ├── inventory_api.py       
│   └── home_api.py            
│
├── config/
│   ├── global_login.py        ← Global token handling
│   └── load_profiles.py       ← Load profiles
│
├── data/
│   ├── test_payloads.json     ← Sample payloads
│   └── users.csv              ← Test users
│
└── utils/
    ├── csv_loader.py          ← CSV utilities
    └── report_generator.py    ← Report generation
```

## ✨ Key Features

1. ✅ **Modular Structure** - প্রতিটি API আলাদা file এ
2. ✅ **Easy to Maintain** - একটা API change করলে শুধু সেই file change
3. ✅ **Selective Testing** - যেকোনো একটা API আলাদা test করা যায়
4. ✅ **Auto CSV Reports** - প্রতিটি test এর পর CSV generate হয়
5. ✅ **Configurable** - `locust.conf` থেকে সব adjust করা যায়

## 🚀 দ্রুত শুরু

```bash
# ১. Dependencies install
pip install -r requirements.txt

# ২. Setup validate করুন
python validate_setup.py

# ३. Quick test চালান
python run_tests.py --quick

# ४. Report দেখুন
start quick_test_report.html
```

## 📞 Support

যদি কোনো API add/modify করতে চান:
- সংশ্লিষ্ট file খুলুন (`supplier_orders_api.py` ইত্যাদি)
- নতুন `@task` মেথড যোগ করুন
- Test চালান: `python run_tests.py --quick`

---

**Status**: ✅ Ready to Load Test Supplier Connect API
