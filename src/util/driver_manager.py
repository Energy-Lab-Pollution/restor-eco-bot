# Class - DriverManager
# Author - Federico Dominguez Molina
# Description - This class is used to manage the driver and browser instances


import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome import webdriver as chrome_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

# Local imports
from util.constants import TIMEOUT


class DriverManager:
    TIMEOUT = TIMEOUT

    def __init__(self, localtest, headless, download_location):
        self.localtest = localtest
        self.download_location = download_location
        self.headless = headless
        self.driver = self._get_chrome_driver()
        self.action = ActionChains(self.driver)

    def _get_chrome_driver(self):
        chrome_options = chrome_webdriver.Options()
        chrome_options.add_argument("--no-sandbox")

        if self.headless:
            chrome_options.add_argument("--headless")
            # chrome_options.add_argument("--no-sandbox")

        # if self.download_location:
        prefs = {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": False,
            "safebrowsing.disable_download_protection": True,
            # Set "enabled": False if you want authomatic downloads.
            "plugins.plugins_list": [
                {"enabled": False, "name": "Chrome PDF Viewer"}
            ],
        }

        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-gpu")

        # chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        driver_path = self.download_location

        print(driver_path)
        driver = Chrome(executable_path=driver_path, options=chrome_options)

        return driver

    def get_page(self, page):
        self.driver.get(page)

    def click_by_xpath(self, xpath):
        """
        Función que recibe un xpath, un driver y lo que hace es darle click
        al elemento asociado a dicho xpath
        """
        button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        # button = self.driver.find_element_by_xpath(xpath)

        try:
            button = WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            print("Hovering to button")
            self.action.move_to_element(button)
            self.action.perform()
            button.click()
        except Exception as error:
            print(str(error))
            # self.action.move_to_element(button).click().perform()
            self.driver.execute_script("arguments[0].click();", button)
        return button

    def click_by_iden(self, iden):
        """
        Función que recibe un id, un driver y lo que hace es darle click
        al elemento asociado a dicho id
        """
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located((By.ID, iden))
        )
        # button = self.driver.find_element_by_id(iden)
        try:
            button = WebDriverWait(self.driver, TIMEOUT).until(
                EC.element_to_be_clickable((By.ID, iden))
            )
            print("Hovering to button")
            self.action.move_to_element(button)
            self.action.perform()
            button.click()
        except Exception as error:
            print(str(error))
            self.driver.execute_script("arguments[0].click();", button)

        return button

    def send_text(self, xpath, text):
        # le damos click al text box
        text_box = self.click_by_xpath(xpath)

        # Mándamos 'Minatitlan'
        text_box.send_keys(text)

    def get_text(self, xpath):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return self.driver.find_element(by=By.XPATH, value=xpath).text

    def get_text_or_value(self, xpath):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element = self.driver.find_element(by=By.XPATH, value=xpath)

        if element.get_attribute("value"):
            return element.get_attribute("value")
        else:
            return element.text

    def get_texts(self, xpath):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        texts = self.driver.find_elements(by=By.XPATH, value=xpath)
        texts = [i.text for i in texts]
        return texts

    def is_clickable(self, id):
        try:
            WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.element_to_be_clickable((By.XPATH, id))
            )
            return True
        except selenium.common.exceptions.TimeoutException:
            return False
