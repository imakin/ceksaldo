from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

class Klikbca:
    """Get account balance from klikbca"""

    def __init__(self, browser, username, password):
        self.browser = browser
        self.username = username
        self.password = password
        self.browser.implicitly_wait(10)

    def visit_klikbca(self):
        self.browser.get('https://ibank.klikbca.com')

    def login(self):
        input_username = self.browser.find_element_by_css_selector('input#user_id')
        input_password = self.browser.find_element_by_css_selector('input#pswd')

        input_username.send_keys(self.username)
        input_password.send_keys(self.password)
        input_password.send_keys(Keys.ENTER)

    def visit_balance_page(self):
        self.__switch_to_menu_frame()
        account_information_link = self.browser.find_element_by_link_text('Account Information')
        account_information_link.click()
        balance_inquiry_link = self.browser.find_element_by_link_text('Balance Inquiry')
        balance_inquiry_link.click()
        self.browser.switch_to_default_content()

    def fetch_balance_value(self):
        self.__switch_to_main_frame()
        balance_cell_selector = 'body > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4)'
        balance_cell = self.browser.find_element_by_css_selector(balance_cell_selector)
        self.account_balance = balance_cell.text
        self.browser.switch_to_default_content()

    def get_balance(self):
        self.visit_klikbca()
        self.login()
        self.visit_balance_page()
        self.fetch_balance_value()

    def __switch_to_menu_frame(self):
        self.browser.switch_to_frame('menu')

    def __switch_to_main_frame(self):
        self.browser.switch_to_frame('atm')


def main():
    username = sys.argv[1]
    password = sys.argv[2]

    browser = webdriver.Firefox()

    klikbca = Klikbca(browser, username, password)
    klikbca.get_balance()
    print(klikbca.account_balance)

    browser.quit()

if __name__ == '__main__':
    main()
