# Automation Service Store

Automation framework for testing **Omnify Service Store** using **Python**, **Selenium**, and **Pytest**.  
Implements Page Object Model (POM), supports data-driven and parallel testing, and generates HTML reports for better visibility.  
Fully configurable for multiple environments (test, staging, production).

---

## 🚀 Features

- 🔹 UI automation using Selenium WebDriver  
- 🔹 Test execution with Pytest  
- 🔹 Shell scripts for setup and test execution
- 🔹 Environment-based configuration via `.env`  
- 🔹 Page Object Model (POM) design pattern    
- 🔹 Parallel test execution with `pytest-xdist`  

---

## 🔰 Tech Stack & Badges

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pytest](https://img.shields.io/badge/Pytest-Framework-green?logo=pytest)
![Selenium](https://img.shields.io/badge/Selenium-WebAutomation-brightgreen?logo=selenium)
![API Testing](https://img.shields.io/badge/API-Testing-yellow)
![Allure Report](https://img.shields.io/badge/Allure-Report-ff69b4?logo=allure)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-blue?logo=githubactions)


## 🗂 Project Structure

automation-service-store/

├── pages/ # Page Object classes (LoginPage, DashboardPage, etc.) </br>
├── shellFiles/ # Shell scripts (setup, env selection, execution) </br>
├── tests/ # Test cases </br>
├── data_json.sample # Sample data file </br>
├── env.sample # Sample environment config </br>
├── requirements.txt # Dependencies </br>
├── .gitignore # Ignored files list </br>
└── README.md # Project documentation </br>


---

## ⚙️ Setup and Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/PrasadHelaskar/automation-service-store.git

   cd automation-service-store

   python3 -m venv venv

   source venv/bin/activate   # For Linux/Mac
    
   venv\Scripts\activate      # For Windows
    
   pip install -r requirements.txt
    
    ```
## ▶️ Running Tests
Run all tests
```
 pytest
```
Run tests in parallel eg: 4
```
 pytest -n 4 
``` 
Run with HTML report
```
 pytest --html=reports/report.html --self-contained-html 
```

## 🐚 Shell File Usage

    The project includes helper shell scripts under the shellFiles/ directory to simplify environment setup and test execution.
    These scripts automate selecting environments, exporting variables, and triggering Pytest runs.

1️⃣ env_selector.sh

    Used to choose the environment configuration file (test.env, staging.env, or prod.env) and export its variables.

    Usage:

    source shellFiles/env_selector.sh
    select_env

    or directly:

    source shellFiles/env_selector.sh test

    This loads environment variables into the current shell session based on your choice.

2️⃣ PytestRunner.sh


    Main runner script that uses the environment setup and triggers the required test suite.

    Usage:

    bash shellFiles/PytestRunner.sh


    Menu Options:

    For Selenium UI Tests

    The script:

    Calls env_selector.sh internally to set the correct environment.

    Loads .env variables for the test.

    Executes pytest commands for the selected type of test.

    Can be extended to include Allure or HTML report generation.

## ⚙️ Configuration Example

``BASE_URL``=https://service-store.example.com </br>
``USERNAME``=test_user  </br>
``PASSWORD``=test_password  </br>
``ENVIRONMENT``=staging  </br>



## 🧱 Page Object Model (POM)

    Each web page is represented by a Page Object class inside the pages/ directory.
    These classes contain locators and reusable methods for UI actions.

    Example:

    LoginPage — handles login flow and validations

    DashboardPage — handles service creation, update, and delete

    ServiceStorePage — handles navigation and bookings actions

    This improves test readability and reduces duplication.

## 🧪 Test Structure

    All tests are placed under the tests/ directory.
    Each test file targets a specific functionality, e.g.:

    tests/test_login.py — verifies login scenarios

    tests/test_service_crud.py — verifies create/update/delete services

    Common features:

    Reusable fixtures for browser setup

    Assertions for validation

    Screenshot capture on failure

## 👨‍💻 Author

**Prasad Helaskar**  
Automation Engineer | QA | Python + Selenium + Pytest  
🔗 [GitHub Profile](https://github.com/PrasadHelaskar)

