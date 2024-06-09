
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

class AdminTest(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_admin_delete_user(self):
        from ..utils import insertAdmin
        from ..model_funcs import insertVolunteer
        insertAdmin()
        insertVolunteer('Volonter','Test','2000-01-01','volonter@mejl.com','sifra123','')
        self.driver.get(f'{self.live_server_url}/budivolonter/login')
        self.driver.maximize_window()
       
        email_input = self.driver.find_element(By.NAME, 'email')
        password_input = self.driver.find_element(By.NAME, 'password')
        submit_button = self.driver.find_element(By.ID, 'submit')
        email_input.send_keys('admin@bv.rs')
        password_input.send_keys('Admin123')
        submit_button.click()
        #assert (self.driver.current_url.split('?')[0] == f'{self.live_server_url}/budivolonter/admin_start')
        
        delete_input=self.driver.find_element(By.ID, 'email')
        delete_button=self.driver.find_element(By.ID, 'obrisiKorisnika')
        delete_input.send_keys('volonter@mejl.com')
        delete_button.click()
        poruka=self.driver.find_element(By.ID,'poruka')
        assert 'Obrisan korisnik volonter@mejl.com' in poruka.text

        delete_input=self.driver.find_element(By.ID, 'email')
        delete_button=self.driver.find_element(By.ID, 'obrisiKorisnika')
        delete_input.send_keys('volonter@mejl.com')
        delete_button.click()
        poruka=self.driver.find_element(By.ID,'poruka')
        assert 'Ne postoji korisnik sa tom email adresom' in poruka.text
        
        delete_input=self.driver.find_element(By.ID, 'email')
        delete_button=self.driver.find_element(By.ID, 'obrisiKorisnika')
        delete_input.send_keys('')
        delete_button.click()
        greske = self.driver.find_elements(By.CSS_SELECTOR,'input:invalid') 
        poruka = greske[0].get_attribute('validationMessage')
        assert 'Please fill in this field.' in poruka.text

    def test_admin_delete_activity(self):
        from ..utils import insertAdmin
        from ..model_funcs import insertOrganization,insertActivity,getUserEmail
        insertAdmin()
        insertOrganization('Organizacija','123456789','+381600000000','organizacija@mejl.com','sifra123')
        insertActivity(getUserEmail('organizacija@mejl.com'),'Aktivnost','',1,'2030-01-01','2030-01-01','2030-01-01','','Avganistan','','')
        self.driver.get(f'{self.live_server_url}/budivolonter/login')
        self.driver.maximize_window()
        
        email_input = self.driver.find_element(By.NAME, 'email')
        password_input = self.driver.find_element(By.NAME, 'password')
        submit_button = self.driver.find_element(By.ID, 'submit')
        email_input.send_keys('admin@bv.rs')
        password_input.send_keys('Admin123')
        submit_button.click()
        #assert (self.driver.current_url.split('?')[0] == f'{self.live_server_url}/budivolonter/admin_start')
        
        delete_input=self.driver.find_element(By.ID, 'aktivnost')
        delete_button=self.driver.find_element(By.ID, 'obrisiAktivnost')
        delete_input.send_keys('1')
        delete_button.click()
        poruka=self.driver.find_element(By.ID,'poruka')
        assert 'Obrisana aktivnost 1' in poruka.text

        delete_input=self.driver.find_element(By.ID, 'aktivnost')
        delete_button=self.driver.find_element(By.ID, 'obrisiAktivnost')
        delete_input.send_keys('0')
        delete_button.click()
        poruka=self.driver.find_element(By.ID,'poruka')
        assert 'Ne postoji aktivnost sa tim ID' in poruka.text
        
        delete_input=self.driver.find_element(By.ID, 'aktivnost')
        delete_button=self.driver.find_element(By.ID, 'obrisiAktivnost')
        delete_input.send_keys('')
        delete_button.click()
        greske = self.driver.find_elements(By.CSS_SELECTOR,'input:invalid') 
        poruka = greske[0].get_attribute('validationMessage')
        assert 'Please fill in this field.' in poruka
    
    def tearDown(self):
        self.driver.close()

