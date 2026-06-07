# ⚙️ Customizing Load Test Timing - Supplier Connect

## 📍 **File Locations**

### **Option 1: Simple Configuration (Most Common)**
**File:** `locust.conf`  
**Full Path:** `C:\Load_Testing_Locust\Supplier connect load test using Locust\locust.conf`

### **Option 2: Advanced Ramp-Up Profiles**
**File:** `load_profiles.py`  
**Full Path:** `C:\Load_Testing_Locust\Supplier connect load test using Locust\config\load_profiles.py`

---

## 🎯 **Option 1: Simple Configuration (Recommended)**

### **File: `locust.conf`**

এটি load test parameters কাস্টমাইজ করার সবচেয়ে সহজ উপায়।

### **Current Settings:**
```ini
host=http://52.220.47.3
users=1                     # মোট concurrent users
spawn-rate=1                # প্রতি সেকেন্ডে spawn হওয়া ইউজার (ramp-up rate)
run-time=10s                # মোট test duration
headless=false
html=reports/html_reports/report.html
csv=reports/json_reports/locust_report
```

### **Customization Examples:**

#### **Example 1: দ্রুত Ramp-Up**
```ini
users=50
spawn-rate=10              # প্রতি সেকেন্ডে 10 জন ইউজার (দ্রুত)
run-time=5m
```
- **Ramp-up সময়:** 50 ÷ 10 = **৫ সেকেন্ড**
- **Steady state:** ৪ মিনিট ৫৫ সেকেন্ড 50 জন ইউজার

#### **Example 2: ধীর Ramp-Up (ক্রমান্বয়ে)**
```ini
users=100
spawn-rate=2               # প্রতি সেকেন্ডে 2 জন (ধীর)
run-time=10m
```
- **Ramp-up সময়:** 100 ÷ 2 = **৫০ সেকেন্ড**
- **Steady state:** ৮ মিনিট ১০ সেকেন্ড 100 জন ইউজার

#### **Example 3: Spike Test (হঠাৎ চাপ)**
```ini
users=200
spawn-rate=50             # প্রতি সেকেন্ডে 50 জন (খুবই দ্রুত!)
run-time=2m
```
- **Ramp-up সময়:** 200 ÷ 50 = **৪ সেকেন্ড**
- **Steady state:** 1 মিনিট ৫৬ সেকেন্ড 200 জন ইউজার

#### **Example 4: দীর্ঘ Endurance Test**
```ini
users=30
spawn-rate=1               # প্রতি সেকেন্ডে 1 জন (অত্যন্ত ক্রমান্বয়ে)
run-time=30m
```
- **Ramp-up সময়:** 30 ÷ 1 = **৩০ সেকেন্ড**
- **Steady state:** ২৯ মিনিট ৩০ সেকেন্ড 30 জন ইউজার

### **Time Format Options:**
```ini
run-time=30s               # ৩০ সেকেন্ড
run-time=5m                # ৫ মিনিট
run-time=2h                # ২ ঘন্টা
run-time=300               # ৩০০ সেকেন্ড (no unit = সেকেন্ড)
```

---

## 🚀 **Option 2: Advanced Ramp-Up Profiles**

### **File: `config/load_profiles.py`**

Use this for **complex load patterns** with multiple stages.

### **Current Profile (HeavyLoad):**
```python
stages = [
    {"duration": 60, "users": 50, "spawn_rate": 5},      # Stage 1: 0-60s
    {"duration": 120, "users": 100, "spawn_rate": 10},   # Stage 2: 60-120s
    {"duration": 180, "users": 200, "spawn_rate": 20},   # Stage 3: 120-180s
]
```

**What this does:**
- **0-60 seconds:** Ramp up to 50 users at 5 users/sec
- **60-120 seconds:** Ramp up to 100 users at 10 users/sec
- **120-180 seconds:** Ramp up to 200 users at 20 users/sec
- **After 180 seconds:** Test stops

## 🚀 **Option 2: Advanced Ramp-Up Profiles**

### **File: `config/load_profiles.py`**

জটিল load patterns এর জন্য এটি ব্যবহার করুন।

### **Custom Profile Examples:**

#### **Example 1: Supplier Connect - Orders API Testing**
```python
from locust import LoadTestShape

class SupplierOrdersLoadTest(LoadTestShape):
    """
    Gradually increase orders API load
    """
    stages = [
        {"duration": 60, "users": 5, "spawn_rate": 1},      # Baseline
        {"duration": 180, "users": 20, "spawn_rate": 2},    # Ramp to 20
        {"duration": 360, "users": 50, "spawn_rate": 5},    # Heavy load
        {"duration": 420, "users": 50, "spawn_rate": 0},    # Hold for 1 min
        {"duration": 480, "users": 0, "spawn_rate": 10},    # Ramp down
    ]
    
    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                return (stage["users"], stage["spawn_rate"])
        return None
```

#### **Example 2: Inventory API - Spike Test**
```python
from locust import LoadTestShape

class InventorySpikeTest(LoadTestShape):
    """
    Test inventory API with sudden spike
    """
    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 1},     # Baseline
        {"duration": 90, "users": 100, "spawn_rate": 30},   # SPIKE!
        {"duration": 180, "users": 100, "spawn_rate": 0},   # Hold spike
        {"duration": 240, "users": 10, "spawn_rate": 20},   # Back to baseline
    ]
    
    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                return (stage["users"], stage["spawn_rate"])
        return None
```

#### **Example 3: Supplier Requests - Step Load**
```python
from locust import LoadTestShape

class SupplierRequestsStepLoad(LoadTestShape):
    """
    Step-wise load increase for requests
    """
    stages = [
        {"duration": 120, "users": 10, "spawn_rate": 2},    # Step 1
        {"duration": 240, "users": 30, "spawn_rate": 3},    # Step 2
        {"duration": 360, "users": 50, "spawn_rate": 5},    # Step 3
        {"duration": 480, "users": 70, "spawn_rate": 5},    # Step 4
    ]
    
    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                return (stage["users"], stage["spawn_rate"])
        return None
```

---

## 🔧 **কিভাবে Load Profiles ব্যবহার করবেন**

### **Step 1: `config/load_profiles.py` সম্পাদনা করুন**

আপনার custom profile যোগ করুন বা বিদ্যমান class modify করুন।

### **Step 2: `locustfile.py` আপডেট করুন**

এই লাইন যোগ করুন `locustfile.py` এর শেষে:

```python
# locustfile.py শেষে
from config.load_profiles import SupplierOrdersLoadTest  # আপনার custom class
```

**অথবা** সরল উপায় - শুধু class নাম দিয়ে চালান:

```bash
locust -f locustfile.py --host=http://52.220.47.3 --headless --class-name SupplierOrdersLoadTest
```

---

## 📊 **সাধারণ vs উন্নত তুলনা**

| বৈশিষ্ট্য | `locust.conf` | `load_profiles.py` |
|---------|-------------|-------------------|
| **ব্যবহার সহজতা** | ⭐⭐⭐⭐⭐ খুব সহজ | ⭐⭐⭐ মাঝারি |
| **Ramp-up নিয়ন্ত্রণ** | একক হার | মাল্টি-স্টেজ |
| **Load patterns** | লিনিয়ার শুধু | যেকোনো pattern |
| **উপযুক্ত** | বেশিরভাগ test | জটিল scenario |
| **ফাইল অবস্থান** | Root directory | `config/` ফোল্ডার |

---

## 🎯 **Recommended Settings by Supplier Connect Test Type**

### **1. Smoke Test (দ্রুত যাচাই)**
**File:** `locust.conf`
```ini
users=5
spawn-rate=1
run-time=1m
```
**কোনটা টেস্ট করে:** সব API endpoints সাধারণ (Supplier Orders, Inventory, Dashboard)

### **2. Load Test (স্বাভাবিক ট্রাফিক)**
**File:** `locust.conf`
```ini
users=20
spawn-rate=5
run-time=5m
```
**কোনটা টেস্ট করে:** একযোগে multiple users Supplier Connect API ব্যবহার করছে

### **3. Stress Test (সর্বোচ্চ চাপ খুঁজবে)**
**File:** `config/load_profiles.py`
```python
stages = [
    {"duration": 60, "users": 20, "spawn_rate": 5},      # Start
    {"duration": 180, "users": 50, "spawn_rate": 10},    # Ramp up
    {"duration": 360, "users": 100, "spawn_rate": 20},   # Heavy load
]
```

### **4. Spike Test (আকস্মিক ট্রাফিক)**
**File:** `config/load_profiles.py`
```python
stages = [
    {"duration": 30, "users": 5, "spawn_rate": 1},       # Baseline
    {"duration": 60, "users": 100, "spawn_rate": 50},    # SPIKE!
    {"duration": 120, "users": 5, "spawn_rate": 20},     # Back to normal
]
```

### **5. Endurance Test (দীর্ঘ সময়ের পরীক্ষা)**
**File:** `locust.conf`
```ini
users=15
spawn-rate=2
run-time=30m
```
**উদ্দেশ্য:** Supplier Connect API memory leaks, connection pooling issues detect করবে

---

## 🔍 **Understanding the Parameters**

### **`users`**
- মোট concurrent virtual users
- বেশি = আরও বেশি লোড সিস্টেমে

### **`spawn-rate`**
- প্রতি সেকেন্ডে কতজন ইউজার add করবে
- **বেশি spawn-rate** = দ্রুত ramp-up, আক্রমণাত্মক
- **কম spawn-rate** = ধীর ramp-up, ক্রমান্বয়ে

### **`run-time`**
- মোট test সময়কাল
- Format: `30s`, `5m`, `2h`, বা শুধু একটি সংখ্যা (সেকেন্ডে)

---

## ✅ **দ্রুত সম্পাদনা গাইড**

### **সাধারণ পরিবর্তনের জন্য:**
1. Open `locust.conf`
2. Edit `users`, `spawn-rate`, বা `run-time`
3. সংরক্ষণ করুন
4. চালান `run_tests.bat` বা `python run_tests.py --quick`

### **Supplier Connect API Test করতে:**
```bash
# Dashboard API test
python run_tests.py --quick

# Supplier Orders test
locust -f locustfile.py --host=http://52.220.47.3 --headless -u 10 -r 2 -t 60s SupplierOrdersAPI

# Inventory API test
locust -f locustfile.py --host=http://52.220.47.3 --headless -u 10 -r 2 -t 60s InventoryAPI
```

---

## 📋 **Summary**

| কী পরিবর্তন | File | Path |
|-----------|------|------|
| **Users সংখ্যা** | `locust.conf` | `C:\Load_Testing_Locust\...\locust.conf` |
| **Spawn rate** | `locust.conf` | `C:\Load_Testing_Locust\...\locust.conf` |
| **Test duration** | `locust.conf` | `C:\Load_Testing_Locust\...\locust.conf` |
| **Multi-stage ramp-up** | `load_profiles.py` | `C:\Load_Testing_Locust\...\config\load_profiles.py` |

---

## 🎉 **Quick Start**

**এখনই ramp-up সময় পরিবর্তন করতে:**

1. খুলুন: `locust.conf`
2. পরিবর্তন করুন: `spawn-rate=1` থেকে আপনার মান
3. সংরক্ষণ এবং চালান: `run_tests.bat` বা `python run_tests.py --medium`

**সম্পূর্ণ!** 🚀

### উদাহরণ কমান্ড:
```bash
# 50 ইউজার, 5/sec spawn rate, 5 মিনিট
locust -f locustfile.py --host=http://52.220.47.3 --headless -u 50 -r 5 -t 300s --csv=results

# 100 ইউজার, stress test
python run_tests.py --stress
```