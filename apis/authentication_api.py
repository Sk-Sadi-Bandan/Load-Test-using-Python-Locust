"""
Authentication API Load Tests
Tests for sign up, sign in
"""
from locust import task, between
from apis.base_user import BaseUser
from faker import Faker

fake = Faker()


class AuthenticationAPI(BaseUser):
    """Authentication API test scenarios"""
    
    wait_time = between(1, 3)
    
    def on_start(self):
        """Initialize test data"""
        self.access_token = None
        # Don't call parent on_start to avoid auto-login

    @task(1)
    def registration(self):
        """Test user registration"""
        payload = {
            "name": "Sadi supplier 606 (Load test)",
            "phone": "01567839606",
            "address": "nokhailam",
            "sourcing_area_id": 10,
            "pin": "0000",
            "bkash_number": "01712222022",
            "profile_image_url": "https://ifarmer-spply-chain.s3.ap-southeast-1.amazonaws.com/staging/profile_images/105-fahhh.png",
            "nid_front_url": "https://ifarmer-spply-chain.s3.ap-southeast-1.amazonaws.com/staging/users/nidfront/105-1780378390-1ec79596-front-54937_nid_front.jpg",
            "nid_back_url": "https://ifarmer-spply-chain.s3.ap-southeast-1.amazonaws.com/staging/users/nidback/105-1780378390-cb3a20dc-back-54937_nid_back.jpg",
            "bank_id": 103,
            "bank_name": "BRAC BANK ",
            "branch_id": 99342,
            "branch_name": "TANGAIL new",
            "account_name": "sadi qa",
            "account_number": "12345678901234322",
            "routing_number": "090260374332132"
        }
        
        headers = {
            "X-API-Token": "crzw188ZmS-lvJzb2tWq7lUfuBlCzbjfQyunP1vjZq4",
            "Content-Type": "application/json"
        }
        
        with self.client.post(
            "/api/v1/registrations/",
            json=payload,
            headers=headers,
            catch_response=True,
            name="Auth - Registration"
        ) as response:
            if response.status_code in (200, 201):
                try:
                    data = response.json()
                    self.access_token = data.get("access")
                except Exception:
                    pass
                response.success()
            elif response.status_code == 409:
                # User already exists
                response.success()
            else:
                response.failure(f"Sign up failed: {response.status_code} - {response.text[:200]}")
    
    @task(2)
    def login(self):
        """Test user login"""
        payload = {
            "phone": "01567839606",
            "pin": "0000"
        }
        
        headers = {
            "X-API-Token": "crzw188ZmS-lvJzb2tWq7lUfuBlCzbjfQyunP1vjZq4",
            "Content-Type": "application/json"
        }
        
        with self.client.post(
            "/api/v1/auth/login/",
            json=payload,
            headers=headers,
            catch_response=True,
            name="Auth - Login"
        ) as response:
            if response.status_code == 200:
                data = response.json()
                self.access_token = data.get("access")
                response.success()
            else:
                response.failure(f"Sign in failed: {response.status_code}")
