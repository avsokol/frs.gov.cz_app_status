import os
import shutil
from time import sleep
from inc.decorator_funcs import wait_till_exist
from inc.frsapp.env_constants import ROBOT_OUTPUT_DIR, DUMP_DIR_NAME

DEFAULT_EFFECT_TIME = 0
DEFAULT_EFFECT_COLOR = "red"
DEFAULT_BORDER_WIDTH = 2


def highlight(element, effect_time=None, color=None, border=None):
    """Highlights (blinks) a Selenium WebDriver element"""
    if effect_time is None:
        effect_time = DEFAULT_EFFECT_TIME

    if color is None:
        color = DEFAULT_EFFECT_COLOR

    if border is None:
        border = DEFAULT_BORDER_WIDTH

    driver = element.parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    sleep(effect_time)
    apply_style(original_style)


def click_it(element, effect_time=None, color=None, border=None):
    if effect_time is None:
        effect_time = DEFAULT_EFFECT_TIME

    if color is None:
        color = DEFAULT_EFFECT_COLOR

    if border is None:
        border = DEFAULT_BORDER_WIDTH

    highlight(element, effect_time, color, border)
    element.click()


@wait_till_exist
def click_me(element, element_human_name=None, effect_time=None, color=None, border=None):
    show_element = element
    if element_human_name is not None:
        show_element = element_human_name

    if element is None:
        raise Exception("Element '{0}' couldn't be found", show_element)

    print("Click on '{0}'".format(show_element))
    click_it(element, effect_time=effect_time, color=color, border=border)
    print("Ok, {0} clicked!".format(show_element))


def str2bool(input_string):
    if not isinstance(input_string, str):
        raise Exception("Input must be string, not '{0}': '{1}'".format(input_string, type(input_string)))

    if input_string in ["true", "True", "t", "T"]:
        return True

    if input_string in ["false", "False", "f", "F"]:
        return False

    raise Exception("Unsupported input for converting to boolean: {0}".format(input_string))
    

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def prepare_dump_path():
    cur_dir = os.path.dirname(__file__)
    save_dir = os.path.abspath(os.path.join(cur_dir, "..", "..", ROBOT_OUTPUT_DIR, DUMP_DIR_NAME))

    try:
        if os.path.exists(save_dir):
            shutil.rmtree(save_dir)

    except PermissionError:
        try:
            for file in os.listdir(save_dir):
                os.remove(os.path.join(save_dir, file))

        finally:
            pass

    except Exception:
        raise

    ensure_dir(save_dir)
