from selenium.webdriver.common.by import By
import inc.frsapp.constants as constants
from inc.exceptions.unknown_locator_exception import UnknownLocatorException


def _get_locator(locator_text):
    if locator_text == constants.TYPE_ID:
        return By.ID

    if locator_text == constants.TYPE_CLASS:
        return By.CLASS_NAME

    if locator_text == constants.TYPE_NAME:
        return By.NAME

    if locator_text == constants.TYPE_TAG:
        return By.TAG_NAME

    raise UnknownLocatorException


class UI(object):

    @staticmethod
    def get_element_locator(item):
        if item not in constants.APP_UI:
            raise Exception("Item {0} does not exist in dictionary".format(item))

        return \
            _get_locator(constants.APP_UI[item][constants.ELEMENT_TYPE]), \
            constants.APP_UI[item][constants.ELEMENT_TEXT]

    @staticmethod
    def get_app_number_locator():
        return UI.get_element_locator(constants.APP_NUMBER)

    @staticmethod
    def get_app_dash_number_locator():
        return UI.get_element_locator(constants.APP_DASH_NUMBER)

    @staticmethod
    def get_app_type_locator():
        return UI.get_element_locator(constants.APP_TYPE)

    @staticmethod
    def get_app_year_locator():
        return UI.get_element_locator(constants.APP_YEAR)

    @staticmethod
    def get_app_submit_locator():
        return UI.get_element_locator(constants.SUBMIT_BUTTON)

    @staticmethod
    def get_status_message_locator():
        return UI.get_element_locator(constants.STATUS_MESSAGE)

    @staticmethod
    def get_app_status_warning_locator():
        return UI.get_element_locator(constants.APP_STATUS_WARNING)

    @staticmethod
    def get_app_status_success_locator():
        return UI.get_element_locator(constants.APP_STATUS_SUCCESS)
