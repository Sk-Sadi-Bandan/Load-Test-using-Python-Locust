# 🚀 Locust Test Run Commands - সব Command এক জায়গায় (Supplier Connect)

## 📋 Table of Contents
1. [UI Mode Commands](#ui-mode-commands)
2. [Headless Mode Commands](#headless-mode-commands)
3. [Specific API Commands](#specific-api-commands)
4. [Quick Reference](#quick-reference)

---

## 🖥️ UI Mode Commands

### সব API একসাথে (Web UI)
```bash
python3 -m locust -f locustfile.py --host=http://52.220.47.3
```
তারপর browser এ যান: **http://localhost:8089**

### শুধু Authentication API (Web UI)
```bash
python3 -m locust -f locustfile.py AuthenticationAPI --host=http://52.220.47.3
```

### শুধু Dashboard (Home) API (Web UI)
```bash
python3 -m locust -f locustfile.py HomeAPI --host=http://52.220.47.3
```

### শুধু Inventory API (Web UI)
```bash
python3 -m locust -f locustfile.py InventoryAPI --host=http://52.220.47.3
```

### শুধু Supplier Request API (Web UI)
```bash
python3 -m locust -f locustfile.py SupplierRequestAPI --host=http://52.220.47.3
```

### শুধু Supplier Orders API (Web UI)
```bash
python3 -m locust -f locustfile.py SupplierOrdersAPI --host=http://52.220.47.3
```

---

## 🤖 Headless Mode Commands

### সব API একসাথে (Headless)

#### Quick Test (10 users, 1 minute)
```bash
python3 -m locust -f locustfile.py \
  --host=http://52.220.47.3 \
  --headless \
  -u 10 \
  -r 2 \
  -t 60s \
  --html quick_test_report.html \
  --csv quick_test_results
```

#### Medium Test (50 users, 5 minutes)
```bash
python3 -m locust -f locustfile.py \
  --host=http://52.220.47.3 \
  --headless \
  -u 50 \
  -r 5 \
  -t 300s \
  --html medium_test_report.html \
  --csv medium_test_results
```

#### Stress Test (100 users, 10 minutes)
```bash
python3 -m locust -f locustfile.py \
  --host=http://52.220.47.3 \
  --headless \
  -u 100 \
  -r 10 \
  -t 600s \
  --html stress_test_report.html \
  --csv stress_test_results
```

---

## 🎯 Specific API Commands

### Authentication API Only

#### UI Mode
```bash
python3 -m locust -f locustfile.py AuthenticationAPI --host=http://52.220.47.3
```

#### Headless Mode
```bash
python3 -m locust -f locustfile.py AuthenticationAPI \
  --host=http://52.220.47.3 \
  --headless \
  -u 10 \
  -r 2 \
  -t 60s \
  --html auth_report.html
```

---

### Dashboard (Home) API Only

#### UI Mode
```bash
python3 -m locust -f locustfile.py HomeAPI --host=http://52.220.47.3
```

#### Headless Mode
```bash
python3 -m locust -f locustfile.py HomeAPI \
  --host=http://52.220.47.3 \
  --headless \
  -u 10 \
  -r 2 \
  -t 60s \
  --html dashboard_report.html
```

---

### Inventory API Only

#### UI Mode
```bash
python3 -m locust -f locustfile.py InventoryAPI --host=http://52.220.47.3
```

#### Headless Mode
```bash
python3 -m locust -f locustfile.py InventoryAPI \
  --host=http://52.220.47.3 \
  --headless \
  -u 10 \
  -r 2 \
  -t 60s \
  --html inventory_report.html
```

---

### SupplierRequest API Only

#### UI Mode
```bash
python3 -m locust -f locustfile.py SupplierRequestAPI --host=http://52.220.47.3
```

#### Headless Mode
```bash
python3 -m locust -f locustfile.py SupplierRequestAPI \
  --host=http://52.220.47.3 \
  --headless \
  -u 10 \
  -r 2 \
  -t 60s \
  --html supplier_request_report.html
```

---

### SupplierOrders API Only

#### UI Mode
```bash
python3 -m locust -f locustfile.py SupplierOrdersAPI --host=http://52.220.47.3
```

#### Headless Mode
```bash
python3 -m locust -f locustfile.py SupplierOrdersAPI \
  --host=http://52.220.47.3 \
  --headless \
  -u 10 \
  -r 2 \
  -t 60s \
  --html supplier_orders_report.html
```

---

## 📊 Quick Reference

### Parameters ব্যাখ্যা:

| Parameter | অর্থ | Example |
|-----------|------|---------|
| `-f` | Locustfile path | `-f locustfile.py` |
| `--host` | API base URL | `--host=http://52.220.47.3` |
| `--headless` | UI ছাড়া run করবে | `--headless` |
| `-u` | Total users | `-u 10` |
| `-r` | Spawn rate (users/sec) | `-r 2` |
| `-t` | Run time | `-t 60s` (60 seconds) |
| `--html` | HTML report file | `--html report.html` |
| `--csv` | CSV results prefix | `--csv results` |

### Time Format:
- `60s` = 60 seconds
- `5m` = 5 minutes
- `1h` = 1 hour

---

## 🎨 UI Mode এ কিভাবে ব্যবহার করবেন?

### Step 1: Command Run করুন
```bash
python3 -m locust -f locustfile.py --host=http://52.220.47.3
```

### Step 2: Browser Open করুন
যান: **http://localhost:8089**

### Step 3: Configuration দিন
- **Number of users**: 10
- **Spawn rate**: 2
- **Host**: http://52.220.47.3 (already set)

### Step 4: Start করুন
"Start swarming" button এ click করুন

### Step 5: Monitor করুন
- **Statistics** tab: Request count, response time দেখুন
- **Charts** tab: Real-time graphs দেখুন
- **Failures** tab: Errors দেখুন

### Step 6: Stop করুন
"Stop" button এ click করুন

---

## 💡 Recommended Commands

### 🔰 শুরুতে (UI Mode):
```bash
python3 -m locust -f locustfile.py SupplierOrdersAPI --host=http://52.220.47.3
```
Browser এ: http://localhost:8089

### 🚀 Quick Test (Headless):
```bash
python3 -m locust -f locustfile.py SupplierOrdersAPI \
  --host=http://52.220.47.3 \
  --headless \
  -u 5 \
  -r 1 \
  -t 30s \
  --html supplier_orders_quick.html
```

### 📈 Full Test (Headless):
```bash
python3 -m locust -f locustfile.py \
  --host=http://52.220.47.3 \
  --headless \
  -u 20 \
  -r 5 \
  -t 120s \
  --html full_test.html \
  --csv full_test
```

---

## 🔧 Custom Commands

### আপনার নিজের configuration:
```bash
python3 -m locust -f locustfile.py [API_CLASS] \
  --host=http://52.220.47.3 \
  --headless \
  -u [USERS] \
  -r [SPAWN_RATE] \
  -t [TIME] \
  --html [REPORT_NAME].html
```

### Example:
```bash
python3 -m locust -f locustfile.py HomeAPI \
  --host=http://52.220.47.3 \
  --headless \
  -u 25 \
  -r 5 \
  -t 90s \
  --html my_dashboard_test.html
```

---

## 📝 Notes

1. **UI Mode** - Interactive, real-time monitoring
2. **Headless Mode** - Automated, generates reports
3. **Specific API** - শুধু একটা API test করতে চাইলে
4. **All APIs** - সব API একসাথে test করতে চাইলে

---

## 🎯 আপনার জন্য সবচেয়ে ভালো Command:

### UI Mode এ সব API test:
```bash
python3 -m locust -f locustfile.py --host=http://52.220.47.3
```

### UI Mode এ শুধু Supplier Orders API:
```bash
python3 -m locust -f locustfile.py SupplierOrdersAPI --host=http://52.220.47.3
```

Browser এ যান: **http://localhost:8089** এবং test start করুন! 🚀
