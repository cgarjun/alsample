import json
from base_driver import BaseDriver
from personal_schema import Contact

class Driver(BaseDriver):
    def __init__(self, file_path):
        super(Driver, self).__init__(file_path)

    def load_file(self):
        json_data = None
        with open(self.file_path, 'r') as outfile:
            json_data = json.load(outfile)
        return json_data

    def fetch(self):
        data = self.load_file()
        schema_list =[Contact(i, **data[i]) for i in data]
        return sorted(schema_list, key=lambda x : x.index)
