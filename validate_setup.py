#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Validation script to check Locust setup before running tests
"""

import sys
import os

def check_imports():
    """Check if all required modules can be imported"""
    print("Checking imports...")
    try:
        import locust
        print("  [OK] locust imported successfully")
    except ImportError as e:
        print(f"  [FAIL] Failed to import locust: {e}")
        return False
    
    try:
        import requests
        print("  [OK] requests imported successfully")
    except ImportError as e:
        print(f"  [FAIL] Failed to import requests: {e}")
        return False
    
    try:
        from config.global_login import GLOBAL_TOKEN, API_KEY
        print("  [OK] global_login imported successfully")
    except ImportError as e:
        print(f"  [FAIL] Failed to import global_login: {e}")
        return False
    
    try:
        from apis.base_user import BaseUser
        print("  [OK] base_user imported successfully")
    except ImportError as e:
        print(f"  [FAIL] Failed to import base_user: {e}")
        return False
    
    try:
        from apis.home_api import DashboardAPI
        print("  [OK] dashboard_api imported successfully")
    except ImportError as e:
        print(f"  [FAIL] Failed to import dashboard_api: {e}")
        return False
    
    try:
        from apis.supplier_orders_api import HelpAPI
        print("  [OK] help_api imported successfully")
    except ImportError as e:
        print(f"  [FAIL] Failed to import help_api: {e}")
        return False
    
    try:
        from apis.pdf_api import PDFAPI
        print("  [OK] pdf_api imported successfully")
    except ImportError as e:
        print(f"  [FAIL] Failed to import pdf_api: {e}")
        return False
    
    return True

def check_files():
    """Check if all required files exist"""
    print("\nChecking required files...")
    required_files = [
        "locustfile.py",
        "locust.conf",
        "requirements.txt",
        "config/global_login.py",
        "apis/base_user.py",
        "apis/dashboard_api.py",
        "apis/help_api.py",
        "apis/pdf_api.py",
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"  [OK] {file} exists")
        else:
            print(f"  [FAIL] {file} missing")
            all_exist = False
    
    return all_exist

def check_config():
    """Check locust.conf configuration"""
    print("\nChecking configuration...")
    try:
        with open("locust.conf", "r") as f:
            config = f.read()
            
        required_params = ["host=", "users=", "spawn-rate=", "run-time="]
        for param in required_params:
            if param in config:
                print(f"  [OK] {param} configured")
            else:
                print(f"  [FAIL] {param} missing")
                return False
        
        return True
    except Exception as e:
        print(f"  [FAIL] Error reading locust.conf: {e}")
        return False

def main():
    """Run all validation checks"""
    print("=" * 60)
    print("Locust Setup Validation")
    print("=" * 60)
    
    checks = [
        ("File Structure", check_files),
        ("Python Imports", check_imports),
        ("Configuration", check_config),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n[{name}]")
        result = check_func()
        results.append((name, result))
    
    print("\n" + "=" * 60)
    print("Validation Summary")
    print("=" * 60)
    
    all_passed = True
    for name, result in results:
        status = "PASS" if result else "FAIL"
        symbol = "[OK]" if result else "[FAIL]"
        print(f"{symbol} {name}: {status}")
        if not result:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n[OK] All checks passed! Ready to run Locust tests.")
        print("\nRun tests with:")
        print("  run_tests.bat")
        print("  OR")
        print("  locust -f locustfile.py --config locust.conf")
        return 0
    else:
        print("\n[FAIL] Some checks failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

