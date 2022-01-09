from selenium.webdriver.common.by import By


class HomePage:
    """
    Home Page Related Locators
    """
    # Contact us link locator
    contact_us = (By.XPATH, "//button[@class='contact-label btn btn-1b']")

    # Contact us form locators
    name = (By.ID, 'cf-1')
    email = (By.ID, 'cf-2')
    email_validation_message = (By.XPATH, "//span[@class='wpcf7-form-control-wrap your-email']//span["
                                          "@class='wpcf7-not-valid-tip']")
    mobile = (By.ID, 'cf-3')
    subject = (By.ID, 'cf-4')
    message = (By.ID, 'cf-5')
    submit = (By.XPATH, "//input[@class='wpcf7-form-control has-spinner wpcf7-submit btn-cf-submit']")

    # Company link locator
    company = (By.XPATH, "//div//ul[@id='menu-main-nav-1']//a[contains(., 'Company')]")

    # Career link locator
    career = (By.XPATH, "//ul[@id='menu-main-nav-1']//a[@href='https://www.musala.com/careers/']")

    def __init__(self, browser):
        self.browser = browser

    def go_to_contact_us(self):
        self.browser.execute_script("window.scrollTo(0, 900)")
        self.browser.find_element(*self.contact_us).click()

    def fill_the_form(self, name, email, mobile, subject, message):
        self.browser.find_element(*self.name).clear()
        self.browser.find_element(*self.name).send_keys(name)

        self.browser.find_element(*self.email).clear()
        self.browser.find_element(*self.email).send_keys(email)

        self.browser.find_element(*self.mobile).clear()
        self.browser.find_element(*self.mobile).send_keys(mobile)

        self.browser.find_element(*self.subject).clear()
        self.browser.find_element(*self.subject).send_keys(subject)

        self.browser.find_element(*self.message).clear()
        self.browser.find_element(*self.message).send_keys(message)
        self.browser.find_element(*self.submit).click()

    def get_validation_message(self):
        message = self.browser.find_element(*self.email_validation_message).text
        return message

    def go_to_company(self):
        self.browser.find_element(*self.company).click()

    def navigate_to_career(self):
        self.browser.find_element(*self.career).click()
