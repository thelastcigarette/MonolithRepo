from selenium.webdriver.common.by import By
from base_page import BaseTestObject

class HeaderSection(BaseTestObject):

    destroy = By.ID, "btnDestroy"
    stats = By.ID, "btnStats"
    about = By.ID, "btnAbout"

    def click_destroy(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        return bp.find(self.destroy).click()

    def accept_alert(self):
        return self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        return self.driver.switch_to.alert.dismiss()

