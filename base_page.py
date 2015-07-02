from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec


class BaseTestObject(object):
    def __init__(self, driver):
        self.driver = driver

    def find(self, selector):
        return self.driver.find_element(*selector)

    def find_elements(self, selector):
        return self.driver.find_elements(*selector)

    def wait_for(self, selector):
        timeout = 10
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(selector))
        except TimeoutException:
            msg = "Waiting {0} seconds for '{1}' timed out."
            msg = msg.format(str(timeout), str(selector))
            raise TimeoutException(msg)

