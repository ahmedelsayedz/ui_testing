"""
This module contains shared fixtures.
"""

import json
import pytest
import selenium.webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def config(scope='session'):
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        driver = selenium.webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
    elif config['browser'] == 'Chrome':
        s = Service(ChromeDriverManager().install())
        driver = selenium.webdriver.Chrome(service=s)
        driver.maximize_window()
    elif config['browser'] == 'Headless Chrome':
        options = selenium.webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = selenium.webdriver.Chrome(ChromeDriverManager().install(), options=options)

    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    driver.get(config['url'])
    # Make its calls wait for elements to appear
    driver.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield driver

    # Quit the WebDriver instance for the cleanup
    driver.quit()
