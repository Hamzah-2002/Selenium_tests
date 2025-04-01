# Airbnb Search Automation Tests

This repository contains automated test cases for Airbnb's search functionality using Selenium WebDriver and Python. The tests are integrated with GitHub Actions for continuous integration and continuous deployment (CI/CD).

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── test.yml          # GitHub Actions workflow configuration
├── test_airbnb_search.py     # Main test file containing test cases
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Prerequisites

- Python 3.9 or higher
- Chrome browser
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Hamzah-2002/Selenium_tests.git
cd Selenium_tests
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests Locally

To run the tests locally:

```bash
pytest test_airbnb_search.py --html=report.html
```

This will generate a detailed HTML report in the `report.html` file.

## Test Cases

The test suite includes the following test cases:

1. **Basic Search Test**
   - Opens Airbnb website
   - Verifies homepage loading
   - Performs location search
   - Selects dates
   - Modifies guest count
   - Executes search

2. **Search Results Validation**
   - Verifies search results page
   - Validates search parameters
   - Checks result count

3. **Filter Tests**
   - Price range filtering
   - Property type filtering
   - Amenities filtering

## CI/CD Pipeline

The project uses GitHub Actions for continuous integration. The workflow:
1. Runs on push to main branch and pull requests
2. Sets up Python environment
3. Installs dependencies
4. Runs test suite
5. Generates and uploads test reports

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 