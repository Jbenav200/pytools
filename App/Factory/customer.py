from Algorithms.bubbleSort import bubble_sort


class Customer:
    def __init__(self):
        self.data = {}
        self.key_list = list(self.data.keys())
        self.value_list = list(self.data.values())

    def get_data(self):
        self.data = {"Carpets R Us": 120000000,
                     "Textiles UK Ltd": 50000000,
                     "Rugs Wrath and Beyond": 250000000}
        return self.data

    def set_data(self, data):
        self.data = data
        print("Data has been set: ")
        for key in data:
            print(key, "-->", self.data[key])
        return self.data

    def sort_by_revenue(self, data, arr=[]):
        self.data = self.get_data()
        self.arr = arr
        for key in self.data:
            self.arr.append(self.data[key])

        self.arr = bubble_sort(self.arr)
        for i in self.arr:
            self.find_key_by_val(i)

    def find_key_by_val(self, val):
        for key, value in self.data.items():
            if val == value:
                print(key, "-->", val)

    def bubble_sort(self):
        self.arr = bubble_sort(self.arr)
        return self.arr
