def myFunk(name_func, *args):
    name = name_func.__name__.title().replace('_', " ")
    print(name, *args)


def open_browser(browser_name):
    myFunk(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    myFunk(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    myFunk(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="https://stepik.org/")
find_registration_button_on_login_page(page_url="https://stepik.org/", button_text= "login")