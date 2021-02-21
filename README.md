### Test Automation Scenarios for Testing Parent.Land Website

This a project for web automation of Parent.Land 

Technology stack: [Python](https://www.python.org/), [Selenium](https://www.selenium.dev/), 
[Behave](https://pypi.org/project/behave/)


### Structure

```
Project Folder
├── features
│   ├── pages
│   │   ├── base_page.py    # base class - helper functions
│   │   ├── home.page.py    # homepage class with locators dictionary
│   ├── steps
│   │   ├── parentland.py   # Gherkin steps
│   ├── parentland.feature  # test scenarios
│   ├── environment.py      # browser settings 
├── test_data.py            # test data, usernames etc.
```

### Local env setup

Tu use this project Python 3.8. is required.

```bash
python3.8 -m venv venv
pip install -r requirements.txt
```

The convention for managing Python dependency is as follows:
- we add the dependency into requirements.in
- we call ```pip-compile``` to create requirements.txt
- we commit both files to repository.

To run tests locally Selenium Webdriver is required. 
In this project Selenium Webdriver is managed automatically by 
[Webdriver Manager](https://github.com/SergeyPirogov/webdriver_manager)
Be sure that you have updated version of [Chrome Browser](https://www.google.com/chrome/) on your device.

### How to run?

Just type in command line

```
behave
```
