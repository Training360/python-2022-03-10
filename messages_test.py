from urllib.parse import urljoin
import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_wait_for_message(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/docs/messages/index.html")
    button = driver.find_element(By.ID, "liveAlertTimeoutBtn")
    button.click()

    message_div = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, ".alert-success")))
    message = message_div.text
    assert "Nice" in message

    