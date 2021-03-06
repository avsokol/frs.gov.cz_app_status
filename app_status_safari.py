import os
import stat
import sys
from selenium import webdriver
import drivers.drv_config as drv
from inc.helpers import prepare_dump_path, str2bool
from lib.common_engine import CommonEngine


class DarwinEngine(CommonEngine):

    ROBOT_LIBRARY_SCOPE = "TEST SUITE"

    def __init__(self, url=None, driver_path=None):
        print("DarwinEngine Init")
        super(DarwinEngine, self).__init__(url)

        self.platform = sys.platform
        self.engine = "safari"

        if driver_path is None:
            driver_path = "/usr/bin/safaridriver"

        self.driver_path = driver_path

        self.make_sure_engine_is_ready()

    @staticmethod
    def prepare_dump_engine():
        prepare_dump_path()

    def make_sure_engine_is_ready(self):
        if not os.path.exists(self.driver_path):
            url = drv.DRIVERS[self.platform][self.engine]
            save_dir = os.path.dirname(self.driver_path)

            downloaded_driver = drv.download_file(url, save_dir)
            drv.extract_archive(downloaded_driver, save_dir=save_dir)
            os.remove(downloaded_driver)

        if self.platform not in ["windows", "win32"]:
            if not drv.is_file_executable(self.driver_path):
                st = os.stat(self.driver_path)
                os.chmod(self.driver_path, st.st_mode | stat.S_IEXEC)

    def start_engine(self, headless=None):
        print("driver", self.driver_path)
        safari_options = webdriver.WebKitGTKOptions()

        if headless is None:
            headless = HEADLESS

        if isinstance(headless, str):
            headless = str2bool(headless)

        safari_options.headless = headless
        print("Headless mode: '{0}'".format(headless), type(headless))

        self._driver = webdriver.Safari(executable_path=self.driver_path)
        self._driver.set_window_size(1440, 900)


if __name__ == "__main__":
    from inc.frsapp.config import FRSAPP_URL, HEADLESS
    from lib.do_task import just_run

    browser = DarwinEngine(FRSAPP_URL)
    engine_path = browser.driver_path
    browser.prepare_dump_engine()
    browser.start_engine()
    just_run(browser)
    browser.exit()
