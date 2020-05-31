import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

from Test_suite.pages.admin_categories_page import AdminCategoriesPage
from Test_suite.pages.admin_product_page import AdminProductPage
from Test_suite.pages.input_page import InputPage
from Test_suite.pages.listener import MyListener


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='Chrome',
        help='This is browser for testing'
    )


@pytest.fixture
def browser_opt(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def browser(browser_opt):
    if browser_opt == 'Chrome':
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--ignore-certificate-errors')
        browser = EventFiringWebDriver(webdriver.Chrome(options=options), MyListener())
    elif browser_opt == 'Firefox':
        options = FirefoxOptions()
        options.add_argument('--kiosk')
        browser = EventFiringWebDriver(webdriver.Firefox(), MyListener())
        profile.accept_untrusted_certs = True
    elif browser_opt == 'IE':
        browser = EventFiringWebDriver(webdriver.Ie(), MyListener())
    yield browser
    browser.quit()


@pytest.fixture()
def admin_product_page(browser):
    page = AdminProductPage(browser)
    page.open()
    page.login_admin()
    page.go_to_product_tab()
    return page


@pytest.fixture()
def setup_product_page(admin_product_page):
    if not admin_product_page.is_product_in_tab(p_name='Mouse'):
        admin_product_page.add_new_product(p_name='Mouse', m_tag='pereferi')


@pytest.fixture()
def admin_categories_page(browser):
    page = AdminCategoriesPage(browser)
    page.open()
    page.login_admin()
    page.go_to_categories()
    return page


@pytest.fixture()
def input_page(browser):
    page = InputPage(browser)
    page.open()
    return page
