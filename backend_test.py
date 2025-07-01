#!/usr/bin/env python3
import requests
import json
import sys
from datetime import datetime

class CodeFuserAPITester:
    def __init__(self, base_url="http://localhost:8001"):
        self.base_url = base_url
        self.token = None
        self.tests_run = 0
        self.tests_passed = 0
        self.test_user = {
            "email": "test@example.com",
            "password": "test123"
        }

    def run_test(self, name, method, endpoint, expected_status, data=None, auth=False):
        """Run a single API test"""
        url = f"{self.base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}
        if auth and self.token:
            headers['Authorization'] = f'Bearer {self.token}'

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    return success, response.json()
                except:
                    return success, {}
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                try:
                    print(f"Response: {response.json()}")
                except:
                    print(f"Response: {response.text}")
                return False, {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            return False, {}

    def test_root(self):
        """Test the root endpoint"""
        return self.run_test("Root endpoint", "GET", "", 200)

    def test_login(self):
        """Test login with test user"""
        success, response = self.run_test(
            "Login with test user",
            "POST",
            "api/auth/login",
            200,
            data=self.test_user
        )
        if success and 'access_token' in response:
            self.token = response['access_token']
            print(f"Token obtained: {self.token[:10]}...")
            return True
        return False

    def test_signup(self):
        """Test signup with a new user"""
        # Generate a unique email
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        new_user = {
            "name": f"Test User {timestamp}",
            "email": f"test{timestamp}@example.com",
            "password": "testpass123"
        }
        
        success, response = self.run_test(
            "Signup with new user",
            "POST",
            "api/auth/signup",
            200,
            data=new_user
        )
        return success

    def test_me(self):
        """Test the /me endpoint with authentication"""
        if not self.token:
            print("❌ No token available for /me test")
            return False
            
        success, response = self.run_test(
            "Get current user info",
            "GET",
            "api/auth/me",
            200,
            auth=True
        )
        if success:
            print(f"User info: {response}")
        return success

    def test_templates(self):
        """Test getting templates"""
        success, response = self.run_test(
            "Get templates",
            "GET",
            "api/templates",
            200
        )
        if success:
            print(f"Templates available: {len(response.get('templates', {}))}")
        return success

    def test_stats(self):
        """Test getting stats"""
        success, response = self.run_test(
            "Get stats",
            "GET",
            "api/stats",
            200
        )
        if success:
            print(f"Stats: {response}")
        return success

    def test_queries(self):
        """Test getting user queries"""
        if not self.token:
            print("❌ No token available for queries test")
            return False
            
        success, response = self.run_test(
            "Get user queries",
            "GET",
            "api/queries",
            200,
            auth=True
        )
        if success:
            print(f"Queries count: {len(response.get('queries', []))}")
        return success

    def test_process_guest(self):
        """Test processing files as guest"""
        test_data = {
            "files": [
                {
                    "name": "test.py",
                    "content": "print('Hello, world!')",
                    "size": 23
                }
            ],
            "general_prompt": "Explain this code",
            "output_format": "html"
        }
        
        success, response = self.run_test(
            "Process files as guest",
            "POST",
            "api/process/guest",
            200,
            data=test_data
        )
        if success:
            print(f"Process result: {response.get('query_id', 'No ID')}")
        return success

    def test_process_authenticated(self):
        """Test processing files as authenticated user"""
        if not self.token:
            print("❌ No token available for authenticated process test")
            return False
            
        test_data = {
            "files": [
                {
                    "name": "test.py",
                    "content": "print('Hello, world!')",
                    "size": 23
                }
            ],
            "general_prompt": "Explain this code",
            "output_format": "html"
        }
        
        success, response = self.run_test(
            "Process files as authenticated user",
            "POST",
            "api/process",
            200,
            data=test_data,
            auth=True
        )
        if success:
            print(f"Process result: {response.get('query_id', 'No ID')}")
        return success

    def run_all_tests(self):
        """Run all tests"""
        print("🚀 Starting CodeFuser API Tests")
        print(f"Base URL: {self.base_url}")
        print("=" * 50)
        
        # Basic endpoints
        self.test_root()
        self.test_templates()
        self.test_stats()
        
        # Guest processing
        self.test_process_guest()
        
        # Authentication flow
        login_success = self.test_login()
        if login_success:
            self.test_me()
            self.test_queries()
            self.test_process_authenticated()
        else:
            # Try signup if login fails
            signup_success = self.test_signup()
            if signup_success:
                self.test_login()  # Login with the new user
                self.test_me()
                self.test_queries()
                self.test_process_authenticated()
        
        # Print results
        print("\n" + "=" * 50)
        print(f"📊 Tests passed: {self.tests_passed}/{self.tests_run}")
        print("=" * 50)
        
        return self.tests_passed == self.tests_run

if __name__ == "__main__":
    # Get base URL from environment or use default
    import os
    base_url = os.environ.get("REACT_APP_BACKEND_URL", "http://localhost:8001")
    
    tester = CodeFuserAPITester(base_url)
    success = tester.run_all_tests()
    
    sys.exit(0 if success else 1)