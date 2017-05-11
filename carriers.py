

carrier_list = []

class Carrier:
    def __init__(self, name, paper=None):
        self.name = name
        self.paper = []
        
    def __str__(self):
        return('{}\nDelivers: {}\n____________'.format(self.name, self.paper))
        
        
    def add_to_vendor(self, vendor):
        self.paper.append(vendor)
    
    def delete_instance(self):
        pass
    
    __repr__ = __str__
        

#Test Case
#Echo = Carrier('Echo')
#Echo.add_to_vendor('Canusa')
#print(Echo)
