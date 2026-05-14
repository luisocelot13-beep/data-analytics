cust_list = []


class RewardsProgram:
    """"rewards for specific programs"""
    def __init__(self,cust_name,phone,email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        print(f'Name: {self.cust_name}\n'
              f'Phone: {self.phone}\n'
              f'Email: {self.email}')
    def Thank_you(self):
        print(f'thank you,{self.cust_name}, for visiting our restaurant')
    def add_to_cust_list(self):
      cust_list.append((self.cust_name,self.phone,self.email))
      print(f'New cust list update:{cust_list}')

cust_1 = RewardsProgram('Luis','6658559474','luis@gmail.com')
cust_2 = RewardsProgram('Bryan','8874774125','Bryan@gmail.com')

cust_1.profile()
cust_1.Thank_you()
cust_1.add_to_cust_list()
print()
cust_2.profile()
cust_2.Thank_you()
cust_2.add_to_cust_list()