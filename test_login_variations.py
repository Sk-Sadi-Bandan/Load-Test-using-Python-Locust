#!/usr/bin/env python3
"""
Test different login variations to find what works
"""
import requests

HOST = "https://backend.amal.education"
API_KEY = "7ca7c0a9-4d15-4697-81ae-e0b9ded2502d"
EMAIL = "habib.qtec@gmail.com"
PASSWORD = "asdfgh"

print("=" * 70)
print("Testing Different Login Variations")
print("=" * 70)

# Test 1: With username and API key header
print("\n1️⃣ Test: username + x-api-key header")
try:
    resp = requests.post(
        f"{HOST}/api/accounts/sign-in/",
        json={"username": EMAIL, "password": PASSWORD},
        headers={"x-api-key": API_KEY, "Content-Type": "application/json"},
        timeout=10
    )
    print(f"   Status: {resp.status_code}")
    print(f"   Response: {resp.text[:150]}")
except Exception as e:
    print(f"   Error: {e}")

# Test 2: With email field and API key header
print("\n2️⃣ Test: email + x-api-key header")
try:
    resp = requests.post(
        f"{HOST}/api/accounts/sign-in/",
        json={"email": EMAIL, "password": PASSWORD},
        headers={"x-api-key": API_KEY, "Content-Type": "application/json"},
        timeout=10
    )
    print(f"   Status: {resp.status_code}")
    print(f"   Response: {resp.text[:150]}")
except Exception as e:
    print(f"   Error: {e}")

# Test 3: With username, NO API key header
print("\n3️⃣ Test: username, NO x-api-key header")
try:
    resp = requests.post(
        f"{HOST}/api/accounts/sign-in/",
        json={"username": EMAIL, "password": PASSWORD},
        headers={"Content-Type": "application/json"},
        timeout=10
    )
    print(f"   Status: {resp.status_code}")
    print(f"   Response: {resp.text[:150]}")
except Exception as e:
    print(f"   Error: {e}")

# Test 4: With email, NO API key header
print("\n4️⃣ Test: email, NO x-api-key header")
try:
    resp = requests.post(
        f"{HOST}/api/accounts/sign-in/",
        json={"email": EMAIL, "password": PASSWORD},
        headers={"Content-Type": "application/json"},
        timeout=10
    )
    print(f"   Status: {resp.status_code}")
    print(f"   Response: {resp.text[:150]}")
except Exception as e:
    print(f"   Error: {e}")

# Test 5: Check what staging expects (for comparison)
print("\n5️⃣ Test: Staging server (for comparison)")
try:
    resp = requests.post(
        "https://staging.amal.education/auth/login/api",
        json={"username": EMAIL, "password": PASSWORD},
        headers={"x-api-key": API_KEY, "Content-Type": "application/json"},
        timeout=10
    )
    print(f"   Status: {resp.status_code}")
    print(f"   Response: {resp.text[:150]}")
except Exception as e:
    print(f"   Error: {e}")

print("\n" + "=" * 70)
