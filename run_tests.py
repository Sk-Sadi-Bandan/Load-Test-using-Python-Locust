#!/usr/bin/env python3
"""
Simple script to run Locust load tests with common configurations
"""

import sys
import subprocess
import argparse


def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import locust
        import faker
        print("✓ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("\nPlease install dependencies:")
        print("  pip install -r requirements.txt")
        return False


def run_locust(args):
    """Run Locust with specified configuration"""
    
    cmd = [
        "python", "-m", "locust",
        "-f", "locustfile.py",
        "--host", args.host
    ]
    
    if args.headless:
        cmd.append("--headless")
        cmd.extend(["-u", str(args.users)])
        cmd.extend(["-r", str(args.spawn_rate)])
        
        if args.run_time:
            cmd.extend(["-t", args.run_time])
    
    if args.html:
        cmd.extend(["--html", args.html])
    
    if args.csv:
        cmd.extend(["--csv", args.csv])
    
    print(f"\nRunning command: {' '.join(cmd)}\n")
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\nError running Locust: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description="Run Supplier Connect API Load Tests",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run with web UI
  python run_tests.py
  
  # Quick test (5 users, 1 minute)
  python run_tests.py --quick
  
  # Medium test (10 users, 5 minutes)
  python run_tests.py --medium
  
  # Stress test (20 users, 10 minutes)
  python run_tests.py --stress
  
  # Custom configuration
  python run_tests.py --headless -u 20 -r 5 -t 120s --html report.html
        """
    )
    
    parser.add_argument(
        "--host",
        default="http://52.220.47.3",
        help="API host URL (default: http://52.220.47.3)"
    )
    
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run in headless mode (no web UI)"
    )
    
    parser.add_argument(
        "-u", "--users",
        type=int,
        default=10,
        help="Number of users to simulate (default: 10)"
    )
    
    parser.add_argument(
        "-r", "--spawn-rate",
        type=int,
        default=2,
        help="User spawn rate per second (default: 2)"
    )
    
    parser.add_argument(
        "-t", "--run-time",
        help="Test duration (e.g., 60s, 5m, 1h)"
    )
    
    parser.add_argument(
        "--html",
        help="Generate HTML report (e.g., report.html)"
    )
    
    parser.add_argument(
        "--csv",
        help="Generate CSV results (e.g., results)"
    )
    
    # Preset configurations
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Quick test: 5 users, 5/s spawn rate, 15 seconds"
    )
    
    parser.add_argument(
        "--medium",
        action="store_true",
        help="Medium test: 10 users, 10/s spawn rate, 30 seconds"
    )
    
    parser.add_argument(
        "--stress",
        action="store_true",
        help="Stress test: 15 users, 15/s spawn rate, 45 seconds"
    )
    
    args = parser.parse_args()
    
    # Check dependencies first
    if not check_dependencies():
        sys.exit(1)
    
    # Apply preset configurations
    if args.quick:
        args.headless = True
        args.users = 5
        args.spawn_rate = 5
        args.run_time = "15s"
        args.html = "quick_test_report.html"
        args.csv = "quick_test_results"
    
    elif args.medium:
        args.headless = True
        args.users = 10
        args.spawn_rate = 10
        args.run_time = "30s"
        args.html = "medium_test_report.html"
        args.csv = "medium_test_results"
    
    elif args.stress:
        args.headless = True
        args.users = 15
        args.spawn_rate = 15
        args.run_time = "45s"
        args.html = "stress_test_report.html"
        args.csv = "stress_test_results"
    
    # Run the tests
    run_locust(args)


if __name__ == "__main__":
    main()
