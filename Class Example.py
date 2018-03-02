#Pratik Prabhakar
#117220752

'''CreditCard class definition which gives the following pieces of information as getter methods:
(i) the name of the customer,
(ii) the name of the bank,
(iii) the account identifier,
(iv) the credit card limit
(v) the balance (in euros).

Also there are other three methods:
1) charge (which calculates charge for the card)
2) make_payment (which calculates balance after payment of credit)
3) show_summary (A static method which shows customer's name, balance and account ID) sorted by name.
'''
class CreditCard:

    #List containing details of all credit cards
    all_credit_cards = []
    
    #Common base classes for all Credit card holders
    def __init__(self, cst_name, bank_name, account_id, limit, balance):
        self.__cst_name = cst_name
        self.__bank_name = bank_name
        self.__account_id = account_id
        self.__limit = limit
        self.__balance = balance
        CreditCard.all_credit_cards.append(self)

    #Get the customer's name
    def get_customerName(self):
        return "Account Holder Name: ", self.__cst_name

    #Get the customer's bank name
    def get_bankName(self):
        return "Bank Name: ", self.__bank_name

    #Get the customer's account id
    def get_accountId(self):
        return "Account Number: ", self.__account_id

    #Get the customer's limit amount
    def get_limit(self):
        return "Card Limit: €", self.__limit

    #Get the customer card's balance
    def get_balance(self):
        return "Balance: €", self.__balance

    #Functions that calculate charges for the given price to the card, assuming sufficient credit limit.
    def charge(self, price):
        if price < self.__balance:
            self.__balance = self.__balance - price
            return True
        else:
            print("Sorry, you don't have enough balance to make purchase")
            return False
        
    #Function to process customer payment by reducing balance by amount and return the remaining balance
    def make_payment(self, amount):

        self.__balance = self.__balance + amount
        #self.__limit = self.__limit + amount
        return "The remaining balance in the card is €", self.__balance

    #Static function that show the list of all credit card holders sorted by name
    def show_summary():
        cards = sorted(CreditCard.all_credit_cards,
                       key=lambda creditcard: creditcard.__cst_name,
                       reverse=False)
        for cc in cards:
            #print(cc.get_customerName(), cc.get_accountId(), cc.get_balance())
            print ("Customer Name:",cc.__cst_name,
                   ", Balance: €", cc.__balance,
                   ", Account ID:", cc.__account_id,
                   ", Limit: €", cc.__limit)


'''PriorityQueue class is a container that holds a collection of key-value pairs known as items.
Keys need not be distinct. Priority queue objects support the following functions along with following operations:
1) Add elements to the queue.
2) Get the length of the queue.
3) Check whether the queue is empty.
4) Get the minimum elements from the queue.
5) Remove the elements from the queue based on minimum key.
'''

class PriorityQueue:

    #Dictionary initialisation for keeping track of the elements in queue
    items = {}

    #Common base classes for all Priority Queue
    def __init__(self, element):
        self.__element = element

    #Adding elements to the queue with keys.
    def add_element(self, k, v):
        val = []
        if k in self.items:
            val = self.items[k]
            val.append(v)
            self.items[k] = val
        else:
            val.append(v)
            self.items[k] = val
            
    #Get the length of the queue
    def length(self):
        return len(self.items)
    
    #Check whether the queue is empty.
    def check_empty(self):
        if not self.items:
            return True
        else:
            return False

    #Get the elements based on the minimum key
    def minimum_element(self):
        minimum = 0
        value = 0
        if len(self.items) != 0:
            minimum = min(self.items.keys())
            value = self.items[minimum]
            return minimum , value
        else:
            return "Sorry the queue is empty"

    #Remove the elements based on the minimum key.    
    def remove_element(self):
        minimum_key = 0
        #minimum_value = 0
        if len(self.items) > 0:
            for key in self.items:
                minimum_key = min(self.items.keys())
                #minimum_value = min(self.items[minimum_key])
            return minimum_key, self.items.pop(minimum_key)
        else:
            print("Sorry, you don't have any elements in the queue")
            return False
