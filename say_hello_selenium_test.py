from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

def go_to_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5500/docs/index.html")
    return driver

def type_name(driver, name):
    driver.find_element(By.ID, "name-input").send_keys(name)

def press_button(driver):
    driver.find_element(By.ID, "submit-button").click()

def get_message(driver):
    return driver.find_element(By.ID, "message-p").text


def get_list_items(driver):
    elements = driver.find_elements(By.TAG_NAME, "li")
    print(elements)
    items = []
    for element in elements:
        items.append(element.text)
    print(items)
    return items

def test_say_hello():  
    driver = go_to_page()
    type_name(driver, "John Doe")
    press_button(driver)
    message = get_message(driver)
    print(message)
    assert message == "Hello John Doe!"

def test_list():
    driver = go_to_page()
    items = get_list_items(driver)
    assert items == ["Python", "HTML", "JavaScriptx"]