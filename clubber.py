from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from base_page import BaseTestObject

class ClubberPageSection(BaseTestObject):

    # Melee unit selectors
    buy_melee = By.ID, "btn_buyMelee"
    m_cost = By.ID, "costMelee"
    m_name = By.ID, "nameMelee"
    m_owned = By.ID, "ownedMelee"
    # Ranged Unit selectors
    buy_ranged = By.ID, "btn_buyRanged"
    r_cost = By.ID, "costRanged"
    r_name = By.ID, "nameRanged"
    r_owned = By.ID, "ownedRanged"
    # Cavalry Unit selectors
    buy_cavalry_unit = By.ID, "btn_buyMounted"
    c_cost = By.ID, "costMounted"
    c_owned = By.ID, "ownedMounted"
    c_name = By.ID, "nameMounted"
    # Artillery Unit selectors
    # Flying Unit selectors

    def waiting(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        bp.wait_for(self.buy_melee)

    def upgrade_sword(self, num, letter):
        driver = self.driver
        bp = BaseTestObject(driver)
        sword_upgrade = "upgradeBtnSword_{0}_{1}"
        sword = By.ID, sword_upgrade.format(num, letter)
        try:
            bp.find(sword).click()
        except NoSuchElementException:
            pass

    def check_ranged_present(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        bp.wait_for(self.buy_ranged)

    def buy_clubber(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        bp.find(self.buy_melee).click()

    def get_clubber_cost(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        total = bp.find(self.m_cost).text
        clubs = total.split()
        cost = clubs[0].replace(',', '')
        return int(cost)

    def get_clubber_owned(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        num = bp.find(self.m_owned).text
        return int(num)

    def get_clubber_name(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        return bp.find(self.m_name).text

    def buy_ranged_unit(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        bp.find(self.buy_ranged).click()

    def get_ranged_cost(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        total = bp.find(self.r_cost).text
        rocks = total.split()
        cost = rocks[0].replace(',', '')
        return int(cost)

    def get_ranged_owned(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        num = bp.find(self.r_owned).text
        return int(num)

    def get_ranged_name(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        return bp.find(self.r_name).text

    def buy_cavalry(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        bp.find(self.buy_cavalry_unit).click()

    def get_cavalry_cost(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        total = bp.find(self.c_cost).text
        horse = total.split()
        cost = horse[0].replace(',', '')
        return int(cost)

    def get_cavalry_owned(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        num = bp.find(self.c_owned).text
        return int(num)

    def get_cavalry_name(self):
        driver = self.driver
        bp = BaseTestObject(driver)
        return bp.find(self.c_name).text
