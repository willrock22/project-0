from dao.customer_dao import CustomerDao
from exception.customer_not_found_error import CustomerNotFoundError


class CustomerService:

    def __init__(self):
        self.customer_dao = CustomerDao()

    def get_all_customers(self):
        customers = self.customer_dao.get_all_customers()
        dict = {"customers": []}
        for cust in customers:
            dict["customers"].append(cust.to_dict())
        return dict

    def get_customer_by_customer_id(self, customer_id):
        user = self.customer_dao.get_customer_by_customer_id(customer_id)

        if user:
            return user.to_dict()
        else:
            raise CustomerNotFoundError("Customer not found")


        return  user.to_dict()