# SimTestBench

**SimTestBench** is a Python-based framework for simulation and testing, designed to validate hardware components, embedded systems, and software modules. The project supports simulation of real-world scenarios, fault injection, and automated test execution, making it ideal for validation engineers, software developers, and DFX engineers.

---

## **Features**

- **Simulation Engine**: Simulates hardware and software interactions, including GPIO, UART, and interrupts.
- **Fault Injection**: Introduces faults for testing system robustness and fault recovery mechanisms.
- **Testing Framework**: Supports automated test execution with detailed reporting.
- **Extensibility**: Add custom simulators, plugins, and test cases.
- **Reports and Logging**: Generates comprehensive reports and logs for debugging and analysis.

---

## **Project Architecture**

Below is a high-level diagram of the SimTestBench architecture:
```

                      +-----------------------+
                      |      User Scripts     |
                      +-----------------------+
                                |
                                v
+------------------+      +-----------+      +------------------+
| Simulation Engine|<---->| Extensions|<---->| Custom Simulators|
+------------------+      +-----------+      +------------------+
                                |
                                v
     +---------------------------------------------------+
     |              Core Modules (Sim/Test)              |
     |   Simulation | Fault Injection | UART | Interrupt |
     +---------------------------------------------------+
                                |
                                v
       +-----------------------------------------------+
       |           Configuration & Logging             |
       +-----------------------------------------------+
                                |
                                v
                +---------------------------+
                |        Reports & Logs     |
                +---------------------------+
```


## Installation

### Prerequisites
- Python >= 3.8
- Pip (Python package manager)

### Steps

1. Clone the repository:
    ```bash
    git clone <repository-url> SimTestBench
    cd SimTestBench
    ```

2. Install dependencies:
    ```bash
    python setup/manage_dependencies.py
    ```

3. Verify installation:
    ```bash
    pytest
    ```

## Usage

### Running a Simulation
1. Configure the simulation parameters in `config/config.yaml`.
2. Run an example simulation:
    ```bash
    python examples/example_simulation.py
    ```

### Adding Custom Tests
1. Create a test script in `extensions/custom_tests/`.
2. Define the test logic and integrate it with the framework.
3. Run the new test:
    ```bash
    python core/test_runner.py --test extensions/custom_tests/your_test.py
    ```

### Running Automated Tests
To run all available tests in the framework:
```bash
pytest
```


## Directory Structure

Here’s an overview of the project directory structure:

```
SimTestBench/
├── assets/                     # Static data and example files
│   ├── sample_data/            # Sample test/simulation data
│   │   ├── gpio_test_data.csv
│   │   └── uart_sample_data.txt
│   └── example_configs/        # Example configuration files
│       └── default_config.yaml
├── config/                     # Configuration files
│   ├── config.yaml             # Main project configuration
│   ├── logging_config.json     # Logging setup
│   └── hardware_profiles.yaml  # Hardware profiles and definitions
├── core/                       # Core logic for simulations and testing
│   ├── simulation_engine.py    # Simulation engine
│   ├── test_runner.py          # Core test execution logic
│   ├── fault_injection.py      # Fault injection utilities
│   ├── report_generator.py     # Report generation
│   ├── interrupt_manager.py    # Interrupt handling and management
│   ├── uart_communication.py   # UART communication handling
│   └── utils.py                # Common utilities
├── extensions/                 # Extensions and plugins
│   ├── custom_tests/           # User-defined test cases
│   ├── simulators/             # Custom simulation modules
│   └── plugins/                # Additional plugin modules
├── docs/                       # Documentation for the project
│   ├── architecture.md         # High-level architecture overview
│   ├── usage.md                # How to use the framework
│   └── contributions.md        # Guidelines for contributing
├── examples/                   # Example test cases and simulations
│   ├── example_test_case.py
│   └── example_simulation.py
├── tests/                      # Unit and integration tests
│   ├── test_simulation.py      # Test cases for simulation engine
│   ├── test_runner.py          # Test cases for test runner logic
│   ├── test_fault_injection.py # Test cases for fault injection
│   ├── test_interrupts.py      # Test cases for interrupts
│   ├── test_uart.py            # Test cases for UART communication
│   └── conftest.py             # Configuration file for pytest
├── logs/                       # Logs generated by the framework
│   └── .gitkeep                # Placeholder for an empty directory
├── setup/                      # Setup and installation utilities
│   ├── setup.py                # Installation script
│   ├── requirements.txt        # Dependencies
│   ├── manage_dependencies.py  # Dependency management script
│   └── README.md               # Setup-specific documentation
├── tools/                      # Utility scripts for maintenance
│   ├── update_dependencies.py  # Script to update dependencies
│   └── debug_tool.py           # Debugging tool for the project
├── README.md                   # Project overview
└── pytest.ini                  # Pytest configuration

```



## Contributing

We welcome contributions to the project! If you wish to contribute, please follow these steps:

1. Fork the repository and create a new branch (git checkout -b branch_name).
2. Make your changes and ensure they are properly tested (use pytest).
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **SimTestBench** is inspired by the need for a flexible and extensible simulation and testing framework for embedded systems.
- Thanks to the open-source community for contributing to this project and making it a collaborative effort.
