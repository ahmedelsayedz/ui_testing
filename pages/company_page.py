from selenium.webdriver.common.by import By


class CompanyPage:
    """
    Company Page Related Locators
    """
    leadership = (By.XPATH, "//div[@class='cm-content']//h2")
    facebook = (By.XPATH, "//a//span[@class='musala musala-icon-facebook']")

    def __init__(self, browser):
        self.browser = browser

    def get_company_url(self):
        return self.browser.current_url

    def verify_leadership_section(self):
        title = self.browser.find_element(*self.leadership).text
        return title

    def verify_facebook_link(self):
        self.browser.find_element(*self.facebook).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        return self.browser.current_url

    def return_to_first_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[0])
        return self.browser.current_url
