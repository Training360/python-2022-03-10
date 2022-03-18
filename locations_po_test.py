from LocationsMainPage import LocationsMainPage


def test_create(driver):
    page = LocationsMainPage(driver)
    page.open() \
        .click_create_location_link() \
        .fill_form("Work", "2,2") \
        .click_on_create_location_button() \
        .assert_text_on_message_panel("Location has been created")

    # assert page.text_on_message_panel() == "Location has been created"


    print("end")


def test_empty_name(driver):
    page = LocationsMainPage(driver)
    page.open()
    page.click_create_location_link()
    page.fill_form("")
    page.click_on_create_location_button() 
    assert page.get_error_message() == "Can not be empty name!"
    print("end")

def test_empty_coords(driver):
    page = LocationsMainPage(driver)
    page.open()
    page.click_create_location_link()
    page.fill_form(coords="")
    page.click_on_create_location_button()        
    assert page.get_error_message() == "Invalid format!"
    print("end")