import time

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.shortcuts import redirect, render
from django.test import (
    Client,
    LiveServerTestCase,
    RequestFactory,
    SimpleTestCase,
    TestCase,
)
from django.urls import resolve, reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WebChatTest(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_openChat(self):
        from ..model_funcs import insertOrganization, insertVolunteer

        self.user = insertVolunteer(
            "marko", "markovic", "1990-01-01", "marko@gmail.com", "Pass1234", ""
        )
        self.org = insertOrganization(
            ime="TestOrg",
            pib=88888888,
            telefon="0616357399",
            email="org@gmail.com",
            lozinka="Pass1234",
        )
        self.driver.get(f"{self.live_server_url}/budivolonter/login")
        self.driver.maximize_window()
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.ID, "submit")
        email_input.send_keys("marko@gmail.com")
        password_input.send_keys("Pass1234")
        submit_button.click()
        assert (
            self.driver.current_url.split("?")[0]
            == f"{self.live_server_url}/budivolonter/profile"
        )
        prepiske_btn = self.driver.find_element(By.ID, "inbox")
        prepiske_btn.click()
        assert (
            self.driver.current_url.split("?")[0]
            == f"{self.live_server_url}/budivolonter/inbox"
        )


# Create your tests here.
