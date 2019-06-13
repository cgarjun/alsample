import xml.etree.ElementTree as etree
from base_driver import BaseDriver
from personal_schema import Contact

class Driver(BaseDriver):
    def __init__(self, file_path):
        super(Driver, self).__init__(file_path)

    def load_file(self):
        json_data = {}
        xmlroot = etree.parse(self.file_path).getroot()

        for index in xmlroot:
            contact_data = {}
            for child in index.getchildren():
                contact_data[child.tag] = child.text
            json_data[index.attrib['name']]=contact_data
        return json_data

    def fetch(self):
        data = self.load_file()
        schema_list =[Contact(i, **data[i]) for i in data]
        return sorted(schema_list, key=lambda x : x.index)
