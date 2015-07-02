from selenium.webdriver.common.by import By
from header import HeaderSection

class StatsPage(HeaderSection):

    export = By.ID, "btnExport"
    use_export = By.ID, "btnImport"
    save_game = By.ID, "btnSave"
    save_code = By.XPATH, "//*[@id='export']//textarea"

    def export_save(self):
        driver = self.driver
        header = HeaderSection(driver)
        header.find(self.stats).click()
        header.wait_for(self.export)
        header.find(self.export).click()
        code = header.find(self.save_code).get_attribute("value")
        with open("game_save", "w+") as export_code:
            export_code.write(code)
        header.find(self.stats).click()

    def import_save(self):
        driver = self.driver
        header = HeaderSection(driver)
        header.find(self.stats).click()
        header.wait_for(self.use_export)
        header.find(self.use_export).click()
        with open("game_save", "r") as game_save:
            code = game_save.read()
            driver.switch_to.alert.send_keys(code)
        driver.switch_to.alert.accept()

    def man_save(self):
        driver = self.driver
        header = HeaderSection(driver)
        header.find(self.stats).click()
        header.wait_for(self.save_game)
        header.find(self.save_game).click()
        header.find(self.stats).click()
