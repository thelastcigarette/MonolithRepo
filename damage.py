from selenium.webdriver.common.by import By
from base_page import BaseTestObject
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

class DamagePageSection(BaseTestObject):

    egg = By.ID, "beastButton"
    dps = By.ID, "DPS"
    damage = By.ID, "damage"
    shard = By.ID, "shards"
    hero = By.ID, "heroImage"
    hero_state = By.ID, "heroTicker"

    crit = By.ID, "critical"

    def click_egg(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        bp.find(self.egg).click()

    def get_dps(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        return bp.find(self.dps).text

    def get_total_damage(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        return bp.find(self.damage).text

    def click_critical(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        try:
            bp.find(self.crit).click()
        except (ElementNotVisibleException, NoSuchElementException):
            pass
