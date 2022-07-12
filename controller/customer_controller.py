from flask import Blueprint, request


cc = Blueprint('customer_controller', __name__)

@cc.route('/test')
def test():
    return "test"

@cc.route('/customers')
def get_all_customers():
    return