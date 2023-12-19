
list_numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
new_list = list(set(list_numbers))
print(new_list)

new_list2 = []
for item in list_numbers:
    if item not in new_list2:
        new_list2.append(i)
print(new_list2 )