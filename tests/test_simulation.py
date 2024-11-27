import unittest
from unittest.mock import patch
from core.fault_injection import FaultInjection
from core.simulation_engine import SimulationEngine
from core.utils import load_config

class TestSimulationEngine(unittest.TestCase):
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

    def test_edge_case_invalid_config(self):
        """Test if invalid config file is handled properly."""
        with patch('builtins.open', side_effect=FileNotFoundError):
            with self.assertRaises(TypeError):
                load_config('invalid_path.json')

    def test_edge_case_missing_test_case(self):
        """Test if missing or invalid test case handles properly."""
        self.config['test_cases'] = []
        with self.assertRaises(ValueError):
            self.simulation_engine.run()

    def test_fault_injection_bit_flip(self):
        """Test fault injection for bit flip."""
        test_case = self.config['test_cases'][0]
        result = self.simulation_engine.fault_injection.inject_faults(test_case)
        
        # Check if bit flip was injected
        self.assertEqual(result, "Bit flip injected")

    def test_fault_injection_packet_loss(self):
        """Test fault injection for packet loss."""
        test_case = self.config['test_cases'][0]
        result = self.simulation_engine.fault_injection.inject_faults(test_case)
        
        # Check if packet loss was injected
        self.assertEqual(result, "Packet loss injected")

    def test_invalid_fault_type(self):
        """Test handling of an invalid fault type."""
        self.simulation_engine.fault_injection.fault_types = ['valid_fault']
        result = self.simulation_engine.fault_injection.inject_faults('invalid_fault')
        
        # Check if the invalid fault type is handled gracefully
        self.assertEqual(result, "Invalid fault type")

    def test_load_config(self):
        """Test if the configuration file is loaded properly."""
        config = load_config('valid_config.json')  # Ensure this file exists with correct structure
        self.assertEqual(config['simulation']['name'], 'Basic Simulation')

    def test_run_simulation(self):
        """Test the simulation engine's ability to run the simulation."""
        results = self.simulation_engine.run()
        
        # Check if the simulation results are generated
        self.assertIsInstance(results, dict)

if __name__ == '__main__':
    unittest.main()