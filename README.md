# Selenium Web Testing Project with CI/CD

This project demonstrates web application testing using Selenium with Python and includes CI/CD release management through GitHub Actions.

## Project Structure

```
.
├── tests/
│   ├── test_base.py      # Base test class with common setup/teardown
│   └── test_amazon.py    # Amazon website test cases
├── test_results/         # Test reports and screenshots
├── requirements.txt      # Project dependencies
├── pytest.ini           # Pytest configuration
└── .github/
    └── workflows/       # GitHub Actions workflows
```

## Features

- Automated web testing using Selenium
- Comprehensive test cases for Amazon website
- Detailed logging and reporting
- Screenshot capture for visual verification
- CI/CD pipeline with GitHub Actions
- Automated release management

## Prerequisites

- Python 3.11 or higher
- Chrome browser installed
- Git

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Hamzah-2002/Selenium_tests1.git
   cd Selenium_tests1
   ```

2. Create and activate virtual environment:
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

### Manual Execution

1. Run all tests:
   ```bash
   pytest
   ```

2. Run specific test file:
   ```bash
   pytest tests/test_amazon.py
   ```

3. Run specific test case:
   ```bash
   pytest tests/test_amazon.py::TestAmazon::test_search_product
   ```

4. Run with detailed logging:
   ```bash
   pytest --log-cli-level=DEBUG
   ```

### View Results

- HTML report: Open `test_results/report.html` in your browser
- Screenshots: Check the timestamped folders in `test_results/`
- Logs: View the console output or check the log files

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:
1. Runs tests on every push and pull request
2. Generates and uploads test reports as artifacts
3. Creates releases when tags are pushed

### Creating a Release

1. Create and push a new tag:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

2. The workflow will automatically create a release with the test results

## Test Cases

The project includes the following test cases for Amazon:
1. Homepage verification
2. Product search functionality
3. Add to cart functionality
4. Sign-in button verification
5. Department navigation

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Run tests locally
5. Create a pull request

## License

MIT License 