# Project Setup Summary — Supplier Connect

## ✅ What Has Been Created

### Core Files
1. **locustfile.py** - Main load testing file that imports all API classes:
   - AuthenticationAPI (Login: phone + PIN)
   - SupplierOrdersAPI (List Orders, Order Details)
   - SupplierRequestAPI (List Requests, Request Details)
   - InventoryAPI (List, Create, Details, Update, Delete)
   - HomeAPI (Dashboard, Top Companies)

2. **locust.conf** - Configuration file with:
   - Target host
   - Users / spawn-rate / run-time
   - Headless mode
   - HTML and CSV report paths

3. **config/global_login.py** - One-time login (phone + PIN), Bearer token, X-API-Token

4. **requirements.txt** - Python dependencies:
   - locust>=2.15.0
   - requests>=2.31.0

5. **run_tests.py** - Convenient test runner with presets:
   - Quick test (10 users, 1 min)
   - Medium test (50 users, 5 min)
   - Stress test (100 users, 10 min)

6. **README.md** - Comprehensive documentation
7. **QUICKSTART.md** - Quick start guide
8. **.gitignore** - Git ignore rules

## ✅ Dependencies Installed

All required dependencies are now installed:
- ✓ locust (2.34.0)
- ✓ requests (2.32.5)

## 🚀 How to Run

### Option 1: Web UI (Recommended)
```bash
python3 run_tests.py
```
Then open http://localhost:8089

### Option 2: Quick Test
```bash
python3 run_tests.py --quick
```

### Option 3: Direct Locust Command
```bash
locust -f locustfile.py --host=http://52.220.47.3
```

## 📊 Test Coverage

The load tests cover these Supplier Connect API endpoints:

### Authentication
- ✓ Login (phone + PIN)

### Supplier Orders
- ✓ List Orders
- ✓ Order Details

### Supplier Requests
- ✓ List Requests
- ✓ Request Details

### Inventory (Full CRUD)
- ✓ List
- ✓ Create
- ✓ Details
- ✓ Update
- ✓ Delete

### Dashboard
- ✓ Dashboard
- ✓ Top Companies


## 🎯 Task Distribution

Tasks are weighted to simulate realistic user behavior:
- Supplier Orders: 30% (weight: 3)
- Dashboard: 30% (weight: 3)
- Supplier Requests: 20% (weight: 2)
- Inventory: 20% (weight: 2)

## ⚙️ Configuration

### API Settings
- **Host**: http://52.220.47.3
- **API Token**: crzw188ZmS-lvJzb2tWq7lUfuBlCzbjfQyunP1vjZq4
- **Test User**: 01567839606

### Load Test Defaults
- **Users**: 10
- **Spawn Rate**: 2 users/second
- **Wait Time**: 1-3 seconds between requests

## 📈 Expected Results

For a healthy API, you should see:
- **Response Time**: < 500ms average
- **Failure Rate**: < 1%
- **Requests/sec**: 20-50 (for 10 users)

## 🔧 Customization

### Change Test User
Edit `config/global_login.py`:
```python
login_payload = {
    "phone": "01567839606",
    "pin": "0000"
}
```

### Adjust Task Weights
Edit the relevant file in `apis/` and change the `@task(weight)` values:
```python
# apis/supplier_orders_api.py
@task(5)  # increase orders testing
def list_orders(self):
    ...

@task(1)  # reduce details testing
def order_details(self):
    ...
```

### Change Wait Time
Edit the API class in `apis/`:
```python
wait_time = between(2, 5)  # Wait 2-5 seconds
```

## 🎓 Next Steps

1. **Run a quick test** to verify everything works:
   ```bash
   python3 run_tests.py --quick
   ```

2. **Review the HTML report** generated after the test

3. **Gradually increase load**:
   - Start with 10 users
   - Then try 25 users
   - Then 50 users
   - Monitor server resources

4. **Customize for your needs**:
   - Add more endpoints
   - Adjust task weights
   - Create custom test scenarios

## 📚 Documentation

- **QUICKSTART.md** - Quick start guide
- **README.md** - Full documentation
- **locust.conf** - Configuration reference
- **config/global_login.py** - Login & credentials reference
- **locustfile.py** - Test scenarios (well-commented)

## ⚠️ Important Notes

1. **Test Environment**: Always test against staging/test environment
2. **API Token**: Update if the token expires
3. **Server Monitoring**: Watch server CPU/memory during tests
4. **Gradual Ramp-up**: Start small and increase gradually
5. **Data Cleanup**: Clean up test data after load testing (especially Inventory Create/Delete)

## 🆘 Troubleshooting

### Issue: Import errors
**Solution**: Ensure all dependencies are installed
```bash
python3 -m pip install -r requirements.txt
```

### Issue: Connection refused
**Solution**: Verify API is accessible
```bash
curl http://52.220.47.3/
```

### Issue: High failure rate
**Solution**: 
- Reduce number of users
- Check API token is valid
- Verify test credentials

## ✨ Features

- ✅ Realistic user behavior simulation
- ✅ Multiple test scenarios
- ✅ Configurable load patterns
- ✅ HTML and CSV reports
- ✅ Easy-to-use presets
- ✅ Well-documented code
- ✅ Modular API structure
- ✅ Authentication handling
- ✅ Error handling and retries

## 🎉 You're Ready!

Everything is set up and ready to go. Start with:

```bash
python3 run_tests.py --quick
```

Good luck with your load testing! 🚀
