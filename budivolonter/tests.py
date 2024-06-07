from django.test import TestCase, Client, SimpleTestCase,LiveServerTestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create your tests here.
class ApplicationTest(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        from .model_funcs import insertVolunteer
        insertVolunteer('marko','markovic','1990-01-01','marko@gmail.com', 'Pass1234','')        
        self.driver.get(f'{self.live_server_url}/budivolonter/login')
        self.driver.maximize_window()
        email_input = self.driver.find_element(By.NAME, 'email')
        password_input = self.driver.find_element(By.NAME, 'password')
        submit_button = self.driver.find_element(By.ID, 'submit')
        email_input.send_keys('marko@gmail.com')
        password_input.send_keys('Pass1234')
        submit_button.click()
        assert (self.driver.current_url.split('?')[0] == f'{self.live_server_url}/budivolonter/profile')
        

    def tearDown(self):
        self.driver.close()
