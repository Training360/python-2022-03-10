from LocationsMainPage import LocationsMainPage


def test_create(driver):
    page = LocationsMainPage(driver)
    page.open() \
        .click_create_location_link() \
        .fill_form("Work", "2,2")
    print("end")


def test_empty_name(driver):
    page = LocationsMainPage(driver)
    page.open()
    page.click_create_location_link()
    page.fill_form("")
    print("end")

def test_empty_coords(driver):
    page = LocationsMainPage(driver)
    page.open()
    page.click_create_location_link()
    page.fill_form(coords="")
    print("end")