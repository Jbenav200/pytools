from Algorithms.bubbleSort import bubble_sort


class Customer:
    # Initialise the customer object
    def __init__(self):
        self.data = {}
        self.key_list = list(self.data.keys())
        self.value_list = list(self.data.values())

    # Get the preset data in the form of a dictionary.
    def get_data(self):
        self.data = {"Carpets R Us": 120000000,
                     "Textiles UK Ltd": 50000000,
                     "Rugs Wrath and Beyond": 250000000}
        return self.data

    # Set the data property
    def set_data(self, data):
        self.data = data
        print("Data has been set: ")
        for key in data:
            print(key, "-->", self.data[key])
        return self.data

    # Using a bubble sort algorithm to sort by revenue
    def sort_by_revenue(self, data, arr=[]):

        # define the data
        self.data = self.get_data()
        # create an empty array
        self.arr = arr
        # For each key in the data, i.e. "Carpets R Us"
        for key in self.data:
            # add the value to the array
            self.arr.append(self.data[key])

        # Using bubble sort, I order the array of values, in order of lowest to highest.
        self.arr = bubble_sort(self.arr)
        # For each value in the array I call the find_key_by_val method, passing the value as a parameter.
        for i in self.arr:
            self.find_key_by_val(i)

    # This function takes a value and checks it against the items in self.data values
    # And if the value is identical to a value in the data values
    # it prints the key and the value together formatteds with an arrow pointing right to left.
    def find_key_by_val(self, val):
        for key, value in self.data.items():
            if val == value:
                print(key, "-->", val)

    # This function calls the bubble sort algorithm and returns a sorted array
    # in place of the array it was given
    def bubble_sort(self):
        self.arr = bubble_sort(self.arr)
        return self.arr
