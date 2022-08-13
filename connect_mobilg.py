from selenium import webdriver
from selenium.common.exceptions import *
import time
import account as acc


class ConnectPoems:

    def __init__(self):
        self.poems_url = acc.PHILLIP_URL
        self.acc_number = acc.ACCOUNT_NUMBER
        self.acc_password = acc.PASSWORD
        self.browser = webdriver.Firefox()

    def open_browser(self):
        try:
            self.browser.get(self.poems_url)

        except WebDriverException:
            time.sleep(10)

    # open new tab
    def open_future_contract_tab(self):
        self.browser.find_elements("xpath", "/html/body/div/div[1]/div/div[1]/button")[0].click()
        self.browser.find_element("xpath", "/html/body/div/div[1]/div/div[2]/ul[5]/li/a").click()
        self.browser.find_element("xpath", "/html/body/div/div[1]/div/div[2]/ul[5]/li/ul/li[2]/a").click()

    def login_poems(self):
        self.browser.find_element("id", "HesapNo").send_keys(self.acc_number)
        self.browser.find_element("id", "Sifre").send_keys(self.acc_password)
        self.browser.find_element("id", "BtnGiris").click()

    def browser_url(self):
        url = self.browser.command_executor.url  # "http://127.0.0.1:60622/hub"
        print(url)
        return url

    def browser_session(self):
        session_id = self.browser.session_id  # '4e167f26-dc1d-4f51-a207-f761eaf73c31'
        print(session_id)
        return session_id

    def accept_the_statement_of_account(self):
        try:
            self.browser.find_element_by_id("Image1").click()
            #if browser.find_element_by_id("ContentSection_btnMutabik"):
                #print("mutabik misin")
                #browser.find_element_by_id("ContentSection_btnMutabik").click()
                #browser.find_element_by_id("ContentSection_btn_Kapat").click()

        except NoSuchElementException:
            pass