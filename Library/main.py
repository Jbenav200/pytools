from Factory import customer
# set data


if __name__ == "__main__":
    cust = customer.Customer()
    data = cust.get_data()
    sorted_data = cust.sort_by_revenue(data)
