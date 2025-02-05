def find_common_elements(list1, list2):
    """Function to find common elements between two lists."""
    return list(set(list1) & set(list2))

# Example usage
list1 = input("Enter the first list of elements separated by spaces: ").split()
list2 = input("Enter the second list of elements separated by spaces: ").split()

common_elements = find_common_elements(list1, list2)
print("Common elements:", common_elements)