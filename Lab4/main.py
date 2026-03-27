number_of_user = int(input("Enter number of users: "))

users = dict()

for i in range(number_of_user):
    name = input("Enter username: ")
    item_number = int(input("How many items? "))
    list_of_items = list()
    for j in range(item_number):
        item_name = input(f"Item {j+1}: ")
        list_of_items.append(item_name)
    users[name] = list_of_items
    print("")

print("USER DATA:")
for user in users:
    print(user, "->", users[user])

itemsDic = dict()

for items in users.values():
    uniques = set(items)
    for item in uniques:
        if item in itemsDic:
            itemsDic[item] += 1
        else:
            itemsDic[item] = 1


print("\nCOMMON ITEMS:")
for item in itemsDic:
    if itemsDic[item] > 1:
        print(item)


print("\nUNIQUE ITEMS:")
for item in itemsDic:
    if itemsDic[item] == 1:
        print(item)

maxOccurence = 0
for item in itemsDic:
    if itemsDic[item] > maxOccurence:
        most_pop = item
        maxOccurence = itemsDic[item]

print("\nMOST POPULAR ITEM:")
print(most_pop)

