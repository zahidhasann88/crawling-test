from selenium.webdriver.common.by import By
from utils.utils import Utils
from pages.product_details_page import ProductDetailsPage
from product_url_scrapper import ProductLinkScraper

class AllMenPage:
    DISPLAY_NUMBERS_ACTIVE: tuple[str, str] = (By.XPATH, "//a[contains(@class,'test-active')]")
    DISPLAY_NUMBERS_INACTIVE: tuple[str, str] = (By.XPATH, "//span[contains(@class,'test-inactive')]")
    PRODUCT_TITLE_TEXT: tuple[str, str] = (By.XPATH, "//div[@class='articleDisplayCard-Title']")
    RIGHT_ARROW_BUTTON: tuple[str, str] = (By.XPATH, "//li[contains(@class,'test-next')]")
    FOOTER_CLOSE_BUTTON: tuple[str, str] = (By.XPATH, "//button[@class='footerstickyClosebutton']")
    PAGINATION_NEXT_BUTTONS: tuple[str, str] = (By.XPATH, "//li[contains(@class,'test-next')]")

    def __init__(self, driver):
        self.driver = driver

    def get_products(self, product_count: int = 1):
        utils = Utils()
        footer_close_button_element = utils.find_element_or_none(self.driver, self.FOOTER_CLOSE_BUTTON, 10)
        if footer_close_button_element is not None:
            footer_close_button_element.click()

        product_scraper = ProductLinkScraper()
        product_urls = product_scraper.work()
        print(product_urls)

        data = []
        for url in product_urls:
            self.driver.get(url)
            product_details_page = ProductDetailsPage(self.driver)
            datum = product_details_page.get_formatted_data()
            data.append(datum)
        utils.write_dict_to_csv(data, 'output.csv')
