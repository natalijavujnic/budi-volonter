
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

    def test_edit_org_succ(self):

        from ..model_funcs import insertOrganization

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
    
    def test_edit_org_fail_noName(self):

        from ..model_funcs import insertOrganization

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
        ime_input.clear()
        from time import sleep
        potvrdi_button=self.driver.find_element(By.ID, 'confirm btn')
        sleep(5)
        potvrdi_button.click()


        assert (
            self.driver.current_url
            == f"{self.live_server_url}/budivolonter/edit_profile"
        )

    def test_edit_org_fail_noPIB(self):

        from ..model_funcs import insertOrganization

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
        pib_input = self.driver.find_element(By.NAME, 'pib')
        pib_input.clear()
        from time import sleep
        potvrdi_button=self.driver.find_element(By.ID, 'confirm btn')
        sleep(5)
        potvrdi_button.click()


        assert (
            self.driver.current_url
            == f"{self.live_server_url}/budivolonter/edit_profile"
        )
    def test_edit_org_fail_noPhone(self):

        from ..model_funcs import insertOrganization

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
        tel_input = self.driver.find_element(By.NAME, 'telefon')
        tel_input.clear()
        from time import sleep
        potvrdi_button=self.driver.find_element(By.ID, 'confirm btn')
        sleep(5)
        potvrdi_button.click()


        assert (
            self.driver.current_url
            == f"{self.live_server_url}/budivolonter/edit_profile"
        )
    def test_edit_org_fail_usedPIB(self):

        from ..model_funcs import insertOrganization

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
        pib_input = self.driver.find_element(By.NAME, 'pib')
        pib_input.send_keys('123456689')
        from time import sleep
        potvrdi_button=self.driver.find_element(By.ID, 'confirm btn')
        sleep(5)
        potvrdi_button.click()
        assert (
            self.driver.current_url
            == f"{self.live_server_url}/budivolonter/edit_profile"
        )
    
    def test_edit_org_fail_usedPhone(self):

        from ..model_funcs import insertOrganization

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
        tel_input = self.driver.find_element(By.NAME, 'telefon')
        tel_input.send_keys('+381652346866')
        from time import sleep
        potvrdi_button=self.driver.find_element(By.ID, 'confirm btn')
        sleep(5)
        potvrdi_button.click()
        assert (
            self.driver.current_url
            == f"{self.live_server_url}/budivolonter/edit_profile"
        )
        
    def tearDown(self):
        self.driver.close()

