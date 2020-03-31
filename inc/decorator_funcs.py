from time import sleep
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from inc.frsapp.constants import DEFAULT_SHORT_TIMEOUT


def wait_till_exist(target_func):
    def func_wrapper(*args, **kwargs):
        interval = 1
        elapsed = 0

        while True:
            if elapsed > DEFAULT_SHORT_TIMEOUT:
                raise Exception("Timeout!")

            try:
                res = target_func(*args, **kwargs)
                print("Ok, waited for {0} sec!".format(elapsed))
                return res

            except (WebDriverException, NoSuchElementException):
                print("Wait for '{0}' sec".format(interval))
                sleep(interval)
                elapsed += interval

            except Exception:
                raise

    return func_wrapper
