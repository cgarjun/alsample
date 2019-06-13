import importlib
import drivers.json_driver


class ContactManager(object):

    def __init__(self, file_path, driver_name):
        self.file_path = file_path
        self.driver_name = driver_name

    def get_driver(self):
        '''
            Returns the specified driver
        '''
        return importlib.import_module("drivers.{0}".format(self.driver_name))

    def display_schema(self):
        pass

    def run(self):
        driver = self.get_driver()
        driver_obj = driver.Driver(self.file_path)
        for i in driver_obj.fetch():
            i.display()