import time
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.shortcuts import redirect
from django.urls import resolve, reverse
from selenium import webdriver
from selenium.webdriver.common.by import By

#Djordje Sarovic
class CreateActivityTest(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_create_activity(self):
        from ..model_funcs import insertOrganization,getUserEmail
        insertOrganization('Organizacija','123456789','+381600000000','organizacija@mejl.com','sifra123')
        self.driver.get(f'{self.live_server_url}/budivolonter/login')
        self.driver.maximize_window()
        
        email_input = self.driver.find_element(By.NAME, 'email')
        password_input = self.driver.find_element(By.NAME, 'password')
        submit_button = self.driver.find_element(By.ID, 'submit')
        email_input.send_keys('organizacija@mejl.com')
        password_input.send_keys('sifra123')
        submit_button.click()
        
        self.driver.find_element(By.ID, 'OtvoriAkt').click()
        ime_input = self.driver.find_element(By.NAME, 'name')
        ime_input.send_keys('TestAkt')
        desc_input = self.driver.find_element(By.NAME, 'desc')
        desc_input.send_keys('TestDesc')
        spots_input = self.driver.find_element(By.NAME, 'spots')
        spots_input.send_keys('1')
        startD_input = self.driver.find_element(By.NAME, 'startDate')
        startD_input.send_keys('10102024')
        endD_input = self.driver.find_element(By.NAME, 'endDate')
        endD_input.send_keys('10102024')
        deadline_input = self.driver.find_element(By.NAME, 'deadlineDate')
        deadline_input.send_keys('01102024')
        city_input = self.driver.find_element(By.NAME, 'city')
        city_input.send_keys('TestCity')
        submit_button = self.driver.find_element(By.ID, 'submitAct')
        submit_button.click()
        poruka=self.driver.find_element(By.ID,'poruka')
        assert 'USPESNO DODATA AKTIVNOST!' in poruka.text

    def tearDown(self):
        self.driver.close()