from dao.customer_dao import CustomerDao



class CustomerService:

    def __init__(self):
        self.customer_dao = CustomerDao()

    def get_all_customers(self):
        customers = self.customer_dao.get_all_customers()
        dict = {"customers": []}
        for cust in customers:
            dict["customers"].append(cust.to_dict())
        return dict
