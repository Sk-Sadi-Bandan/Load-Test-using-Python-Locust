from locust import events
import requests

GLOBAL_TOKEN = None
API_KEY = "crzw188ZmS-lvJzb2tWq7lUfuBlCzbjfQyunP1vjZq4"
    
@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    global GLOBAL_TOKEN
    print("\n🔐 Performing ONE-TIME login...")

    login_payload = {
        "phone": "01567839606",
        "pin": "0000"
    }

    # Use X-API-Token header as required by backend
    headers = {
        "X-API-Token": API_KEY,
        "Content-Type": "application/json"
    }

    resp = requests.post(
        environment.host + "/api/v1/auth/login/",
        json=login_payload,
        headers=headers
    )

    print(f"📊 Login response status: {resp.status_code}")
    if resp.status_code == 200:
        GLOBAL_TOKEN = resp.json().get("access")
        print(f"✅ Global Bearer token saved: {GLOBAL_TOKEN[:20]}..." if GLOBAL_TOKEN else "❌ Token is None!")
    else:
        print(f"❌ Login failed with status {resp.status_code}")
        print(f"Response: {resp.text}")
