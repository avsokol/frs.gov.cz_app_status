import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import inc.frsapp.constants as constants
from inc.decorator_funcs import wait_till_exist
from inc.frsapp.ui import UI
from inc.helpers import click_me
from lib.common_driver import CommonDriver


class CommonEngine(CommonDriver):

    DEFAULT_TIMEOUT = constants.DEFAULT_TIMEOUT
    DEFAULT_LONG_TIMEOUT = constants.DEFAULT_LONG_TIMEOUT

    ENGINES_EXE = {
        "chrome": "chromedriver",
        "firefox": "geckodriver"
    }

    def __init__(self, url=None):
        super(CommonEngine, self).__init__()
        self.url = url
        self.engine = None
        self.driver_path = None

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def get_content(self):
        self._driver.get(self.url)

    def enter_app_number(self, number):
        number_el = self.find_it(UI.get_app_number_locator())
        click_me(number_el, element_human_name="Application number")
        number_el.clear()
        click_me(number_el, element_human_name="Application number")
        actions = ActionChains(self._driver)
        actions.send_keys(number)
        actions.perform()

    @staticmethod
    def select_option(options_element, item):
        index = 0
        for option_element in options_element.options:
            option_text = option_element.text
            if option_text == item:
                options_element.select_by_index(index)
                break

            index += 1

    def enter_app_type(self, input_type):
        app_types = Select(self.find_it(UI.get_app_type_locator()))
        self.select_option(app_types, input_type)

    def enter_app_year(self, input_year):
        app_years = Select(self.find_it(UI.get_app_year_locator()))
        self.select_option(app_years, input_year)

    def submit_form(self):
        submit_button = self.find_it(UI.get_app_submit_locator())
        click_me(submit_button, element_human_name="Submit")

    def wait_for_submitted_result(self):
        WebDriverWait(self.get_driver(), constants.DEFAULT_SHORT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(UI.get_status_message_locator())
        )

    def stop_engine(self):
        self._driver.quit()

    def final_clean(self):
        if None in [self.engine, self.driver_path]:
            return

        if self.engine == "safari":
            return

        attempts = 2
        period = 5
        count = 0
        while count < attempts:
            try:
                print("Trying to delete engine binary...")
                os.remove(self.driver_path)
                print("Trying to delete engine binary...Ok")
                break

            except PermissionError as e:
                print(f"Final clean exception: {e.args}")
                time.sleep(period)
                count += 1
                continue

            except FileNotFoundError:
                break

            except Exception:
                raise

    @wait_till_exist
    def get_app_status(self):
        try:
            status_el = self.find_it(UI.get_app_status_warning_locator())

        except NoSuchElementException:
            status_el = self.find_it(UI.get_app_status_success_locator())

        except Exception:
            raise

        return status_el.text
