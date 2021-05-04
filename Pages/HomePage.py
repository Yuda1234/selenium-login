from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):

    ADMIN_BTN = (By.ID, "//b[text()[contains(.,'Admin')]]")
    WELCOME_LINK = (By.ID, "welcome")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self,title):
        return self.get_title(title)

    def is_user_managment_exist(self):
        return self.is_visible(self.ADMIN_BTN)

    def get_welcome_link_exist(self):
        return self.is_visible(self.WELCOME_LINK)