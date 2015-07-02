from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from base_page import BaseTestObject

class EvoPointPageSection(BaseTestObject):

    available_evo = By.ID, "evoPoints"
    current_eps = By.ID, "EPS2"
    age = By.ID, "currentAge"
    upgrades = By.ID, "upgradesMenu"

    scholar = By.ID, "btn_buyScholar"
    s_name = By.ID, "nameScholar"
    s_owned = By.ID, "ownedScholar"
    s_cost = By.ID, "costScholar"

    def waiting(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        bp.wait_for(self.scholar)

    def get_evo_points(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        points = bp.find(self.available_evo).text
        avail = points.split()
        total = avail[0].replace(',', "")
        return int(total)

    def get_evo_per_second(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        return bp.find(self.current_eps).text

    def get_age(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        return bp.find(self.age).text

    def buy_scholar(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        bp.find(self.scholar).click()

    def get_name(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        return bp.find(self.s_name).text

    def get_scholar_owned(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        num = bp.find(self.s_owned).text
        return int(num)

    def get_scholar_cost(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        total = bp.find(self.s_cost).text
        scholar = total.split()
        cost = scholar[0].replace(',', '')
        return int(cost)

    def purchase_upgrades(self, num, letter):
        driver = self.driver
        bp = BaseTestObject(driver)
        monolith = "upgradeBtnMonolith_{0}_{1}"
        upgrade = By.ID, monolith.format(num, letter)
        try:
            bp.find(upgrade).click()
        except NoSuchElementException:
            pass

    def upgrade_barracks(self, num, letter):
        driver = self.driver
        bp = BaseTestObject(driver)
        barracks = "upgradeBtnBarracks_{0}_{1}"
        upgrade = By.ID, barracks.format(num, letter)
        try:
            bp.find(upgrade).click()
        except NoSuchElementException:
            pass
