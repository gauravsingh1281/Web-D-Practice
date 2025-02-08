# WAP to create a function that takes two lists of names as parameters and returns true if they have at least one name in common.
def checkCommonName(list1, list2):
    result = False
    for name1 in list1:
        for name2 in list2:
            if name1 == name2:
                result = True
    return result


list1 = ["Alice", "Bob", "Charlie"]
list2 = ["David", "Eve", "Charlie"]
if checkCommonName(list1, list2):
    print("The lists have at least one name in common.")
else:
    print("The lists do not have any names in common.")
