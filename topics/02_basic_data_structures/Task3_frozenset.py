"""Initial steps/scenarios
"""

steps_1 = ["open browser", "navigate to page", "click login"]
steps_2 = ["open browser", "navigate to page", "fill form"]
steps_3 = ["open browser", "navigate to page", "click login"]  # Duplicate of steps_1

"""Convert each scenario's steps to frozensets
"""

scenario_1 = frozenset(steps_1)
scenario_2 = frozenset(steps_2)
scenario_3 = frozenset(steps_3)

"""Dictionary of scenarios with frozensets
"""

dic_scenarios = {
    "Test Case 1": scenario_1,
    "Test Case 2": scenario_2,
    "Test Case 3": scenario_3
}

"""Function to check if a new test scenario already exists
"""

def check_scenario(test_name, new_steps, existing_scenarios):
    if test_name in existing_scenarios.keys():
        print(f"Test case name: {test_name} already exists in the dictionary.")
    elif test_name not in existing_scenarios.keys():
        print(f"Test case name: {test_name} does not exist in the dictionary")
        if new_steps in existing_scenarios.values():
            print(f"Duplicate steps detected: Matches {new_steps}.")
        else:
            steps_to_add = frozenset(new_steps)
            existing_scenarios.__setitem__(test_name, steps_to_add)
            print(f"Test scenario: {test_name} added to the dictionary.")

"""
Example usage
"""
new_steps = ["open browser", "navigate to page", "click login"]  # Same steps as Test Case 1
check_scenario("Test Case 5", new_steps, dic_scenarios) # Output: Should indicate that it matches Test Case 1