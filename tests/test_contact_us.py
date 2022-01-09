import os

import pytest

from helper.common import load_json_file
from pages.career_by_location_page import CareerLocationPage
from pages.careers_page import CareersPage
from pages.company_page import CompanyPage
from pages.home_page import HomePage
from pages.job_page import JobPage
from pages.join_us_page import JoinUsPage


def test001_validation_message_in_contact_form(browser):
    """
    Visit http://www.musala.com/
    Scroll down and go to ‘Contact Us’
    Fill all required fields except email
    Under email field enter string with wrong email format (e.g. test@test)
    Click ‘Send’ button
    Verify that error message ‘The e-mail address entered is invalid.’ appears
    """
    file_path = "helper/form_data.json"
    list_data = load_json_file(file_path)["form"]

    home_page = HomePage(browser)
    home_page.go_to_contact_us()
    for i in range(5):
        home_page.fill_the_form("Ahmed Mahmoud", list_data[i]["email"], "01003936065", "Form Subject", "Form Message")
        assert home_page.get_validation_message() == "The e-mail address entered is invalid."


def test002_company_tap(browser):
    """
    Visit http://www.musala.com/
    Click ‘Company’ tap from the top
    Verify that the correct URL (http://www.musala.com/company/) loads
    Verify that there is ‘Leadership’ section
    Click the Facebook link from the footer
    Verify that the correct URL (https://www.facebook.com/MusalaSoft?fref=ts) loads
    verify if the Musala Soft profile picture appears on the new page
    """
    home_page = HomePage(browser)
    home_page.go_to_company()
    company_page = CompanyPage(browser)
    assert company_page.get_company_url() == "https://www.musala.com/company/"
    assert company_page.verify_leadership_section() == "Leadership"
    assert company_page.verify_facebook_link() == "https://www.facebook.com/MusalaSoft?fref=ts"
    assert company_page.return_to_first_tab() == "https://www.musala.com/company/"


FormData = [
    (1, "", "email", "01003936065", "linkedin_link", "message", "The e-mail address entered is invalid."),
    (0, "", "test@test", "", "", "", "The field is required."),

]


@pytest.mark.parametrize("number, name, email, mobile, linkedin_link, message, validation", FormData)
def test003_careers_menu(browser, number, name, email, mobile, linkedin_link, message, validation):
    """
    Visit http://www.musala.com/
    Navigate to Careers menu (from the top)
    Click ‘Check our open positions’ button
    Verify that ‘Join Us’ page is opened (can verify that URL is correct:
    http://www.musala.com/careers/join-us/
    From the dropdown ‘Select location’ select ‘Anywhere’
    Choose open position by name (e.g. Experienced Automation QA Engineer)
    Verify that 4 main sections are shown: General Description, Requirements, Responsibilities, What we offer
    Verify that ‘Apply’ button is present at the bottom
    Click ‘Apply’ button
    Prepare a few sets of negative data (e.g. leave required field(s) empty, enter e-mail with invalid format etc)
    Upload a CV document, and click ‘Send’ button
    Verify shown error messages (e.g. The field is required, The e-mail address entered is invalid etc.)
    """
    upload_cv_path = "/helper/Ahmed Mahmoud Resume.pdf"
    upload_cv = os.getcwd() + upload_cv_path

    home_page = HomePage(browser)
    home_page.navigate_to_career()

    career_page = CareersPage(browser)
    career_page.navigate_to_join_us()
    assert career_page.get_current_url() == "https://www.musala.com/careers/join-us/"

    join_us_page = JoinUsPage(browser)
    join_us_page.select_location_from_ddl("Anywhere")

    career_location_page = CareerLocationPage(browser)
    career_location_page.choose_automation_position()

    job_page = JobPage(browser)
    assert job_page.get_general_description_title() == "General description"
    assert job_page.get_requirements_title() == "Requirements"
    assert job_page.get_responsibilities_title() == "Responsibilities"
    assert job_page.get_offer_title() == "What we offer"
    assert job_page.check_apply_btn() == True
    job_page.apply_the_job()

    job_page.fill_the_form_with_invalid_email(name, email, mobile, upload_cv, linkedin_link, message)
    array = [job_page.get_name_validation_message(), job_page.get_email_validation_message()]
    assert array[number] == validation


FilterByCity = [
    ("Sofia", "People Development Lead"),
    ("Skopje", None),
]


@pytest.mark.parametrize("city, expected_title", FilterByCity)
def test003_check_open_positions_by_city(browser, city, expected_title):
    """
    Visit http://www.musala.com/
    Go to Careers
    Click ‘Check our open positions’ button
    Filter the available positions by available cities in the dropdown ‘Select location’ (Sofia and Skopje)
    Get the open positions by city
    Print in the console the list with available positions by city in the following format:
    Example:
    Sofia
    Position: Database Administrator
    More info: http://www.musala.com/job/database-administrator/
    Position: OS and Application Administrator
    """
    home_page = HomePage(browser)
    home_page.navigate_to_career()

    career_page = CareersPage(browser)
    career_page.navigate_to_join_us()
    assert career_page.get_current_url() == "https://www.musala.com/careers/join-us/"

    join_us_page = JoinUsPage(browser)
    join_us_page.select_location_from_ddl(city)
    actual_title = join_us_page.select_specific_title_from_list(city)
    assert actual_title == expected_title
    if actual_title is not None:
        print(city)
        print("Position: " + actual_title)

