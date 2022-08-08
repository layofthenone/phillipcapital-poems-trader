from selenium import webdriver
from selenium.common.exceptions import *
import time

url ="https://h.phillip.com.tr/(S(mnw14ipff0ooiqm5u42mtr4l))/login.aspx?ReturnUrl=%2f"
account_number = ""
password = ""


def open_browser(poems_url):
    global browser
    browser = webdriver.Firefox()
    browser.get(poems_url)


def login_poems(acc_number, acc_password):
    browser.find_element_by_id("HesapNo").send_keys(acc_number)
    browser.find_element_by_id("Sifre").send_keys(acc_password)
    browser.find_element_by_id("BtnGiris").click()


def accept_the_statement_of_account():
    try:
        browser.find_element_by_id("Image1").click()
        #if browser.find_element_by_id("ContentSection_btnMutabik"):
            #print("mutabik misin")
            #browser.find_element_by_id("ContentSection_btnMutabik").click()
            #browser.find_element_by_id("ContentSection_btn_Kapat").click()

    except NoSuchElementException:
        pass


def main():
    open_browser(url)
    login_poems(account_number, password)
    time.sleep(10)
    accept_the_statement_of_account()


if __name__ == "__main__":
    main()
