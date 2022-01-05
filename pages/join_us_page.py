from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class JoinUsPage:
    """
    Join Us Page Related Locators
    """
    all_location_ddn = (By.ID, 'get_location')
    career_location_list = (By.XPATH, "//p[@class='card-jobsHot__location']")
    to_get_card_title = "..//h2[@class='card-jobsHot__title']"

    def __init__(self, browser):
        self.browser = browser

    def select_location_from_ddl(self, location):
        self.browser.find_element(*self.all_location_ddn).click()
        sel = Select(self.browser.find_element(*self.all_location_ddn))
        sel.select_by_visible_text(location)

    def select_specific_title_from_list(self, specific_city):
        city_list = self.browser.find_elements(*self.career_location_list)
        for city in city_list:
            if city.text == specific_city:
                return city.find_element(By.XPATH, self.to_get_card_title).text

