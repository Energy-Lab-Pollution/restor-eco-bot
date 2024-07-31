"""
Script that contains the code to scrape the Restor-Eco page
"""

import os
import time

from util.constants import URL
from util.driver_manager import DriverManager

current_dir = os.getcwd()

if "home" in current_dir:
    download_location = "/usr/bin/chromedriver"
    LOCAL_TEST = False
elif "mnt" in current_dir:
    download_location = (
        "/mnt/c/Users/fdmol/Downloads/chromedriver-win32/chromedriver.exe"
    )
    LOCAL_TEST = True

else:
    download_location = (
        "C:/Users/fdmol/Downloads/chromedriver-win32/chromedriver.exe"
    )
    LOCAL_TEST = True


class RestoreEcoScraper:
    LOCAL_TEST = LOCAL_TEST
    URL = URL

    def __init__(self):
        if self.LOCAL_TEST:
            print("Local Test")
            self.chrome_driver = DriverManager(
                self.LOCAL_TEST,
                headless=False,
                download_location=download_location,
            )
            # self.go_to_webpage()
        else:
            print("Server Test")
            self.chrome_driver = DriverManager(
                self.LOCAL_TEST,
                headless=True,
                download_location=download_location,
            )

    def go_to_webpage(self):
        """
        Goes to webpage
        """
        print(f"Going to webpage: {self.URL}")
        self.chrome_driver.get_page(self.URL)

    def hover_to_org(self):
        """
        Hovers to the first org in the page
        """
        xpath = "/html/body/div[1]/div/div[2]/aside/div/div/div/div/div[2]/div/ul/li[1]/a/article/div/span[2]"
        self.chrome_driver.hover_by_xpath(xpath)


if __name__ == "__main__":

    restore_scraper = RestoreEcoScraper()
    restore_scraper.go_to_webpage()
    time.sleep(3)
    restore_scraper.hover_to_org()
    time.sleep(2)
    restore_scraper.chrome_driver.scroll_down()
