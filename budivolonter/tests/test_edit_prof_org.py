
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

class EditOrg(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tet_edit_org(self):

        from .model_funcs import insertOrganization

        insertOrganization('Organizacija','123456789','+381600000000','organizacija@mejl.com','sifra123')

        self.driver.get(f'{self.live_server_url}/budivolonter/login')
        self.driver.maximize_window()
        email_input = self.driver.find_element(By.NAME, 'email')
        password_input = self.driver.find_element(By.NAME, 'password')
        submit_button = self.driver.find_element(By.ID, 'submit')
        email_input.send_keys('organizacija@mejl.com')
        password_input.send_keys('sifra123')
        submit_button.click()

        edit_button=self.driver.find_element(By.ID, 'EDIT')
        edit_button.click()


        ime_input = self.driver.find_element(By.NAME, 'ime')
        ime_input.send_keys('OrganizacijaO')
        potvrdi_button=self.driver.find_element(By.ID, 'confirm btn')
        potvrdi_button.click()

        poruka=self.driver.find_element(By.ID,'nazivOrg')
        assert 'OrganizacijaO' in poruka.text
    
    def tearDown(self):
        self.driver.close()

