class TestCase:
    def __init__(self, name):
        self.name = name

    def setup(self):
        """Setup method: Initialize resources or prepare test environment."""
        print(f"Setting up for test case: {self.name}")

    def run(self):
        """Run method: Execute the actual test logic."""
        print(f"Running test case: {self.name}")

    def teardown(self):
        """Teardown method: Clean up resources or reset environment."""
        print(f"Tearing down for test case: {self.name}")

# Creating individual test cases
test_case_1 = TestCase("TestCase1")
test_case_2 = TestCase("TestCase2")

# Executing test case 1
print("Executing Test Case 1")
test_case_1.setup()
test_case_1.run()
test_case_1.teardown()

print("\nExecuting Test Case 2")
# Executing test case 2
test_case_2.setup()
test_case_2.run()
test_case_2.teardown()
