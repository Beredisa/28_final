import time
import pytest
from pages.base import WebPage
from pages.elements import WebElements
from pages.elements import ManyWebElements
from pages.rostelecom import Rt_Page
from selenium.webdriver import ActionChains


#py -m pytest -v --driver Chrome --driver-path chromedriver.exe test_0.py



def test_sides_is_visible(web_browser):
    page = Rt_Page(web_browser)
    page.wait_page_loaded()

    assert page.left_side.is_visible()








