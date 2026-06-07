"""
Supplier Orders API Load Tests
Tests for supplier orders
"""
from locust import task, between
from apis.base_user import BaseUser
from faker import Faker

fake = Faker()


class SupplierOrdersAPI(BaseUser):
    """Supplier Order API test scenarios"""
    
    wait_time = between(1, 2)

    @task(2)
    def get_supplier_orders(self):
        """Test supplier orders listing"""
        self.client.get(
            "/api/v3/supplier_orders/",
            name="Supplier Orders - List"
        )

    @task(1)
    def get_supplier_order_detail(self):
        """Test supplier order detail"""
        self.client.get(
            "/api/v3/supplier_orders/103/",
            name="Supplier Orders - Detail"
        )
