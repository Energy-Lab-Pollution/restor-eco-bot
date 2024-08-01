# Restor-Eco Scraper

This repository contains the code to scrape organizations from the [Restor-Eco website](https://restor.eco/organizations/?lat=26&lng=14.23&zoom=3)

The code is written in Python and uses Selenium and BeautifulSoup to scrape the organizations data. The chromedriver should be in the path outlined in `constants.py`, so this path should be updated accordingly.

The code takes a couple of hours to run, and the output is saved in the `eco-restor-orgs.csv` file.