class Account:
    def __init__(self,acct_id,bal,cust,acct_type):
        self.account_id = acct_id
        self.balance = bal
        self.customer_id = cust
        self.account_type_id = acct_type

    def to_dict(self):
        my_dict = {
            "account_id": self.account_id,
            "balance": self.balance,
            "customer_id": self.customer_id,
            "account_type_id": self.account_type_id
        }

        return my_dict