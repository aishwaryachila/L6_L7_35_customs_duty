# Lab 6 – Customs Duty Calculator

## Project Overview
This project implements a Customs Duty Calculator in Python. It calculates customs duty based on product categories, declared values, trade agreements, and other applicable conditions. Automated tests are used to verify the correctness of the calculations and clearance decisions.

## Objectives
- Implement customs duty calculation logic.
- Test different product categories and duty rates.
- Validate prohibited goods and negative values.
- Test clearance conditions and documentation requirements.
- Measure code coverage using Python testing tools.

## Technologies Used
- **Python 3**
- **pytest** – Automated testing
- **Coverage.py** – Code coverage measurement

## Project Structure

```text
L6_L7_35_customs_duty-main/
├── customs_duty.py
├── test_customs_duty.py
├── CodeCoverageTest_039_application.py
├── coverage_report.txt
├── 01_pytest_results_21_passed.png
├── 02_coverage_report_97_percent.png
├── README.md
└── lab6/
    ├── customs_duty.py
    ├── test_customs_duty.py
    └── README.md
```

## Features
- Calculates customs duty for different product categories.
- Supports different duty rates based on trade agreements.
- Handles prohibited goods such as weapons and narcotics.
- Checks negative values and applicable duty conditions.
- Evaluates clearance conditions and required documentation.
- Includes automated tests for different scenarios.

## How to Run the Project

### 1. Open the project folder
Open the project folder in VS Code and open the terminal.

### 2. Run the automated tests

```bash
python -m pytest CodeCoverageTest_039_application.py -v
```

**Expected result:** 21 tests passed.

### 3. Run tests with coverage measurement

```bash
python -m coverage erase
python -m coverage run --source=customs_duty -m pytest CodeCoverageTest_039_application.py
```

### 4. Generate the coverage report

```bash
python -m coverage report -m
```

**Observed result:**
- Statements: 36
- Missed statements: 1
- Code coverage: 97%

## Test Results

All 21 automated tests passed successfully in the final test run.

The tests cover:
- Duty rate categories
- Prohibited duty rates
- Negative values
- Minimum and normal duty calculations
- Clearance restrictions
- High-value and low-value clearance
- Required documentation

## Screenshots

### 1. Pytest Results
The screenshot `01_pytest_results_21_passed.png` shows the successful execution of all 21 automated tests.

### 2. Code Coverage Report
The screenshot `02_coverage_report_97_percent.png` shows the coverage report with 97% code coverage.

## Conclusion

The Customs Duty Calculator was tested using pytest, and the final test run passed all 21 tests. Coverage.py reported 97% code coverage, indicating that most of the measured statements were executed during testing.
