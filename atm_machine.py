class ATM(object):

    def __init__(self):
        self.banknotes_left = {'20':0, '50':0, '100':0, '200':0, '500':0}
         
        

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        dict_banknotes_count = {'20': banknotesCount[0], '50':banknotesCount [1], '100':banknotesCount[2], '200':banknotesCount[3], '500':banknotesCount[4]}
        
        for key in dict_banknotes_count:
            self.banknotes_left[key] += dict_banknotes_count[key]
        print("banknotes_left after a deposit: ", self.banknotes_left)

        

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        current_amount = amount
        list_to_return = {'20':0, '50':0, '100':0, '200':0, '500':0}
        var_store = self.banknotes_left
        # print("initial var store", var_store)
  

        for key in reversed(list(self.banknotes_left.keys())):
            # print(key, self.banknotes_left[key])
            denomination = int(key)
            # print("denomination: ", denomination)
            floor_div = int(current_amount//denomination)
            # print(floor_div)

            if self.banknotes_left[key]>=0:
               allowable = min(floor_div, self.banknotes_left[key])
            #    print("allowable", allowable)
               self.banknotes_left[key] -= allowable
               current_amount -= allowable * denomination
            #    print("current  amount", current_amount)
               list_to_return[key] = allowable

        
        if current_amount !=0:
            print("Result of how many banknotes denominations the machine will give me: ", '[-1]')
            # print("final var store", var_store)
            for key in list_to_return.keys():
                self.banknotes_left[key]+= list_to_return[key]
            print("banknotes_left after a withdrawal: ", self.banknotes_left)
            return [-1]
        
        else: 
            result = list(list_to_return.values())
            print("Result of how many banknotes denominations the machine will give me: ", result)
            print("banknotes_left after a withdrawal: ", self.banknotes_left)
            return result
        
        

        


# Your ATM object will be instantiated and called as such:
obj = ATM()
obj.deposit([0,0,1,2,1])
param_2 = obj.withdraw(600)
obj.deposit([0,1,0,1,1])
param_2 = obj.withdraw(600)
param_2 = obj.withdraw(550)