from urllib.parse import urljoin
import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_create(driver: WebDriver):
    driver.get("http://localhost:8080")
    link = driver.find_element(By.LINK_TEXT, "Create location")
    link.click()
    name_input = driver.find_element(By.ID, "location-name")
    name_input.send_keys("Home")

    coord_input = driver.find_element(By.ID, "location-coords")
    coord_input.send_keys("1,1")

    create_location_button = driver.find_element(By.CSS_SELECTOR, "[value='Create location']")
    create_location_button.click()

    WebDriverWait(driver, 10).until(
        ec.text_to_be_present_in_element((By.ID, "locations-table"), "Home"))

    table = driver.find_element(By.ID, "locations-table")
    assert "Home" in table.text    