from inc.helpers import highlight


class CommonDriver(object):

    def __init__(self, driver=None):
        self._driver = driver

    def get_me(self):
        return self

    def get_driver(self):
        return self._driver

    def exit(self):
        self._driver.close()

    def quit(self):
        self._driver.quit()

    def get_title(self):
        return self._driver.title

    def find_it(self, locator, parent=None):
        if parent is None:
            parent = self._driver

        element = parent.find_element(*locator)
        highlight(element)
        return element

    def find_them(self, locator, parent=None, show=True):
        if parent is None:
            parent = self._driver

        elements = parent.find_elements(*locator)
        if show:
            for element in elements:
                highlight(element)

        return elements
