class Customer:
    def __init__(self,cust_id,f_name,l_name,e):
        self.customer_id = cust_id
        self.first_name = f_name
        self.last_name = l_name
        self.email = e

    def to_dict(self):
        my_dict = {
            "customer_id": self.customer_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }

        return my_dict


