class MainTest:
    """Main class for all TCs"""

    def execute_test(self):
        print("Test execution from MainTest")

    def setup(self):
        print("Environment set up from MainTest")


class Logger:
    """Logger class for adding logging capabilities"""

    def execute_test(self):
        print("Logging start: Running test from Logger")
        super().execute_test()

    def log(self, message):
        print(f"Log: {message}")


class UserTest(MainTest, Logger):
    """User test class that inherits from BaseTest and Logger"""

    def execute_test(self):
        print("User execution logic from CustomTest")
        super().execute_test()

    def setup(self):
        print("Environment set up from CustomTest")
        super().setup()


"""An object creation and calling methods"""
test = UserTest()
print("MRO (Method Resolution Order):")
print(UserTest.mro())  # Display the MRO

print("\nRunning execute_test():")
test.execute_test()

print("\nRunning setup():")
test.setup()

print("\nUsing log() method:")
test.log("Test started")
