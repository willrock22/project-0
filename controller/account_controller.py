# from flask import Blueprint, request
# from service.customer_service import CustomerService
# from exception.customer_not_found_error import CustomerNotFoundError
#
# cc = Blueprint('customer_controller', __name__)
# customer_service = CustomerService()
#
# @cc.route('/test')
# def test():
#     return "test"
#
# @cc.route('/customers')
# def get_all_customers():
#     return customer_service.get_all_customers(), 200
#
#
# @cc.route('/customers/<customer_id>')
# def get_customer_by_customer_id(customer_id): # wrap return into try / except block
#     try:
#         return customer_service.get_customer_by_customer_id(customer_id), 200
#
#     except CustomerNotFoundError as e:
#
#         return {
#                     "message": str (e)
#                 }, 404