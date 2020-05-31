import logging
import time

from selenium.webdriver.support.events import AbstractEventListener

logging.basicConfig(filename='logs/log.txt', format='%(asctime)s || %(name)s || %(message)s', level=logging.INFO)


class MyListener(AbstractEventListener):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.time = time.time()

    def before_navigate_to(self, url, driver):
        self.logger.info(f'I`m navigate to: {url}')

    def after_navigate_to(self, url, driver):
        self.logger.info(f'I`m on: {url}')

    def before_navigate_back(self, driver):
        self.logger.info(f'I`m navigating back')

    def after_navigate_back(self, driver):
        self.logger.info(f'I`m back')

    def before_find(self, by, value, driver):
        self.logger.info(f'I`m looking for: "{value}" BY: "{by}"')

    def after_find(self, by, value, driver):
        self.logger.info(f'I`ve found "{value}" BY "{by}"')

    def before_click(self, element, driver):
        self.logger.info(f'I`m clicking: {element}')

    def after_click(self, element, driver):
        self.logger.info(f'I`ve clicked: {element}')

    def before_execute_script(self, script, driver):
        self.logger.info(f'I`m executing "{script}"')

    def after_execute_script(self, script, driver):
        self.logger.info(f"I've executed '{script}'")

    def before_quit(self, driver):
        self.logger.info(f"I'm getting ready to terminate {driver}")
        driver.save_screenshot(f'screens/{self.time}.png')

    def after_quit(self, driver):
        self.logger.info(f"WASTED!!!")

    def on_exception(self, exception, driver):
        self.logger.error(f'Oooops i got: {exception}')
        driver.save_screenshot(f'screens/ex_{self.time}.png')

