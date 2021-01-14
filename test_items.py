import pytest
from selenium import webdriver
import time


def test_existing_of_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(3)
    button = browser.find_elements_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
    assert button, "The add to basket button is absent"