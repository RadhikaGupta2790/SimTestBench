# simulation_engine.py

import logging
import time
from typing import Any, Dict
from utils import setup_logging, load_config

class SimulationEngine:
    def __init__(self, config: Dict[str, Any]) -> None:
        """
        Initializes the SimulationEngine with the provided configuration.

        :param config: A dictionary containing the simulation configuration.
        """
        self.config = config
        self.logger = logging.getLogger(__name__)

    def run(self) -> None:
        """
        Runs the simulation based on the configuration and test cases.
        """
        self.logger.info("Starting simulation...")
        results = {}

        # Check if test cases are defined
        if 'test_cases' not in self.config or not self.config['test_cases']:
            self.logger.error("No test cases defined in the configuration.")
            return

        for test_case in self.config['test_cases']:
            # Ensure each test case has a 'type' defined
            if 'type' not in test_case:
                self.logger.error(f"Test case '{test_case['name']}' is missing a 'type'. Skipping.")
                continue

            self.logger.info(f"Running test case: {test_case['name']} of type: {test_case['type']}")
            result = self.execute_test_case(test_case)
            results[test_case['name']] = result
        
        # Output the results of the simulation
        for name, result in results.items():
            self.logger.info(f"Test case '{name}' result: {result}")

    def execute_test_case(self, test_case: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulates the execution of a test case.

        :param test_case: The test case to execute.
        :return: A simulated result of the test case execution.
        """
        self.logger.info(f"Executing test case: {test_case['name']} with parameters: {test_case['parameters']}")
        
        if test_case['type'] == 'gpio':
            self.run_gpio_test(test_case)
        elif test_case['type'] == 'uart':
            self.run_uart_test(test_case)

        return {
            "status": "success",
            "parameters": test_case['parameters']
        }

    def run_gpio_test(self, test_case: Dict[str, Any]) -> None:
        gpio_pin = test_case['parameters']['gpio_pin']
        state = test_case['parameters']['state']
        duration = test_case['parameters']['duration']
        self.logger.info(f"GPIO Test on pin {gpio_pin}: Setting state to {state} for {duration} seconds")
        time.sleep(duration)
        self.logger.info(f"GPIO Test completed on pin {gpio_pin}: Final state {state}")

    def run_uart_test(self, test_case: Dict[str, Any]) -> None:
        port = test_case['parameters']['port']
        baud_rate = test_case['parameters']['baud_rate']
        message = test_case['parameters']['message']
        self.logger.info(f"UART Test on port {port} with baud rate {baud_rate}: Sending message '{message}'")
        time.sleep(2)
        self.logger.info(f"UART Test completed on port {port}: Sent message '{message}'")


# Load the configuration
if __name__ == "__main__":
    # Setup logging
    setup_logging('config/logging_config.json')  # Ensure this path is correct

    # Load the configuration from a YAML file
    try:
        config = load_config('config/config.yaml')  # Ensure this path is correct
        print("Configuration loaded successfully.")  # Debugging statement
    except Exception as e:
        print(f"Error loading configuration: {e}")
        exit(1)  # Exit if configuration loading fails

    # Run the simulation
    simulation = SimulationEngine(config)
    try:
        simulation.run()
    except Exception as e:
        print(f"An error occurred during simulation: {e}")