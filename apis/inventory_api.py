"""
Inventory API Load Tests
Tests for inventory items
"""
from locust import task, between
from apis.base_user import BaseUser
from faker import Faker

fake = Faker()


class InventoryAPI(BaseUser):
    """Inventory API test scenarios"""
    
    wait_time = between(1, 3)

    def on_start(self):
        """Initialize"""
        super().on_start()
        self.inventory_id = None

    def _extract_inventory_id(self, data):
        """Recursively find a numeric inventory id in response data"""
        if isinstance(data, dict):
            for key in ("id", "pk", "inventory_id"):
                if key in data and data[key]:
                    return data[key]
            for value in data.values():
                result = self._extract_inventory_id(value)
                if result:
                    return result
        elif isinstance(data, list):
            for item in data:
                result = self._extract_inventory_id(item)
                if result:
                    return result
        return None

    def _get_inventory_list(self):
        """Test fetching inventory list"""
        self.client.get(
            "/api/v1/inventory/",
            name="Inventory - List"
        )

    def _create_inventory_item(self):
        """Test creating inventory item"""
        payload = {
            "name": "Potato",
            "picture_url": "https://ifarmer-spply-chain.s3.ap-southeast-1.amazonaws.com/staging/inventory/products/80-Sweet%20Potato.jpg",
            "price": "500.0",
            "company_name": "Syngenta",
            "unit_id": 1,
            "quantity": "100.2",
            "quality_parameters_desc": "Lomba misti potato"
        }

        with self.client.post(
            "/api/v1/inventory/",
            json=payload,
            catch_response=True,
            name="Inventory - Create"
        ) as response:
            if response.status_code in (200, 201):
                try:
                    data = response.json()
                    self.inventory_id = self._extract_inventory_id(data)
                except Exception:
                    self.inventory_id = None
                if not self.inventory_id:
                    self.inventory_id = 80
                response.success()
            else:
                self.inventory_id = None
                response.failure(f"Create failed: {response.status_code}")

    def _update_inventory_item(self):
        """Test updating inventory item"""
        payload = {
            "name": "Potato Update",
            "price": "300.0",
            "company_name": "Pran",
            "quantity": "200.2",
            "quality_parameters_desc": "Lomba misti potato update"
        }

        inv_id = getattr(self, "inventory_id", None) or 80

        with self.client.put(
            f"/api/v1/inventory/{inv_id}/",
            json=payload,
            catch_response=True,
            name="Inventory - Update"
        ) as response:
            if response.status_code in (200, 204):
                response.success()
            else:
                response.failure(f"Update failed: {response.status_code}")

    def _get_inventory_item(self):
        """Test fetching one inventory item"""
        inv_id = getattr(self, "inventory_id", None) or 80

        with self.client.get(
            f"/api/v1/inventory/{inv_id}/",
            catch_response=True,
            name="Inventory - Retrieve"
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Retrieve failed: {response.status_code}")

    def _delete_inventory_item(self):
        """Test deleting one inventory item"""
        inv_id = getattr(self, "inventory_id", None) or 80

        with self.client.delete(
            f"/api/v1/inventory/{inv_id}/",
            catch_response=True,
            name="Inventory - Delete"
        ) as response:
            if response.status_code in (200, 204):
                response.success()
            else:
                response.failure(f"Delete failed: {response.status_code}")

    @task
    def inventory_full_workflow(self):
        """Execute complete inventory workflow: List → Create → Update → Get → Delete"""
        self._get_inventory_list()
        self._create_inventory_item()
        self._update_inventory_item()
        self._get_inventory_item()
        self._delete_inventory_item()
