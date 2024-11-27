import random
import logging

class FaultInjection:
    def __init__(self, fault_config):
        """
        Initializes the FaultInjection with the given configuration.
        
        :param fault_config: A dictionary containing fault injection settings.
        """
        self.enabled = fault_config.get('enabled', False)
        self.fault_types = fault_config.get('types', [])
        self.logger = logging.getLogger(__name__)

    def inject_faults(self, test_case: dict) -> dict:        
        """
        This method will inject faults into the test case if fault injection is enabled.

        :param test_case: A dictionary containing the test case details.
        :return: A modified test case with injected faults or the original test case if no faults are injected.
        """
        if not self.enabled:
            return test_case  # No fault injection if not enabled

        if not isinstance(test_case, dict):
            self.logger.warning("Invalid test_case format. Expected a dictionary.")
            return test_case  # Return the original test_case if it's not a dictionary

        if not self.fault_types:
            self.logger.info("No fault types configured.")
            return test_case  # No fault types to inject

        fault_type = random.choice(self.fault_types)

        self.logger.info(f"Injecting fault type: {fault_type}")

        if fault_type == "packet_loss":
            return self._inject_packet_loss(test_case)
        elif fault_type == "bit_flip":
            return self._inject_bit_flip(test_case)
        else:
            self.logger.info("No fault injected.")
            return test_case

    def _inject_packet_loss(self, test_case):
        """
        Simulates packet loss by randomly removing parts of the test case data.
        
        :param test_case: The test case to modify.
        :return: The test case with packet loss injected.
        """
        self.logger.info(f"Simulating packet loss for test case: {test_case['name']}")
        
        # Remove random keys from the test case to simulate packet loss
        if 'parameters' in test_case:
            param_keys = list(test_case['parameters'].keys())
            if param_keys:  # Check if there are parameters to remove
                lost_key = random.choice(param_keys)
                test_case['parameters'].pop(lost_key, None)
                self.logger.info(f"Simulated packet loss: Removed {lost_key} from parameters.")

        return test_case

    def _inject_bit_flip(self, test_case):
        """
        Simulates a bit flip by randomly flipping a bit in the test case's data.
        
        :param test_case: The test case to modify.
        :return: The test case with a simulated bit flip.
        """
        self.logger.info(f"Simulating bit flip for test case: {test_case['name']}")

        if 'parameters' in test_case:
            param_keys = list(test_case['parameters'].keys())
            if param_keys:  # Check if there are parameters to modify
                random_param = random.choice(param_keys)
                if isinstance(test_case['parameters'][random_param], int):
                    original_value = test_case['parameters'][random_param]
                    flipped_value = original_value ^ 1  # Flip the least significant bit
                    test_case['parameters'][random_param] = flipped_value
                    self.logger.info(f"Simulated bit flip: Flipped bit for {random_param}, from {original_value} to {flipped_value}.")
        
        return test_case

    def add_custom_fault(self, fault_name, handler):
        """
        Register a custom fault handler.

        :param fault_name: The name of the custom fault.
        :param handler: The function that handles the custom fault.
        """
        self.fault_types.append(fault_name)
        # You can also store the handler if needed for custom logic in the future