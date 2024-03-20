from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time




class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome()
        super(AccountTestCase, self).setUp()
        self.selenium.maximize_window()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register_and_login(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/register/')
        # Find the form elements
        first_name = selenium.find_element("id", 'first_name')
        last_name = selenium.find_element("id", 'last_name')
        username = selenium.find_element("id", 'username')
        email = selenium.find_element("id", 'email')
        password1 = selenium.find_element("id", 'password')
        password2 = selenium.find_element("id", 'password_repeat')

        # Fill the form with data
        first_name.send_keys('Pragati')
        last_name.send_keys('Singh')
        username.send_keys('pragati')
        email.send_keys('pragati@gmail.com')
        password1.send_keys('@srinidhi')
        password2.send_keys('@srinidhi')

        # Find the submit button by its id
        submit = selenium.find_element("id", 'register_button')

        # Submit the form
        submit.click()
        print(selenium.current_url)
        time.sleep(3)


        # Check if the redirection to the login page happened after successful registration
        # assert '/login/' in selenium.current_url
        # Find the form elements for login by their names
        username_login = selenium.find_element("name", 'username')
        password_login = selenium.find_element("name", 'password')

        # Fill the login form with the registered username and password
        username_login.send_keys('pragati')
        password_login.send_keys('@srinidhi')

        # Find the login submit button 
        login_button = selenium.find_element(By.XPATH, '//button[@type="submit" and contains(@class, "btn-danger")]')

        # Submit the login form
        login_button.click()
        time.sleep(3)
