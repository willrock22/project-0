from model.customer import Customer
import psycopg


class CustomerDao:

    def get_all_customers(self):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="love", user="postgres",
                             password="ADad8834") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers")
                customers = []
                for customer in cur:
                    customer_id = customer[0]
                    first_name = customer[1]
                    last_name = customer[2]
                    email = customer[3]
                    c = Customer(customer_id,first_name,last_name,email)
                    customers.append(c)
                return customers

    def get_customer_by_customer_id(self,customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="love", user="postgres",
                             password="ADad8834") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers WHERE id = %s",(customer_id,))

                for customer in cur:
                    customer_id = customer[0]
                    first_name = customer[1]
                    last_name = customer[2]
                    email = customer[3]
                    return Customer(customer_id, first_name, last_name, email)


                return None

