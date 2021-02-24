from Factory import customer
# set data


if __name__ == "__main__":
    cust = customer.Customer()
    data = cust.get_data()
    sorted_data = cust.sort_by_revenue(cust.data)
    print("in order of SLA the accounts are: \n\n")
    cust.print_data(cust.print_data_sla(cust.data))
