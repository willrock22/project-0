from flask import Blueprint, request
from service.customer_service import CustomerService

cc = Blueprint('customer_controller', __name__)
customer_service = CustomerService()

@cc.route('/test')
def test():
    return "test"

@cc.route('/customers')
def get_all_customers():
    return customer_service.get_all_customers(), 200