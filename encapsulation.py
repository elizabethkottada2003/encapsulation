class student:
    def __init__(self,name,phnum,address):
        self.name=name
        self._address=address
        self.__phnum=phnum
std1=student("elizi",612435637,"hyd")
print(std1.name)
print(std1._address)
print(std1._student__phnum)

class student:
    def __init__(self,name,phnum,address):      ##########to print private value(phnum)
        self.name=name
        self._address=address
        self.__phnum=phnum
    def details(self):
        print(f'{self.name},phn is {self.__phnum} and addrerss is {self_address}')
std1=student("elizi",612435637,"hyd")
print(std1.name)
print(std1._address)
print(std1._student__phnum)

class account:
    def __init__(self,name,num,balance):     
        self.name=name
        self._num=num
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print(f" amount {amount} have been credited to your account your current balance{self.__balance}")
    def withdraw(self,amount):
        self.__balance-=amount
        print(f" amount {amount} have been debited to yout current {self.__balance} ")
    def checkbalance(self):
        print(f" current balance {self.__balance}")
    def emi(self,amount):
        self.__balance-=amount
        print(f"your emi amount {amount} and current balance is {self.__balance}")
customer1=account("elizi",132435,2000)
# print(customer1.__balance)
customer1.checkbalance()
customer1.deposit(200)
customer1.withdraw(50)
customer1.emi(100)
customer1.checkbalance()

class report:
    def __init__(self,name,sclass,marks):
        self.name=name
        self._sclass=sclass
        self.__marks=marks
    def python(self,total):
        self.__marks=total
        print(f"your marks in this subject {total} outoff {self.__marks}")
    def totalmarks(self):
        print(f"total marks {self.__marks} ")
streport=report("elizi","betch-1st-year",80)
print(streport.name)
print(streport._sclass)
streport.totalmarks()
print(streport.__marks)

class Email:
    def __init__(self,mail,password):
        self.mail=mail
        self.__password=password
    def emailid(self,authen):
        if "@" in authen:
            self.mail==authen
            print("your email id and password ")
    def password(self):
        return self.__password
edetail=Email("elizi@gmail.com","password is elizi!2003")
print(edetail.mail)
print(edetail.password())
edetail.emailid("eli@gmail.com")



