import pytest
from selenium import webdriver
from ui_text_box_page import TextBoxPage


@pytest.fixture
def driver():
    """Fixture to set up"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_text_box_form_submission(driver):
    """Tests validation"""
    page = TextBoxPage(driver)
    page.open()

    """Test data"""
    full_name = "Donald Duck"
    email = "donald.duck@example.com"
    current_address = "56 Main St"
    permanent_address = "379 Apple Rd"

    """Fill form"""
    page.fill_form(full_name, email, current_address, permanent_address)
    page.submit()

    """Get output"""
    output = page.get_output_text()

    """Comparing the results"""
    assert output["name"] == f"Name:{full_name}", "Full Name does not match!"
    assert output["email"] == f"Email:{email}", "Email does not match!"
    assert output["current_address"] == f"Current Address :{current_address}", "Current Address does not match!"
    assert output["permanent_address"] == f"Permananet Address :{permanent_address}", "Permanent Address does not match!"
