class ListOperations:
    def __init__(self):
        self._data = []

    def add_element(self, element):
        self._data.append(element)

    def remove_element(self, element):
        if element in self._data:
            self._data.remove(element)
        else:
            print("Element not found in the list.")

    def get_list(self):
        return self._data

    def sort_list(self):
        self._data.sort()

    def reverse_list(self):
        self._data.reverse()

    def clear_list(self):
        self._data.clear()

    def extend_list(self, iterable):
        self._data.extend(iterable)

# Instantiate the class
list_operations = ListOperations()

# Add elements to the list
list_operations.add_element(3)
list_operations.add_element(1)
list_operations.add_element(2)

# Get the list
print("Original list:", list_operations.get_list())

# Sort the list
list_operations.sort_list()
print("Sorted list:", list_operations.get_list())

# Reverse the list
list_operations.reverse_list()
print("Reversed list:", list_operations.get_list())

# Extend the list
list_operations.extend_list([4, 5])
print("Extended list:", list_operations.get_list())

# Remove an element
list_operations.remove_element(4)
print("List after removing element:", list_operations.get_list())

# Clear the list
list_operations.clear_list()
print("List after clearing:", list_operations.get_list())
