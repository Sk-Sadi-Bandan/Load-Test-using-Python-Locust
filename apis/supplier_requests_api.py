"""
Supplier Request API Load Tests
Tests for supplier request management
"""
from locust import task, between
from apis.base_user import BaseUser


class SupplierRequestAPI(BaseUser):
    """Supplier Request API test scenarios"""
    
    wait_time = between(1, 3)

    @task(2)
    def get_supplier_requests(self):
        """Test supplier requests listing"""
        self.client.get(
            "/api/v3/supplier_requests/",
            name="Supplier Requests - List"
        )

    @task(1)
    def get_supplier_request_detail(self):
        """Test supplier request detail"""
        self.client.get(
            "/api/v3/supplier_requests/200/",
            name="Supplier Requests - Detail"
        )
