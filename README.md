# Airbnb UI Automation Tests

Automated UI testing of the Airbnb web application using Python, Selenium WebDriver, and pytest.

This project was developed as part of a university laboratory assignment on software testing and verification. It explores web UI automation, user interaction testing, boundary-value analysis, and validation of search functionality.

## Tech Stack

- **Python** — programming language
- **Selenium WebDriver** — browser automation
- **pytest** — test execution and test organization
- **Page Object Model (POM)** — separation of page interactions from test logic
- **Google Chrome** — browser used for testing

## Automated Test Cases

| Test ID | Scenario | Focus |
|---|---|---|
| TC_001 | Search functionality | Location search, date selection, guest selection |
| TC_002 | Dynamic price calculation | Booking widget and date selection |
| TC_011 | Switch to Experiences | Navigation between search modes |
| TC_013 | Location autocomplete | Search suggestions |
| TC_018 | Guest count manipulation via URL | Boundary-value and input validation testing |

## Project Structure

```text
airbnb-ui-automation/
├── tests/
│   ├── test_tc_001_search.py
│   ├── test_tc_002_pricing.py
│   ├── test_tc_011_experiences.py
│   ├── test_tc_013_autocomplete.py
│   └── test_tc_018_guest_validation.py
├── home_page.py
├── property_page.py
├── requirements.txt
├── .gitignore
└── README.md
```

*The structure above is a suggested layout. Adjust it to match the actual repository.*

## Getting Started

### Prerequisites

- Python 3.10 or later
- Google Chrome
- pip

### Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/airbnb-ui-automation.git
cd airbnb-ui-automation
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Tests

Run the complete test suite:

```bash
pytest -v
```

Run a specific test:

```bash
pytest -v tests/test_tc_013_autocomplete.py
```

## Testing Approach

The project applies several practical testing techniques:

- Functional UI testing
- Search and navigation testing
- Date-picker interaction
- Autocomplete verification
- Boundary-value and URL parameter testing
- Page Object Model for reusable page interactions

## Notes and Limitations

- Tests interact with the live Airbnb website, whose interface, selectors, and behavior may change.
- Some scenarios depend on dynamic content, availability, localization, and date selection.
- The URL manipulation test checks the rendered page for an invalid guest count; its result alone does not establish that backend validation is implemented correctly.
- Tests may require maintenance when the website changes.
- This is an educational project and is not affiliated with Airbnb.

## Author

Developed as a university laboratory project on software testing and verification.
