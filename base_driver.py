from abc import ABCMeta, abstractmethod

class BaseDriver:
    __metaclass__ = ABCMeta

    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def load_file(self):
        '''
            Method to retun the file data as a dict
            {
                "1": {
                    "full_name" : "Jack",
                    "address":"Apt 1, pacific highway, Artarmon, NSW",
                    "phone": "+91 - 3209430001"
                },
                "2": {
                    "full_name" : "Matt",
                    "address":"Apt 2, pacific highway, Artarmon, NSW",
                    "phone": "+91 - 3209430002"
                }
            }
        '''
        pass

    @abstractmethod
    def fetch(self):
        pass