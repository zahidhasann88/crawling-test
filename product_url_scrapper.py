import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from pages.product_details_page import ProductDetailsPage
from utils.utils import Utils

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

class ProductLinkScraper:
    def __init__(self, driver_path=None):
        self.driver_path = driver_path
        self.driver = self.initialize_driver()
        self.base_url = "https://shop.adidas.jp/item/?gender="

    def initialize_driver(self):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def scroll_page(self, times=5, delay=4):
        for _ in range(times):
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            time.sleep(delay)

    def get_product_urls(self, page):
        self.driver.get(page)
        time.sleep(5)
        self.scroll_page()
        product_elements = self.driver.find_elements(
            By.CSS_SELECTOR, "a.image_link"
        )
        return [element.get_attribute("href") for element in product_elements]

    def scrape_sites(self, pages):
        all_product_urls = []
        for page in pages:
            product_urls = self.get_product_urls(page)
            all_product_urls.extend(product_urls)
            for url in product_urls:
                logging.info(url)
        return all_product_urls

    def save_to_file(self, filename, urls):
        with open(filename, "w") as file:
            for url in urls:
                file.write(url + "\n")

    def quit(self):
        if self.driver:
            self.driver.quit()

    def read_from_file(self, filename):
        with open(filename, "r") as file:
            urls = file.readlines()
            urls = [url.strip() for url in urls]
            return urls

    def work(self):
        categories = [
            "mens&category=footwear&group=sneakers",
            "mens&category=wear&group=tops",
            "mens&category=wear&group=bottoms",
            "mens&sport=running&category=footwear",
        ]

        scraper = ProductLinkScraper()
        base_url = scraper.base_url
        pages = [base_url + category for category in categories]

        all_product_urls = scraper.scrape_sites(pages)
        scraper.save_to_file("product_urls.txt", all_product_urls)
        scraper.quit()

        my_pages = scraper.read_from_file("product_urls.txt")
        return my_pages
