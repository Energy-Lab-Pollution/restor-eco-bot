"""
Script that contains the code to scrape the Restor-Eco page
"""

import re
import os
import time

from util.constants import URL, DEFAULT_TOTAL_ORGS
from bs4 import BeautifulSoup
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
    DEFAULT_TOTAL_ORGS = DEFAULT_TOTAL_ORGS

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

    def get_total_number_of_orgs(self):
        """
        Gets the total number of orgs in the page
        """

        try:
            html = self.chrome_driver.driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            number_paragraph = soup.find("h2", {"class": "paragraph-md"})
            raw_text = number_paragraph.text
            raw_text = raw_text.replace(",", "")

            number = re.findall(r"\d+", raw_text)

            if number:
                self.total_orgs = number[0]

            else:
                self.total_orgs = self.DEFAULT_TOTAL_ORGS

        except Exception as error:
            print(f"Error getting total number of orgs {error}")
            self.total_orgs = self.DEFAULT_TOTAL_ORGS

        print(raw_text)

    def hover_to_org(self, num_element):
        """
        Hovers to a given org in the webpage
        """
        xpath = f"/html/body/div[1]/div/div[2]/aside/div/div/div/div/div[2]/div/ul/li[{num_element}]/a/article/div/span[2]"
        self.chrome_driver.hover_by_xpath(xpath)

    def extract_available_orgs(self):
        """
        This function extracts the html from the webpage
        """
        html = self.chrome_driver.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        li_elements = soup.find_all("li")

        dicts_list = []

        for li_element in li_elements:
            a_tag = li_element.find("a")
            tmp_dict = {}
            if a_tag and "href" in a_tag.attrs:
                # Get the 'href' attribute
                href = a_tag["href"]
                org_name = li_element.find(
                    "span", {"class": "paragraph-md-bold"}
                )

                img_span = li_element.find(
                    "span", {"class": "w-12 pt-[0.25rem]"}
                )

                tmp_dict["org_name"] = org_name.text
                tmp_dict["url"] = f"https://restor.eco{href}"
                tmp_dict["country_name"] = None

                if img_span:
                    img = img_span.find("img")
                    raw_country_name = img["alt"]
                    tmp_dict["country_name"] = raw_country_name

                dicts_list.append(tmp_dict)

    def run(self):
        """
        Extracts
        """
        pass


if __name__ == "__main__":

    restore_scraper = RestoreEcoScraper()
    restore_scraper.go_to_webpage()
    time.sleep(3)
    restore_scraper.get_total_number_of_orgs()
    restore_scraper.hover_to_org(10)
    time.sleep(2)
    restore_scraper.extract_available_orgs()
