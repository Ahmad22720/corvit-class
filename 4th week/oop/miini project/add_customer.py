from customer import Customer


def add_customer(service):
    customer_id = input('Enter new customer id :').strip()
    name = input('Enter customer name :').strip()

    if not customer_id or not name:
        print('Customer id and name are required.')
        return

    for c in service.customers:
        if c.customer_id == customer_id:
            print('Customer id already exists.')
            return

    service.register_customer(Customer(customer_id, name))
    print('Customer added successfully.')

