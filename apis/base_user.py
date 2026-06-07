"""
Base User class for all API tests
Handless authentication and common headers
"""
from locust import HttpUser
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from config.global_login import GLOBAL_TOKEN, API_KEY
except ImportError:
    # Fallback if global_login doesn't exist
    GLOBAL_TOKEN = None
    API_KEY = "crzw188ZmS-lvJzb2tWq7lUfuBlCzbjfQyunP1vjZq4"


class BaseUser(HttpUser):
    """
    Base user class that sets up authentication headers.
    All API test classes should inherit from this.
    """
    
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
            "phone": "01567839606",  # API uses username field for email
            "pin": "0000"
        }
        
        try:
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
            else:
                print(f"Login failed with status code: {response.status_code}")
        except Exception as e:
            print(f"Login error: {e}")
