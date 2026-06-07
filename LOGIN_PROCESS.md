# 🔐 Login Process - বিস্তারিত ব্যাখ্যা (Supplier Connect)

## কিভাবে Login Handle হয়?

### 📋 Overview (সংক্ষেপে)

Login handle করার জন্য **2টি পদ্ধতি** আছে:

1. **Global Login** - Test শুরু হওয়ার আগে একবার login করে সব user এর জন্য token save করে
2. **Individual Login** - প্রতিটি user নিজে নিজে login করে

---

## 🎯 Method 1: Global Login (বর্তমানে এটি ব্যবহার হচ্ছে)

### File: `config/global_login.py`

```python
from locust import events
import requests

GLOBAL_TOKEN = None
API_KEY = "crzw188ZmS-lvJzb2tWq7lUfuBlCzbjfQyunP1vjZq4"

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    global GLOBAL_TOKEN
    print("\n🔐 Performing ONE-TIME login...")
    
    # Login payload
    login_payload = {
        "phone": "01567839606",
        "pin": "0000"
    }
    
    # Headers
    headers = {
        "X-API-Token": API_KEY,
        "Content-Type": "application/json"
    }
    
    # Login request
    resp = requests.post(
        environment.host + "/api/v1/auth/login/",
        json=login_payload,
        headers=headers
    )
    
    # Save token
    if resp.status_code == 200:
        GLOBAL_TOKEN = resp.json().get("access")
        print(f"✅ Global Bearer token saved")
```

### কিভাবে কাজ করে?

1. **Test শুরু হওয়ার আগে** (`@events.test_start.add_listener`)
2. **একবার login** করে
3. **Token save** করে `GLOBAL_TOKEN` variable এ
4. **সব user** এই token ব্যবহার করে

### সুবিধা:
- ✅ শুধু একবার login করতে হয়
- ✅ দ্রুত - প্রতিবার login করতে হয় না
- ✅ API তে কম load

---

## 🎯 Method 2: Individual Login (Fallback)

### File: `apis/base_user.py`

```python
class BaseUser(HttpUser):
    def on_start(self):
        """Set up headers with authentication"""
        # If global token exists, use it
        if GLOBAL_TOKEN:
            self.client.headers.update({
                "Authorization": f"Bearer {GLOBAL_TOKEN}",
                "X-API-Token": API_KEY,
                "Content-Type": "application/json"
            })
        else:
            # Otherwise, login to get token
            self.login()
    
    def login(self):
        """Login and get access token"""
        headers = {
            "X-API-Token": API_KEY,
            "Content-Type": "application/json"
        }
        
        payload = {
            "phone": "01567839606",
            "pin": "0000"
        }
        
        response = self.client.post(
            "/api/v1/auth/login/",
            json=payload,
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            access_token = data.get("access")
            
            # Update headers with token
            self.client.headers.update({
                "Authorization": f"Bearer {access_token}",
                "X-API-Token": API_KEY,
                "Content-Type": "application/json"
            })
```

### কিভাবে কাজ করে?

1. **প্রতিটি user শুরু** হওয়ার সময় (`on_start`)
2. **Check করে** `GLOBAL_TOKEN` আছে কিনা
3. **যদি থাকে** - সেটা ব্যবহার করে
4. **যদি না থাকে** - নিজে login করে

---

## 🔄 Complete Flow (সম্পূর্ণ প্রক্রিয়া)

### Step 1: Test Start
```
Locust শুরু হয় → config/global_login.py execute হয়
                 ↓
            একবার login করে
                 ↓
            GLOBAL_TOKEN save করে
```

### Step 2: User Spawn
```
প্রতিটি user spawn হয় → BaseUser.on_start() call হয়
                       ↓
                  GLOBAL_TOKEN check করে
                       ↓
                  যদি থাকে → সেটা ব্যবহার করে
                       ↓
                  যদি না থাকে → নিজে login করে
```

### Step 3: API Calls
```
User API call করে → Headers এ token থাকে
                   ↓
              Authorization: Bearer {token}
              X-API-Token: {api_key}
```

---

## 📊 Example Flow Diagram

```
┌─────────────────────────────────────────┐
│  Locust Test Starts                     │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  config/global_login.py                 │
│  - Login once                           │
│  - Save GLOBAL_TOKEN                    │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  User 1 Spawns                          │
│  - BaseUser.on_start()                  │
│  - Use GLOBAL_TOKEN                     │
│  - Set headers                          │
└────────────────┬────────────────────────┘
                 │
┌────────────────┼────────────────────────┐
│                │                        │
▼                ▼                        ▼
User 2         User 3                  User N
(same token)   (same token)            (same token)
│                │                        │
▼                ▼                        ▼
┌─────────────────────────────────────────┐
│  All users make API calls with token    │
│  GET /api/v3/supplier_orders/           │
│  GET /api/v1/dashboard/                 │
│  POST /api/v1/inventory/                │
└─────────────────────────────────────────┘
```

---

## 🔍 Headers কি পাঠানো হয়?

প্রতিটি API request এ এই headers পাঠানো হয়:

```python
{
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "X-API-Token": "crzw188ZmS-lvJzb2tWq7lUfuBlCzbjfQyunP1vjZq4",
    "Content-Type": "application/json"
}
```

### ব্যাখ্যা:
- **Authorization**: JWT token (login করে পাওয়া)
- **X-API-Token**: API key (backend এর requirement)
- **Content-Type**: JSON data পাঠানোর জন্য

---

## 🎭 Different API Classes

### AuthenticationAPI
```python
class AuthenticationAPI(BaseUser):
    def on_start(self):
        # Don't call parent on_start
        # কারণ এটি নিজেই login test করে
        self.test_phone = "01567839606"
        self.test_pin = "0000"
```

### SupplierOrdersAPI, SupplierRequestAPI, InventoryAPI, HomeAPI
```python
class SupplierOrdersAPI(BaseUser):
    def on_start(self):
        # Call parent on_start
        # GLOBAL_TOKEN ব্যবহার করে
        super().on_start()
```

---

## 🧪 Test করার সময় কি হয়?

### Console Output দেখবেন:

```bash
🔐 Performing ONE-TIME login...
📊 Login response status: 200
✅ Global Bearer token saved: eyJhbGciOiJIUzI1NiIsI...

[2024-12-06 00:15:00] Starting Locust 2.34.0
[2024-12-06 00:15:00] Spawning 10 users at a rate of 2 users/s
[2024-12-06 00:15:01] User 1 started
[2024-12-06 00:15:01] User 2 started
...
```

### Web UI তে দেখবেন:

1. **Statistics Tab**: 
   - Request count
   - Response times
   - Failure rate

2. **Charts Tab**:
   - Real-time graphs
   - Response time trends

3. **Failures Tab**:
   - যদি কোনো error হয়

---

## 🔧 Troubleshooting

### যদি login fail হয়:

**Check করুন:**
1. ✅ API host সঠিক আছে কিনা
2. ✅ Username/password সঠিক আছে কিনা
3. ✅ X-API-Token সঠিক আছে কিনা
4. ✅ Network connection আছে কিনা

**Console এ দেখবেন:**
```
❌ Login failed with status 401
Response: {"detail": "Invalid credentials"}
```

---

## 📝 Summary

1. **Global Login** - Test শুরুতে একবার login
2. **Token Save** - `GLOBAL_TOKEN` variable এ
3. **All Users** - একই token ব্যবহার করে
4. **Fallback** - যদি global token না থাকে, individual login
5. **Headers** - প্রতিটি request এ Authorization header

এই পদ্ধতিতে:
- ✅ দ্রুত test হয়
- ✅ API তে কম load
- ✅ Realistic user behavior
- ✅ Easy to maintain