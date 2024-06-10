import time
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.shortcuts import redirect
from django.urls import resolve, reverse
from selenium import webdriver
from selenium.webdriver.common.by import By

#Djordje Sarovic
class MyActsTest(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_create_activity(self):
        from ..model_funcs import insertOrganization,insertVolunteer,insertActivity,insertApplication
        
        self.user = insertVolunteer('marko', 'markovic', '1990-01-01', 'marko@gmail.com', 'Pass1234', '')
        self.org = insertOrganization(ime='TestOrg', pib=88888888, telefon='0616357399', email='org@gmail.com', lozinka='Pass1234')
        self.act = insertActivity(org=self.org, name='testAkt', desc='', spots=1, startD='2024-09-09', endD='2025-02-02', deadline='2025-02-01', reqs='', city='', country='Srbija', categories='')
        self.app = insertApplication(idvol=self.user, idakt=self.act.idakt, pismo='testLetter', rezimeFile=None)
        self.app.status = 'A'
        self.app.save()

        self.driver.get(f'{self.live_server_url}/budivolonter/login')
        self.driver.maximize_window()
        email_input = self.driver.find_element(By.NAME, 'email')
        password_input = self.driver.find_element(By.NAME, 'password')
        submit_button = self.driver.find_element(By.ID, 'submit')
        email_input.send_keys('marko@gmail.com')
        password_input.send_keys('Pass1234')
        submit_button.click()

        self.driver.find_element(By.ID, 'mojeAktivnostiBtn').click()
        time.sleep(1)
        assert self.act.naziv in self.driver.page_source
        
    def tearDown(self):
        self.driver.close()
