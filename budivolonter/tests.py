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
class LoginTest(LiveServerTestCase):
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

class ApplicationTest(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_application(self):
        from .model_funcs import insertVolunteer,insertOrganization,insertActivity,getApplicationsForAct,getAllActivities
        insertVolunteer('marko','markovic','1990-01-01','marko@gmail.com', 'Pass1234','')        
        org = insertOrganization(ime='TestOrg',pib=88888888,telefon='0616357399',email='org@gmail.com',lozinka='Pass1234')
        act = insertActivity(org=org,name='testAkt',desc='',spots=1,startD='2024-09-09',endD='2025-02-02',deadline='2025-02-01',reqs='',city='',country='Srbija',categories='') 
        assert(len(getAllActivities()) == 1) 
        self.driver.get(f'{self.live_server_url}/budivolonter/login')
        self.driver.maximize_window()
        email_input = self.driver.find_element(By.NAME, 'email')
        password_input = self.driver.find_element(By.NAME, 'password')
        submit_button = self.driver.find_element(By.ID, 'submit')
        email_input.send_keys('marko@gmail.com')
        password_input.send_keys('Pass1234')
        submit_button.click()
        assert (self.driver.current_url.split('?')[0] == f'{self.live_server_url}/budivolonter/profile')
        self.driver.find_element(By.ID, 'searchActBtn').click()
        assert (self.driver.current_url == f'{self.live_server_url}/budivolonter/search_activity')
        self.driver.find_element(By.NAME, 'prijavaBtn').click()
        assert (self.driver.current_url.split('?')[0] == f'{self.live_server_url}/budivolonter/activity_form')
        pismo = self.driver.find_element(By.NAME, 'pismo')
        pismo.send_keys('TEST PISMO')
        submit_button = self.driver.find_element(By.ID, 'submit')
        submit_button.click()
        assert (len(getApplicationsForAct(idakt=act.idakt)) == 1)



    def tearDown(self):
        self.driver.close()
