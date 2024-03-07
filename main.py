import time
from selenium import webdriver

from pages.men_page import MenPage
from pages.all_men_page import AllMenPage


def start_scrapping():
    start_time = time.time()

    driver = webdriver.Firefox()

    men_page = MenPage(driver)
    men_page.go_to_men_page()
    men_page.go_to_all_men_page()

    all_men_page = AllMenPage(driver)
    all_men_page.get_products(200)
    driver.quit()

    print("Code runtime:", time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))


if __name__ == '__main__':
    start_scrapping()
