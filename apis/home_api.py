"""
Dashboard API Load Tests
Tests for dashboard endpoints
"""
from locust import task, between
from apis.base_user import BaseUser

    
class DashboardAPI(BaseUser):
    """Dashboard API test scenarios"""
    
    wait_time = between(1, 3)

    @task(3)
    def get_supplier_requests(self):
        """Test supplier requests endpoint"""
        self.client.get(
            "/api/v3/supplier_requests?page=1&per_page=1&query=",
            name="Homepage - Supplier Requests"
        )
    
    @task(3)
    def get_supplier_orders(self):
        """Test supplier orders endpoint"""
        self.client.get(
            "/api/v3/supplier_orders?page=1&per_page=15&query=",
            name="Homepage - Supplier Orders"
        )
    
    @task(2)
    def get_dashboard(self):
        """Test dashboard endpoint"""
        self.client.get(
            "/api/v1/dashboard",
            name="Homepage - Dashboard"
        )
    
    @task(2)
    def get_top_companies(self):
        """Test top companies endpoint"""
        self.client.get(
            "/api/v1/dashboard/top_companies",
            name="Homepage - Top Companies"
        )
