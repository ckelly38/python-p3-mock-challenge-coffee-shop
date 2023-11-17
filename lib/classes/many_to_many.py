def isNumType(val):
    return (type(val) == int or type(val) == float);

#minimum length is inclusive max length is exclusive except when maxlen is 0 then the minlen must be 0
def isNumInRangeValid(strlen, minvlen=0, maxlen=-1, incmax=False):
    if (isNumType(strlen) and isNumType(minvlen) and isNumType(maxlen)):
        if (minvlen < 0): raise Exception("invalid minimum length given!");
        elif (maxlen < -1): raise Exception("invalid maximum length given!");
        if (incmax == True or incmax == False): pass;
        else: raise Exception("the include max value must be a boolean!");
        if (maxlen == -1): return (minvlen < strlen or minvlen == strlen);
        elif (maxlen == 0):
            if (minvlen > 0): raise Exception("invalid combination of minimum and maximum lengths given!");
            else: return True;
        else: return ((minvlen < strlen or minvlen == strlen) and
                      ((strlen < maxlen) or (strlen == maxlen and incmax)));
    else: raise Exception("the inputs must be numbers");

#print(isNumInRangeValid(2.0, 1, 10, False));
#print(isNumInRangeValid(2.0, 1, 10, True));

class Coffee:
    def __init__(self, name):
        self.__ininit = True;
        self.setName(name);
        self.__ininit = False;
    
    def getName(self): return self._name;

    def setName(self, val):
        if (type(val) == str and isNumInRangeValid(len(val), 3, -1, False)):
            if (self.__ininit): self._name = "" + val;
            else: raise Exception("cannot change the name outside of init!");
        else: raise Exception("name must be a string with at least 3 characters!");

    name = property(getName, setName);

    def orders(self):
        return [ordr for ordr in Order.all if ordr.coffee == self];
    
    def all_customers(self):
        return [ordr.customer for ordr in self.orders()];

    def customers(self):
        return list(set(self.all_customers()));
    
    def num_orders(self):
        return len(self.orders());
    
    def average_price(self):
        prices = [ordr.price for ordr in self.orders()];
        return sum(prices)/float(len(prices));

class Customer:
    def __init__(self, name):
        self.setName(name);
    
    def getName(self): return self._name;

    def setName(self, val):
        if (type(val) == str and isNumInRangeValid(len(val), 1, 16, False)):
            self._name = "" + val;
        else: raise Exception("name must be a string with between 1 and 15 characters inclusive!");

    name = property(getName, setName);
        
    def orders(self):
        return [ordr for ordr in Order.all if ordr.customer == self];
    
    def all_coffees(self):
        return [ordr.coffee for ordr in self.orders()];

    def coffees(self):
        return list(set(self.all_coffees()));
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price);

    @classmethod
    def maxindx(cls, arr):
        maxval = max(arr);
        maxindxs = [i for i in range(len(arr)) if arr[i] == maxval];
        return maxindxs[0];

    @classmethod
    def didIGetCoffee(cls, crdr, cfe, cmr):
        return (crdr.customer == cmr and crdr.coffee == cfe);

    @classmethod
    def most_aficionado(cls, coffee):
        #get all the orders for the coffee
        #how much has a customer paid for it
        #get the price paid for by each customer...
        #get the list of unique customers for it...
        crdrs = coffee.orders();
        ccus = coffee.customers();
        if (len(ccus) < 1): return None;
        elif (len(ccus) == 1): return ccus[0];
        ppbc = [sum([cor.price for cor in crdrs if cls.didIGetCoffee(cor, coffee, c)]) for c in ccus];
        #print(ppbc);
        return ccus[cls.maxindx(ppbc)];
    
class Order:
    all = [];

    def __init__(self, customer, coffee, price):
        self.__ininit = True;
        self.setCustomer(customer);
        self.setCoffee(coffee);
        self.setPrice(price);
        self.__ininit = False;
        Order.all.append(self);
    
    def getPrice(self): return self._price;

    def setPrice(self, val):
        if (isNumInRangeValid(val, 1, 10, True)):
            if (self.__ininit): self._price = val;
            else: raise Exception("price cannot change!");
        else: raise Exception("price must be between 1 and 10 inclusive!");

    price = property(getPrice, setPrice);

    def getCustomer(self): return self._customer;

    def setCustomer(self, val):
        if (type(val) == Customer):
            if (self.__ininit): self._customer = val;
            else: raise Exception("customer cannot change!");
        else: raise Exception("customer must be a Customer type!");

    customer = property(getCustomer, setCustomer);

    def getCoffee(self): return self._coffee;

    def setCoffee(self, val):
        if (type(val) == Coffee):
            if (self.__ininit): self._coffee = val;
            else: raise Exception("coffee cannot change!");
        else: raise Exception("coffee must be a Coffee type!");

    coffee = property(getCoffee, setCoffee);
