from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver

def test_search_pep(driver: WebDriver, base_url):
    driver.get(base_url)
    driver.find_element(By.ID, "id-search-field").send_keys("pep")
    driver.find_element(By.ID, "submit").click()

    first_link = driver.find_element(By.CSS_SELECTOR, "#content > div > section > form > ul > li:nth-child(1) > h3 > a").text
    assert "pep" in first_link.lower()

def test_about(driver, base_url):
    # driver.find_element(By.LINK_TEXT, "About").click()
    driver.get(base_url + "/about/")

    title = driver.title
    assert "about" in title.lower()