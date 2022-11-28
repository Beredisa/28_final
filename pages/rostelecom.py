# содержит конкретные адреса элементов страниц !

# import config
import os
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements

class Rt_Page(WebPage):

    def __init__(self, web_driver, url=''):

        url = 'https://b2c.passport.rt.ru'
        self._web_driver = web_driver

        super().__init__(web_driver, url)



    left_side = WebElement(id='page-left')
    left_side_title = WebElement(ClassName='what-is__title')
    right_side = WebElement(id='page-right')
    right_side_title = WebElement(ClassName="card-container__title")
    right_side_title_2 = WebElement(xpath='//h1[@class="card-container__title"]')

    number_box = WebElement()
    mail_box = WebElement()
    login_box = WebElement()
    personal_account_box = WebElement()












#  Общие элементы сайта


