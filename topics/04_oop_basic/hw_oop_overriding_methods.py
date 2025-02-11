class MainTest:
    """Main class for all tests"""

    def execute_test(self):
        """Executing main test"""
        print("Executing main test with main parameters")
        self.setup()
        print("Running main test logic...")
        self.teardown()

    def setup(self):
        print("Setting up the test for main env")

    def teardown(self):
        print("Cleaning up the test for main env")


"""Child class overrides the main test  logic"""
class CustomTest(MainTest):
    def setup(self):
        """Custom setup logic."""
        print("Custom setup: Setting up specific test data and configuration.")

    def execute_test(self):
        """Overridden test execution logic."""
        print("Executing additional custom test")
        self.setup()
        print("Running custom test logic...")
        self.teardown()


"""Initialize objects and run tests"""
print("Running MainTest:")
main_test = MainTest()
main_test.execute_test()

print("\nRunning AdditionalTest:")
additional_test = CustomTest()
additional_test.execute_test()
