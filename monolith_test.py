from selenium import webdriver
import unittest
import time
from damage import DamagePageSection
from clubber import ClubberPageSection
from evopoints import EvoPointPageSection
from stats import StatsPage

class MonolithTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://monolith.greenpixel.ca/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_1_buy_clubbers(self):
        driver = self.driver
        driver.get(self.base_url)
        ml = DamagePageSection(driver)
        club = ClubberPageSection(driver)
        evo = EvoPointPageSection(driver)
        header = StatsPage(driver)
        max_allowed = 0
        points = 0
        m_cost = club.get_clubber_cost()
        try:
            header.import_save()
            driver.refresh()
            max_allowed = club.get_clubber_owned()
            print str(max_allowed) + " close-range fighters owned."
            points = evo.get_evo_points()
        except IOError:
            print "There is no data to import yet."
        club.waiting()
        start_time = time.time()
        while max_allowed < 10:
            ml.click_egg()
            while points > m_cost:
                club.buy_clubber()
                points -= m_cost
                m_cost = club.get_clubber_cost()
                print str(m_cost) + " evo to buy new unit."
                max_allowed += 1
                print str(max_allowed) + " total units owned"
            if (time.time() - start_time) > 30:
                points = evo.get_evo_points()
                print str(points) + " are available to spend."
                start_time = time.time()
        header.export_save()

    def test_2_first_upgrades(self):
        driver = self.driver
        driver.get(self.base_url)
        ml = DamagePageSection(driver)
        club = ClubberPageSection(driver)
        evo = EvoPointPageSection(driver)
        header = StatsPage(driver)
        value = "01"
        upgrade = 0
        points = 0
        try:
            header.import_save()
            points = evo.get_evo_points()
            print "Number of available points: " + str(points)
        except IOError:
            pass
        age = str(evo.get_age()).lower()
        start_time = time.time()
        print "Current Age is " + age
        while age == "stone age":
            ml.click_egg()
            if (time.time() - start_time) > 30:
                points = evo.get_evo_points()
                print "Update! Number of available points: " + str(points)
                start_time = time.time()
            if points > 25:
                club.upgrade_sword(value, "a")
                points -= 25
            if points > 100 and upgrade == 0:
                evo.purchase_upgrades(value, "c")
                points -= 100
                upgrade += 1
            if points > 200 and upgrade == 1:
                evo.purchase_upgrades(value, "a")
                points -= 200
                upgrade += 1
            if points > 200 and upgrade == 2:
                evo.purchase_upgrades(value, "b")
                points -= 200
                upgrade += 1
            if points > 500 and upgrade == 3:
                evo.purchase_upgrades(value, "d")
                points -= 500
                upgrade += 1
            if upgrade == 4:
                age = str(evo.get_age()).lower()
        header.export_save()

    def test_3_buy_scholars(self):
        driver = self.driver
        driver.get(self.base_url)
        ml = DamagePageSection(driver)
        evo = EvoPointPageSection(driver)
        header = StatsPage(driver)
        owned = evo.get_scholar_owned()
        cost = evo.get_scholar_cost()
        try:
            header.import_save()
        except IOError:
            pass
        evo.waiting()
        points = evo.get_evo_points()
        print "Number of available points: " + str(points)
        start = time.time()
        while owned < 10:
            ml.click_egg()
            if (time.time() - start) > 30:
                points = evo.get_evo_points()
                print "Updated number of points: " + str(points)
                while points > cost:
                    evo.buy_scholar()
                    points -= cost
                    cost = evo.get_scholar_cost()
                    owned += 1
                start = time.time()
        r_present = False
        while r_present is False:
            ml.click_egg()
            if points > 600:
                evo.purchase_upgrades("02", "a")
                r_present = True
        header.export_save()

    def test_4_buy_ranged(self):
        driver = self.driver
        driver.get(self.base_url)
        ml = DamagePageSection(driver)
        evo = EvoPointPageSection(driver)
        header = StatsPage(driver)
        rocks = ClubberPageSection(driver)
        try:
            header.import_save()
        except IOError:
            pass
        cost = rocks.get_ranged_cost()
        owned = rocks.get_ranged_owned()
        start = time.time()
        while owned < 10:
            ml.click_egg()
            if (time.time() - start) > 30:
                points = evo.get_evo_points()
                while points > cost:
                    rocks.buy_ranged_unit()
                    points -= cost
                    owned += 1
                    cost = rocks.get_ranged_cost()
                start = time.time()
        header.export_save()

    def test_5_upgrade_again(self):
        driver = self.driver
        driver.get(self.base_url)
        ml = DamagePageSection(driver)
        evo = EvoPointPageSection(driver)
        header = StatsPage(driver)
        club = ClubberPageSection(driver)
        value = "02"
        upgrade = 0
        try:
            header.import_save()
        except IOError:
            pass
        age = evo.get_age().lower()
        points = evo.get_evo_points()
        while age == "neolithic age":
            ml.click_egg()
            if points > 500 and upgrade == 0:
                club.upgrade_sword(value, "b")
                points -= 500
                upgrade += 1
                print upgrade
            if points > 1000 and upgrade == 3:
                evo.purchase_upgrades(value, "b")
                upgrade += 1
                points -= 1000
                print upgrade
            if points > 200 and upgrade == 1:
                evo.upgrade_barracks(value, "a")
                upgrade += 1
                points -= 200
                print upgrade
            if points > 400 and upgrade == 2:
                evo.upgrade_barracks(value, "b")
                upgrade += 1
                points -= 400
                print upgrade
            if points > 2500 and upgrade == 4:
                evo.purchase_upgrades(value, "c")
                upgrade += 1
                points -= 2500
            points = evo.get_evo_points()
            if upgrade == 5:
                age = evo.get_age().lower()
                print age
        header.export_save()

    def test_6_more_units(self):
        driver = self.driver
        driver.get(self.base_url)
        ml = DamagePageSection(driver)
        evo = EvoPointPageSection(driver)
        header = StatsPage(driver)
        club = ClubberPageSection(driver)
        try:
            header.import_save()
        except IOError:
            pass
        m_cost = club.get_clubber_cost()
        r_cost = club.get_ranged_cost()
        s_cost = evo.get_scholar_cost()
        m_count = club.get_clubber_owned()
        r_count = club.get_ranged_owned()
        s_count = evo.get_scholar_owned()
        max_unit = 30
        start = time.time()
        upgrade = 0
        horse = 0
        crit = time.time()
        while horse < 1:
            ml.click_egg()
            if (time.time() - crit) > 5:
                ml.click_critical()
                crit = time.time()
            while m_count < 30 or r_count < 30 or s_count < 30 or upgrade < 2:
                ml.click_egg()
                if (time.time() - crit) > 5:
                    ml.click_critical()
                    crit = time.time()
                if (time.time() - start) > 60:
                    points = evo.get_evo_points()
                    if points > 2500 and upgrade == 0:
                        club.upgrade_sword("03", "a")
                        points -= 2500
                        upgrade += 1
                    if points > 10000 and upgrade == 1:
                        club.upgrade_sword("03", "b")
                        points -= 10000
                        upgrade += 1
                    while points > m_cost and m_count < max_unit:
                        club.buy_clubber()
                        m_count += 1
                        points -= m_cost
                        m_cost = club.get_clubber_cost()
                    while points > r_cost and r_count < max_unit:
                        club.buy_ranged_unit()
                        r_count += 1
                        points -= r_cost
                        print points
                        r_cost = club.get_ranged_cost()
                    while points > s_cost and s_count < max_unit:
                        evo.buy_scholar()
                        s_count += 1
                        points -= s_cost
                        print points
                        s_cost = evo.get_scholar_cost()
                    start = time.time()
            if (time.time() - start) > 30:
                points = evo.get_evo_points()
                if points > 10000:
                    evo.purchase_upgrades("03", "b")
                    horse += 1
        header.export_save()

    def test_8_buy_cavalry(self):
        driver = self.driver
        driver.get(self.base_url)
        ml = DamagePageSection(driver)
        evo = EvoPointPageSection(driver)
        header = StatsPage(driver)
        club = ClubberPageSection(driver)
        try:
            header.import_save()
        except IOError:
            pass
        points = evo.get_evo_points()
        cost = club.get_cavalry_cost()
        owned = club.get_cavalry_owned()
        crit = time.time()
        start = time.time()
        while owned < 20:
            ml.click_egg()
            if(time.time() - crit) > 5:
                ml.click_critical()
                start = time.time()
            if(time.time() - start) > 30:
                while points > cost:
                    club.buy_cavalry()
                    points -= cost
                    owned += 1
                    cost = club.get_cavalry_cost()
            points = evo.get_evo_points()
        header.export_save()


    def tear_down(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
