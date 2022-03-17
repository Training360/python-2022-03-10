import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver


# import pytest
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager


# @pytest.fixture
# def driver():
#     # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
#     driver.get("https://python.org")
#     return driver