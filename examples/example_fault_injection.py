# example_fault_injection.py

import logging
from SimTestBench.core.fault_injection import FaultInjection

def main():
    # Setup logging
    logging.basicConfig(level=logging.INFO)

    # Define fault configuration
    fault_config = {
        'enabled': True,
        'types': ['packet_loss', 'bit_flip']
    }

    # Create an instance of FaultInjection
    fault_injection = FaultInjection(fault_config)

    # Define a test case
    test_case = {
        'name': 'Test Case 1',
        'parameters': {
            'param1': 1,
            'param2': 2
        }
    }

    # Log the original test case
    logging.info(f"Original Test Case: {test_case}")

    # Inject faults into the test case
    modified_test_case = fault_injection.inject_faults(test_case)

    # Log the modified test case
    logging.info(f"Modified Test Case: {modified_test_case}")

    # Output the modified test case
    print("Modified Test Case:", modified_test_case)

if __name__ == "__main__":
    main()