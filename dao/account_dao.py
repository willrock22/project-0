# class AccountDao:
#
#     def get_all_accounts(self):
#         with psycopg.connect(host="127.0.0.1", port="5432", dbname="love", user="postgres",
#                              password="ADad8834") as conn:
#             with conn.cursor() as cur:
#                 cur.execute("SELECT * FROM accounts")
#                 accounts = []
#                 for account in cur:
#                     account_id = account[0]
#                     balance = account[1]
#                     customer_id = account[2]
#                     account_type = account[3]
#                     a = Account(account_id,balance,customer_id,account_type)
#                     accounts.append(a)
#                 return accounts
#
#     def get_account_by_account_id(self,account_id,balance,customer_id,account_type):
#         with psycopg.connect(host="127.0.0.1", port="5432", dbname="love", user="postgres",
#                              password="ADad8834") as conn:
#             with conn.cursor() as cur:
#                 cur.execute("SELECT * FROM accounts WHERE id = %s",(account_id,))
#
#                 for account in cur:
#                     customer_id = account[0]
#                     first_name = account[1]
#                     last_name = account[2]
#                     email = account[3]
#                     a = Account(account_id,balance,customer_id,account_type)
#
#                 return a