# dictionary

# KEYS

# VALUES

phone_book = {'Gang': "3068888888",
              'Gang1': "3061111111"}

print(phone_book)

# my_dict = {1 : [1,2,3,4]}
# print(my_dict[1])


contact = {'Gang': {'email': 'gang.li@usask.ca',
                    'phone': "3068888888"},
           'Justin': {'phone': "3061111111"}
           }
print(contact['Gang']['email'])

# keys should be unique and immutable
# contact = {0: {'name':'Gang',
#      'phone': '306111111',
#      'address': 'college drive'},
# 1: {},
# 2: {}}

# add James to contact
contact['James'] = {'phone':'3065555555'}  # works when assigning a value to  "James"

print(contact)

# Whatever you do to a dictionary, you do it through keys
# for k in contact:
#     print(k)

print("Dima" in contact)  # checking if 'Dima' is one of keys in conact
if "Dima" in contact:
    print(contact['Dima'])

print(contact.get("Dima", "key is not found"))

