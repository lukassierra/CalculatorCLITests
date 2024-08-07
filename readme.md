# LoanPro Calculator CLI Automated Tests

## Description
This project contains automated test cases and their documentation for the LoanPro Calculator CLI using Python. The tests cover basic arithmetic operations, edge cases, and error handling.

## Prerequisites
- Docker installed on your macOS environment.
- Python 3.x installed.

## Setup and Execution
1. Pull the Docker image for the calculator CLI:
    ```
    docker pull public.ecr.aws/l4q9w4c5/loanpro-calculator-cli:latest
    ```

2. Navigate to the folder containing the `automated_tests.py` script.

3. Run the script using Python:
    ```
    python3 automated_tests.py
    ```

## Test Results
- The script will output `[PASS]` if a test case is successful, or `[FAIL]` if it fails, along with the test case description.
- Review the output in the terminal to identify any failed test cases.
