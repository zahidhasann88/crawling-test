from selenium.webdriver.common.by import By
from utils.utils import Utils
from pages.product_details_page import ProductDetailsPage
from product_url_scrapper import ProductLinkScraper

class AllMenPage:

    def __init__(self, driver):
        self.driver = driver

    DISPLAY_NUMBERS_ACTIVE: tuple[str, str] = (By.XPATH, "//a[contains(@class,'test-active')]")
    DISPLAY_NUMBERS_INACTIVE: tuple[str, str] = (By.XPATH, "//span[contains(@class,'test-inactive')]")
    PRODUCT_TITLE_TEXT: tuple[str, str] = (By.XPATH, "//div[@class='articleDisplayCard-Title']")
    RIGHT_ARROW_BUTTON: tuple[str, str] = (By.XPATH, "//li[contains(@class,'test-next')]")
    FOOTER_CLOSE_BUTTON: tuple[str, str] = (By.XPATH, "//button[@class='footerstickyClosebutton']")
    PAGINATION_NEXT_BUTTONS: tuple[str, str] = (By.XPATH, "//li[contains(@class,'test-next')]")

    def get_products(self, product_count: int = 1):
        utils = Utils()
        footer_close_button_element = utils.find_element_or_none(self.driver, self.FOOTER_CLOSE_BUTTON, 10)
        if footer_close_button_element is not None:
            footer_close_button_element.click()

        p = ProductLinkScraper()
        my_pages = p.work()
        print(my_pages)

        data = []
        for page in my_pages:
            self.driver.get(page)
            productDetailsPage = ProductDetailsPage(self.driver)
            datum = productDetailsPage.get_formatted_data()
            data.append(datum)
        utils.write_dict_to_csv(data, 'output.csv')
