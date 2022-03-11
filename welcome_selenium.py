from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

def go_to_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5500/docs/index.html")
    return driver

def get_text_of_paragraph(driver):
    content = driver.find_element(By.CSS_SELECTOR, ".important-p").text
    return content

driver = go_to_page()
content = get_text_of_paragraph(driver)
assert content == "xxxThis is the second paragraph."