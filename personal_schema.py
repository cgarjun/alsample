class Contact(object):
    '''
    '''
    def __init__(self, index, **contact_info):
        self.index = index
        self.full_name = None
        self.address = None
        self.phone = None
        self.__dict__.update(**contact_info)

    def display(self):
        print("Sl No: {0}".format(self.index))
        print("Full Name: {0}".format(self.full_name))
        print("Address: {0}".format(self.address))
        print("Phone: {0}".format(self.phone))
        print("------------------------------------------------------------------")