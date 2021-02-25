from Factory import customer
# set data


if __name__ == "__main__":
    cust = customer.Customer()
    data = cust.get_data()
    sorted_data = cust.sort_by_revenue(cust.data)
    print('\n\n')
    print("In order of annual revenue the accounts low to high are:")
    cust.print_data(sorted_data)
    print('\n')
    print("In order of SLA the accounts are: ")
    cust.print_data_sla()
    print('\n\n\n')
