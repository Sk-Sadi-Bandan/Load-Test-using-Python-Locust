"""
Locust Load Testing for Supplier Connect API
Main file that imports all API test classes
"""

# Import all API test classes
from apis.authentication_api import AuthenticationAPI
from apis.home_api import DashboardAPI
from apis.inventory_api import InventoryAPI
from apis.supplier_requests_api import SupplierRequestAPI
from apis.supplier_orders_api import SupplierOrdersAPI

# All imported classes will be automatically discovered by Locust
# You can run specific classes using: locust -f locustfile.py ClassName

# Example:
# locust -f locustfile.py DashboardAPI
# locust -f locustfile.py SupplierRequestAPI
# locust -f locustfile.py SupplierOrdersAPI
# locust -f locustfile.py --host=http://52.220.47.3
