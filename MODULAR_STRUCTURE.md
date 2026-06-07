# Modular API Structure - বাংলায় ব্যাখ্যা (Supplier Connect)

## 📁 Project Structure (প্রজেক্ট স্ট্রাকচার)

```
Supplier connect load test using Locust/
│
├── apis/                          # সব API test files এখানে
│   ├── base_user.py              # Base class - authentication handle করে
│   ├── authentication_api.py     # Login (phone + PIN)
│   ├── supplier_orders_api.py    # Supplier Orders tests
│   ├── supplier_requests_api.py  # Supplier Requests tests
│   ├── inventory_api.py          # Inventory CRUD tests
│   └── home_api.py               # Dashboard ও Top Companies tests
│
├── config/                        # Configuration files
│   ├── global_login.py           # One-time login setup
│   └── load_profiles.py          # Load test profiles
│
├── locustfile.py                 # Main file - সব API import করে
├── run_tests.py                  # Test run করার script
└── requirements.txt              # Dependencies
```

## 🎯 কিভাবে কাজ করে?

### 1. Base User (base_user.py)
- সব API test class এর parent
- Authentication handle করে
- Common headers set করে
- Login করে token নেয়

### 2. Individual API Files
প্রতিটি API এর জন্য আলাদা file:

#### authentication_api.py
```python
class AuthenticationAPI(BaseUser):
    @task
    def login(self):
        # Login with phone + PIN
        payload = {
            "phone": "01567839606",
            "pin": "0000"
        }
        self.client.post(
            "/api/v1/auth/login/",
            json=payload,
            name="Auth - Login"
        )
```

#### supplier_orders_api.py
```python
class SupplierOrdersAPI(BaseUser):
    @task(3)
    def list_orders(self):
        # List all supplier orders
        self.client.get(
            "/api/v3/supplier_orders/",
            name="Supplier Orders - List"
        )
    
    @task(2)
    def order_details(self):
        # Get order details
        self.client.get(
            "/api/v3/supplier_orders/1/",
            name="Supplier Orders - Details"
        )
```

#### supplier_requests_api.py
```python
class SupplierRequestAPI(BaseUser):
    @task(3)
    def list_requests(self):
        # List all supplier requests
        self.client.get(
            "/api/v3/supplier_requests/",
            name="Supplier Requests - List"
        )
    
    @task(2)
    def request_details(self):
        # Get request details
        self.client.get(
            "/api/v3/supplier_requests/1/",
            name="Supplier Requests - Details"
        )
```

#### inventory_api.py
```python
class InventoryAPI(BaseUser):
    @task(3)
    def list_inventory(self):
        # List all inventory items
        self.client.get(
            "/api/v1/inventory/",
            name="Inventory - List"
        )
    
    @task(2)
    def create_inventory(self):
        # Create a new inventory item
        payload = {
            "name": "Test Item",
            "quantity": 10,
            "unit_price": 100
        }
        self.client.post(
            "/api/v1/inventory/",
            json=payload,
            name="Inventory - Create"
        )
    
    @task(1)
    def inventory_details(self):
        # Get inventory item details
        self.client.get(
            "/api/v1/inventory/1/",
            name="Inventory - Details"
        )
    
    @task(1)
    def update_inventory(self):
        # Update an inventory item
        payload = {
            "name": "Updated Item",
            "quantity": 50
        }
        self.client.put(
            "/api/v1/inventory/1/",
            json=payload,
            name="Inventory - Update"
        )
    
    @task(1)
    def delete_inventory(self):
        # Delete an inventory item
        self.client.delete(
            "/api/v1/inventory/1/",
            name="Inventory - Delete"
        )
```

#### home_api.py
```python
class HomeAPI(BaseUser):
    @task(3)
    def get_dashboard(self):
        # Dashboard data
        self.client.get(
            "/api/v1/dashboard/",
            name="Dashboard"
        )
    
    @task(2)
    def get_top_companies(self):
        # Top companies list
        self.client.get(
            "/api/v1/dashboard/top_companies/",
            name="Top Companies"
        )
```

### 3. Main Locustfile
সব API class import করে:
```python
from apis.authentication_api import AuthenticationAPI
from apis.supplier_orders_api import SupplierOrdersAPI
from apis.supplier_requests_api import SupplierRequestAPI
from apis.inventory_api import InventoryAPI
from apis.home_api import HomeAPI
```

## 🚀 কিভাবে Run করবেন?

### সব API একসাথে test করতে:
```bash
python3 run_tests.py --quick
```
অথবা
```bash
python3 -m locust -f locustfile.py --host=http://52.220.47.3
```

### শুধু একটি API test করতে:

#### শুধু Authentication test:
```bash
python3 -m locust -f locustfile.py AuthenticationAPI --host=http://52.220.47.3
```

#### শুধু Home/Dashboard test:
```bash
python3 -m locust -f locustfile.py HomeAPI --host=http://52.220.47.3
```

#### শুধু Inventory test:
```bash
python3 -m locust -f locustfile.py InventoryAPI --host=http://52.220.47.3
```

#### শুধু Supplier Request test:
```bash
python3 -m locust -f locustfile.py SupplierRequestAPI --host=http://52.220.47.3
```

#### শুধু Supplier Orders test:
```bash
python3 -m locust -f locustfile.py SupplierOrdersAPI --host=http://52.220.47.3
```

## 📊 Task Weights কি?

`@task(number)` দিয়ে বলা হয় কোন task তুলনামূলক কতবার execute হবে:

```python
@task(3)  # বেশি বার execute হবে
def list_orders(self):
    pass

@task(1)  # তুলনামূলক কম execute হবে
def order_details(self):
    pass
```

উপরের example এ, `list_orders` প্রায় 3 গুণ বেশি call হবে `order_details` এর তুলনায়।

## 🔧 নতুন Endpoint যোগ করতে চান?

### উদাহরণ: Supplier Orders এ নতুন endpoint (Create Order) যোগ করা

`apis/supplier_orders_api.py` file খুলুন এবং যোগ করুন:

```python
@task(1)
def create_order(self):
    """Test creating a supplier order"""
    payload = {
        "supplier_id": 123,
        "items": [{"product_id": 1, "quantity": 10}]
    }
    self.client.post(
        "/api/v3/supplier_orders/",
        json=payload,
        name="Supplier Orders - Create"
    )
```

### উদাহরণ: নতুন API file তৈরি করা

ধরুন আপনি Suppliers API এর জন্য আলাদা file চান (উদাহরণস্বরূপ — নিচের endpoint গুলো আপনার আসল API অনুযায়ী বদলে নিন):

1. নতুন file তৈরি করুন: `apis/suppliers_api.py`

```python
from locust import task, between
from apis.base_user import BaseUser

class SuppliersAPI(BaseUser):
    wait_time = between(1, 3)

    @task
    def list_suppliers(self):
        self.client.get(
            "/api/v1/suppliers/",
            name="Suppliers - List"
        )
    
    @task
    def update_supplier(self):
        payload = {
            "name": "Test Supplier",
            "is_active": True
        }
        self.client.put(
            "/api/v1/suppliers/1/",
            json=payload,
            name="Suppliers - Update"
        )
```

2. `locustfile.py` তে import করুন:

```python
from apis.suppliers_api import SuppliersAPI
```

## ✅ সুবিধা (Advantages)

1. **Organized**: প্রতিটি API আলাদা file এ
2. **Easy to maintain**: একটা API change করলে শুধু সেই file change করতে হবে
3. **Selective testing**: যেকোনো একটা API আলাদা test করা যায়
4. **Reusable**: BaseUser সব জায়গায় reuse হয়
5. **Clear structure**: কোন endpoint কোথায় আছে সহজে বুঝা যায়

## 📝 বর্তমান Implementation

### ✅ Implemented APIs:

1. **AuthenticationAPI** - 1 endpoint
   - Login (phone + PIN)

2. **SupplierOrdersAPI** - 2 endpoints
   - List Orders
   - Order Details

3. **SupplierRequestAPI** - 2 endpoints
   - List Requests
   - Request Details

4. **InventoryAPI** - 5 endpoints
   - List
   - Create
   - Details
   - Update
   - Delete

5. **HomeAPI** - 2 endpoints
   - Dashboard
   - Top Companies

**Total: 13 endpoints** across 6 API files

## 🎯 পরবর্তী পদক্ষেপ

1. Test run করুন:
   ```bash
   python3 run_tests.py --quick
   ```

2. Specific API test করুন:
   ```bash
   python3 -m locust -f locustfile.py InventoryAPI --host=http://52.220.47.3
   ```

3. প্রয়োজন অনুযায়ী নতুন endpoint যোগ করুন

## 💡 Tips

- প্রতিটি API file এ `wait_time = between(1, 3)` দিয়ে request এর মধ্যে delay set করা
- `@task(weight)` দিয়ে কোন endpoint কতবার call হবে তা control করা
- `name="..."` parameter দিয়ে report এ readable name দেখানো
- `catch_response=True` দিয়ে custom success/failure logic লেখা যায়
