#!/usr/bin/env python3
"""
Quick diagnostic script to test login and API endpoints
Run this to see why your load tests are failing
"""
import requests

# Configuration
HOST = "http://52.220.47.3"
API_KEY = "crzw188ZmS-lvJzb2tWq7lUfuBlCzbjfQyunP1vjZq4"
PHONE = "01567839606"
PIN = "0000"

print("=" * 60)
print("🔍 DIAGNOSTIC TEST - Checking API Authentication")
print("=" * 60)

# Test 1: Login
print("\n1️⃣ Testing Login Endpoint...")
print(f"   URL: {HOST}/api/v1/auth/login/")
login_payload = {"phone": PHONE, "pin": PIN}
headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

try:
    resp = requests.post(f"{HOST}/api/v1/auth/login/", json=login_payload, headers=headers, timeout=10)
    print(f"   Status Code: {resp.status_code}")
    print(f"   Response: {resp.text[:200]}")
    
    if resp.status_code == 200:
        token = resp.json().get("access")
        print(f"   ✅ Login successful!")
        print(f"   Token (first 20 chars): {token[:20] if token else 'None'}...")
    else:
        print(f"   ❌ Login failed!")
        token = None
except Exception as e:
    print(f"   ❌ Error: {e}")
    token = None

# Test 2: Try API endpoints with the token
if token:
    print("\n2️⃣ Testing Dashboard/Supplier Endpoints with Token...")
    headers = {
        "Authorization": f"Bearer {token}",
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    endpoints = [
        "/api/v3/supplier_requests?page=1&per_page=1&query=",
        "/api/v3/supplier_orders?page=1&per_page=115&query=",
        "/api/v1/dashboard",
        "/api/v1/dashboard/top_companies"
    ]

    for endpoint in endpoints:
        try:
            url = f"{HOST}{endpoint}"
            resp = requests.get(url, headers=headers, timeout=10)
            print(f"   URL: {url}")
            print(f"   Status Code: {resp.status_code}")
            print(f"   Response: {resp.text[:200]}")

            if resp.status_code == 200:
                print(f"   ✅ {endpoint} works!")
            else:
                print(f"   ❌ {endpoint} failed!")
        except Exception as e:
            print(f"   ❌ Error calling {endpoint}: {e}")
else:
    print("\n2️⃣ Skipping endpoint tests (no token)")

# Test 3: Check if server is reachable
print("\n3️⃣ Testing Server Connectivity...")
try:
    resp = requests.get(HOST, timeout=5)
    print(f"   Server is reachable (Status: {resp.status_code})")
except Exception as e:
    print(f"   ❌ Server unreachable: {e}")

print("\n" + "=" * 60)
print("DIAGNOSIS COMPLETE")
print("=" * 60)
