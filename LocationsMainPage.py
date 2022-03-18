from urllib.parse import urljoin
import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LocationsMainPage:

    def __init__(self, driver) -> None:
        self.driver = driver


    def open(self):
        self.driver.get("http://localhost:8080")
        return self

    
    def click_create_location_link(self):
        link = self.driver.find_element(By.LINK_TEXT, "Create location")
        link.click()
        return self

    
    def fill_form(self, name: str = "Home", coords: str = "1,1", interesting_at: str = "", 
            tags: str = ""):
        """Kitölti az űrlapot névvel, koordinátákkal, stb."""
        name_input = self.driver.find_element(By.ID, "location-name")
        name_input.send_keys(name)

        coord_input = self.driver.find_element(By.ID, "location-coords")
        coord_input.send_keys(coords)

        interesting_at_input = self.driver.find_element(By.ID, "location-interesting-at")
        interesting_at_input.send_keys(interesting_at)

        tags_input = self.driver.find_element(By.ID, "location-tags")
        tags_input.send_keys(tags)
        return self

    
    def click_on_create_location_button(self):
        create_location_button = self.driver.find_element(By.CSS_SELECTOR, "[value='Create location']")
        create_location_button.click()
        return self
        
    
    def get_text_on_message_panel(self):
        message_div = self.driver.find_element(By.ID, "message-div")
        return message_div.text

    
    def get_error_message(self):
        message_div = self.driver.find_element(By.CSS_SELECTOR, ".invalid-feedback:not([hidden = 'hidden'])")
        return message_div.text