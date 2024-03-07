import time
from selenium import webdriver
from pages.men_page import MenPage
from pages.all_men_page import AllMenPage

PRODUCTS_TO_SCRAPE = 200

def start_scraping():
    start_time = time.time()

    with webdriver.Firefox() as driver:
        men_page = MenPage(driver)
        men_page.go_to_men_page()
        men_page.go_to_all_men_page()

        all_men_page = AllMenPage(driver)
        all_men_page.get_products(PRODUCTS_TO_SCRAPE)

    elapsed_time = time.time() - start_time
    print(f"Code runtime: {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}")

if __name__ == '__main__':
    start_scraping()
