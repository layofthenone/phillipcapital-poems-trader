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
        self.browser.find_elements_by_xpath("/html/body/div/div[1]/div/div[1]/button")[0].click()
        self.browser.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/ul[5]/li/a").click()
        self.browser.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/ul[5]/li/ul/li[2]/a").click()
        """
        # Open a new window
        self.browser.execute_script("window.open('');")
        self.browser.get(acc.PHILLIP_FUTURE_URL)
        # Switch to the new window and open new URL
        self.browser.switch_to.window(self.browser.window_handles[0])
        """

    def login_poems(self):
        self.browser.find_element_by_id("HesapNo").send_keys(self.acc_number)
        self.browser.find_element_by_id("Sifre").send_keys(self.acc_password)
        self.browser.find_element_by_id("BtnGiris").click()

    def accept_the_statement_of_account(self):
        try:
            self.browser.find_element_by_id("Image1").click()
            #if browser.find_element_by_id("ContentSection_btnMutabik"):
                #print("mutabik misin")
                #browser.find_element_by_id("ContentSection_btnMutabik").click()
                #browser.find_element_by_id("ContentSection_btn_Kapat").click()

        except NoSuchElementException:
            pass


def main():
    connect_poems = ConnectPoems()
    connect_poems.open_browser()
    connect_poems.login_poems()
    time.sleep(15)
#    connect_poems.accept_the_statement_of_account()
    connect_poems.open_future_contract_tab()


if __name__ == "__main__":
    main()
