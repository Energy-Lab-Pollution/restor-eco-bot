"""
Script that contains the code to scrape the Restor-Eco page
"""

import os
import requests

from util.constants import URL, HEADERS
from util.driver_manager import DriverManager

current_dir = os.getcwd()

if "home" in current_dir:
    download_location = "/usr/bin/chromedriver"
    LOCAL_TEST = False
else:
    download_location = (
        "C:/Users/fdmol/Downloads/chromedriver_win32/chromedriver.exe"
    )
    LOCAL_TEST = True


class RestoreEcoScraper:
    LOCAL_TEST = LOCAL_TEST
    URL = URL

    def __init__(self):
        pass

        if self.LOCAL_TEST:
            print("Local Test")
            self.chrome_driver = DriverManager(
                self.localtest,
                headless=False,
                download_location=download_location,
            )
        else:
            print("Server Test")
            self.chrome_driver = DriverManager(
                self.LOCAL_TEST,
                headless=True,
                download_location=download_location,
            )
