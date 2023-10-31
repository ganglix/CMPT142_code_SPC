# List msgs contains sublists of the form [msg,days old]:
# msgs = [ ["Forgot the recipe again! #nofood",3],
# ["such a gluten #food #fivestar",10] ]
# Use list comprehensions to:
# (a) create list food_msgs of messages containing "#food"
# (b) create a new copy of food_msgs where messages are
# appended with "#yawn"

# Topic : List Comprehensions
# DEMO
# list of social media messages as sublists ( message , days since posted )

msgs = [["Forgot the recipe again! #nofood", 3],
        ["such a gluten #food #fivestar", 10],
        ["International #Food day! Hooray!", 1],
        ["Apple pie is bestest food", 5],
        ["lunchtime? #food #craving hits again", 9]]

# (a) create list food_msgs of messages containing "#food"

# list comprehension
# [item_to_put_in_the_new_list for iterator in sequence]
# [item_to_put_in_the_new_list for iterator in sequence if condition]

food_msgs = [m for m in msgs if "#food" in m[0].lower()]   # m is the msg sublist
print(food_msgs)

# # for loop
# food_msgs=[]
# for m in msgs:
#     if "#food" in m[0].lower():
#         food_msgs.append(m)


# (b) create a new copy of food_msgs where messages are
# appended with "#yawn" to the message

food_msgs_yawn = [[ m[0]+" #yawn" , m[1] ]  for m in food_msgs]

print(food_msgs_yawn)