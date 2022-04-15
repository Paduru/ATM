class ATM(object):
    def __init__(self, card_num, pin_num):
        self.card_num = card_num
        self.pin_num = pin_num

    def CashWithdrawal(self, amt):
        print("$" + str(amt) + " withdrawed from account")

    def CashDeposit(self, amt):
        print("$" + str(amt) + " deposited from account")

    def GiveInformation(self):
        print("Card number: " + self.card_num)
        print("Pin number: " + self.pin_num)


Machine = ATM("3298 2389 2383", "2384")

Machine.CashDeposit(35)
Machine.CashWithdrawal(35)
Machine.GiveInformation()
