from selenium.webdriver.common.by import By


class CareersPage:
    """
    Careers Page Related Locators
    """
    career_btn = (By.XPATH, "//button[@class='contact-label contact-label-code btn btn-1b']")

    def __init__(self, browser):
        self.browser = browser

    def navigate_to_join_us(self):
        self.browser.find_element(*self.career_btn).click()

    def get_current_url(self):
        return self.browser.current_url
