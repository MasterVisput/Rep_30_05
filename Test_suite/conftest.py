import logging
import urllib.parse

import pytest
from browsermobproxy import Server, Client
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.events import EventFiringWebDriver

from Test_suite.pages.admin_categories_page import AdminCategoriesPage
from Test_suite.pages.admin_product_page import AdminProductPage
from Test_suite.pages.input_page import InputPage
from Test_suite.pages.listener import MyListener

logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='Chrome',
        help='This is browser for testing'
    )


@pytest.fixture()
def proxy_server(request):
    options = {
        'host': 'localhost',
        'port': 8098,
        'process': None
    }
    server = Server(options=options, path='K:/Learn/Proxy_logger/browsermob-proxy/bin/browsermob-proxy')
    server.start()
    client = Client('localhost:8098')
    server.create_proxy()
    request.addfinalizer(server.stop)
    client.new_har()
    return client


@pytest.fixture
def browser_opt(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def browser(browser_opt, proxy_server):
    if browser_opt == 'Chrome':
        caps = DesiredCapabilities.CHROME
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option('w3c', False)
        caps['loggingPrefs'] = {'perfomance': 'ALL', 'browser': 'ALL'}
        proxy_url = urllib.parse.urlparse(proxy_server.proxy).path
        options.add_argument(f'--proxy-server={proxy_url}')
        browser = EventFiringWebDriver(webdriver.Chrome(options=options, desired_capabilities=caps), MyListener())
        browser.proxy = proxy_server
    elif browser_opt == 'Firefox':
        options = FirefoxOptions()
        options.add_argument('--kiosk')
        browser = EventFiringWebDriver(webdriver.Firefox(), MyListener())
        profile.accept_untrusted_certs = True
    elif browser_opt == 'IE':
        browser = EventFiringWebDriver(webdriver.Ie(), MyListener())
    yield browser
    har = browser.proxy.har['log']
    for el in har['entries']:
        logger.info(el['request'])


@pytest.fixture()
def admin_product_page(browser):
    logger.info('====================Start Setup Activity====================')
    page = AdminProductPage(browser)
    page.open()
    page.login_admin()
    page.go_to_product_tab()
    logger.info('====================End Setup Activity====================')
    return page


@pytest.fixture()
def setup_product_page(admin_product_page):
    if not admin_product_page.is_product_in_tab(p_name='Mouse'):
        admin_product_page.add_new_product(p_name='Mouse', m_tag='pereferi')


@pytest.fixture()
def admin_categories_page(browser):
    logger.info('====================Start Setup Activity====================')
    page = AdminCategoriesPage(browser)
    page.open()
    page.login_admin()
    page.go_to_categories()
    logger.info('====================End Setup Activity====================')
    return page


@pytest.fixture()
def input_page(browser):
    page = InputPage(browser)
    page.open()
    return page
