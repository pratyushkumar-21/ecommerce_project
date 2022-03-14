import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.mark.selenium
def test_dashboard_admin_login(live_server, db_fixture_setup, chrome_browser_instance):
    
    browser = chrome_browser_instance
    browser.get('{}{}'.format(live_server.url, '/admin/login'))

    username = browser.find_element(By.NAME, 'username')
    password = browser.find_element(By.NAME, 'password')
    submit = browser.find_element(By.XPATH,'//input[@type="submit"]')

    username.send_keys("admin")
    password.send_keys("password") 
    submit.send_keys(Keys.ENTER)

    assert "Site administration" in browser.page_source
