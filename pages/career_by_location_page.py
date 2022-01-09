from selenium.webdriver.common.by import By


class CareerLocationPage:
    """
    Career Location Related Locators
    """
    position_name = (By.XPATH, "//div//h2[contains(., 'Experienced Automation QA Engineer')]")

    def __init__(self, browser):
        self.browser = browser

    def choose_automation_position(self):
        self.browser.find_element(*self.position_name).click()
