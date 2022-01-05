from selenium.webdriver.common.by import By


class JobPage:
    """
    Job Related Locators
    """
    general_description = (By.XPATH, "//div//h2[contains(., 'General description')]")
    requirements_description = (By.XPATH, "//div//h2[contains(., 'Requirements')]")
    responsibilities_description = (By.XPATH, "//div//h2[contains(., 'Responsibilities')]")
    offer_description = (By.XPATH, "//div//h2[contains(., 'What we offer')]")
    apply_btn = (By.XPATH, "//input[@class='wpcf7-form-control wpcf7-submit btn-join-us btn-apply']")
    # Form Locators
    name = (By.ID, 'cf-1')
    email = (By.ID, 'cf-2')
    mobile = (By.ID, 'cf-3')
    upload_cv = (By.ID, 'uploadtextfield')
    linkedin_link = (By.ID, 'cf-5')
    message = (By.ID, 'cf-6')
    submit = (By.XPATH, "//input[@class='wpcf7-form-control has-spinner wpcf7-submit btn-cf-submit']")
    name_validation_message = (By.XPATH, "//span[@class='wpcf7-form-control-wrap your-name']//span[contains(., "
                                         "'The field is required')]")
    email_validation_message = (By.XPATH, "//span//span[contains(., 'The e-mail address entered')]")

    def __init__(self, browser):
        self.browser = browser

    def get_general_description_title(self):
        title = self.browser.find_element(*self.general_description).text
        return title

    def get_requirements_title(self):
        title = self.browser.find_element(*self.requirements_description).text
        return title

    def get_responsibilities_title(self):
        title = self.browser.find_element(*self.responsibilities_description).text
        return title

    def get_offer_title(self):
        title = self.browser.find_element(*self.offer_description).text
        return title

    def check_apply_btn(self):
        return self.browser.find_element(*self.apply_btn).is_enabled()

    def apply_the_job(self):
        self.browser.find_element(*self.apply_btn).click()

    def fill_the_form_with_invalid_email(self, name, email, mobile, upload_cv, linkedin_link, message):
        self.browser.find_element(*self.name).send_keys(name)
        self.browser.find_element(*self.email).send_keys(email)
        self.browser.find_element(*self.mobile).send_keys(mobile)
        self.browser.find_element(*self.upload_cv).send_keys(upload_cv)
        self.browser.find_element(*self.linkedin_link).send_keys(linkedin_link)
        self.browser.find_element(*self.message).send_keys(message)
        self.browser.find_element(*self.submit).click()

    def get_email_validation_message(self):
        message = self.browser.find_element(*self.email_validation_message).text
        return message

    def get_name_validation_message(self):
        message = self.browser.find_element(*self.name_validation_message).text
        return message
