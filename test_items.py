#!/usr/bin/env python3

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestFindElement():
    
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."
    
    def test_find_basket_button(self, browser):
        browser.get(self.link)
        basket_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//form[@id='add_to_basket_form']//button"))
        )
        time.sleep(5)
        
        assert basket_button is not None, "Button is not find"
if __name__ == "__main__":
    unittest.main()
