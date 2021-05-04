from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.loginPage.is_visible(HomePage.WELCOME_LINK)

    def test_login_invalid_username_and_an_invalid_password(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME_INVALID, TestData.PASSWORD_INVALID)
        self.loginPage.is_visible(LoginPage.ERROR_MSG)

    def test_login_valid_username_and_empty_password(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login_empty_password(TestData.USER_NAME)
        self.loginPage.is_invisible(HomePage.WELCOME_LINK)




