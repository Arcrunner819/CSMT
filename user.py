from carriers import *

class User():
    def __init__(self, name):
        self.name = name
        
    def create_carrier(self):
        continue_to_add = True
        while continue_to_add:
            carrier_name = input('Please enter the carrier name you wish to add >> ')
            carrier_name = Carrier(carrier_name)
            create_vendor = input('Do you wish to assign a vendor to {} at this time? \'y\' or \'n\' >>'.format(carrier_name.name))
            if create_vendor == 'y':
                carrier_vendor = input('Please enter the vendor this carrier delivers >> ')
                carrier_name.add_to_vendor(carrier_vendor)
            
            carrier_list.append(carrier_name)
            print('\nYou have created {}'.format(carrier_name))
                        
            add_or_no = input('Do you wish to enter more carriers? \'y\' or \'n\' >> ')
            
            if add_or_no == 'n':
                continue_to_add = False
                print('\n')
        
        for carrier_name in carrier_list:
            print(carrier_name)
        
    def delete_carrier(self):
        print(carrier_list)
        to_delete = input('Which carrier would you like to remove?\n>> ')
        for carrier in carrier_list:
            try:
                if to_delete in carrier_list:
                    carrier_list.remove(to_delete)
            except ValueError:
                pass
        print("Here is the updated list:")
        
                  
    
    
    def __str__(self):
        return "Current user is {}".format(self.name)
        
#Test Case
Jordan = User('Jordan')
print(Jordan)
 
Jordan.create_carrier()
Jordan.delete_carrier()
 
    
