class CustomerManager:
    def __init__(self, customers):
        self.customers = customers

    def display_customers(self):
        """Displays all customer records."""
        for cust_id, details in self.customers.items():
            print(
                f"ID: {cust_id} | Name: {details['name']} | Location: {details['location']} | Purchases: {details['purchases']}"
            )

    def filter_customers_by_city(self, city):
        """Placeholder for filtering customers (students will implement)."""
        filtered_customers = {
            cust_id: details
            for cust_id, details in self.customers.items()
            if details["location"].lower() == city.lower()
        }

        if filtered_customers:
            print(f"Customers in {city}:")
            CustomerManager.display_customers(CustomerManager(filtered_customers))
        else:
            print(f"There are not customers in {city}")

    def get_unique_locations(self):
        """Placeholder for retrieving unique locations (students will implement)."""
        customer_locations = {
            customer["location"] for customer in self.customers.values()
        }
        if customer_locations:
            print("\nUnique customer locations:", customer_locations)
