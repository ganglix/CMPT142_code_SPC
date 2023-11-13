# Exercise 2

# Suppose we have dictionary availability:
# keys: friend’s name
# values: list of days they are available to play a game
# (a) Write a function that accepts an availability dictionary and returns a new dictionary mapping days to
# friends who can play that day.
# (b) Using the function from a):
# Find the day most friends can attend to play the game
# List who can and can not attend the session that day

availability = {"Neo": ["Monday"],
                "Morpheus": ["Sunday"],
                "Smith": ["Monday", "Tuesday"]}

def reverse_dict(avail):
    # avail name: list of days
    schedule = {}  # day: list of names
    for name in avail:
        days = avail[name]
        for day in days:
            if day not in schedule:
                schedule[day] = []   # initialize [] when day is first time seen
            schedule[day].append(name)

    return schedule

week_schedule = reverse_dict(availability)

# Find the day most friends can attend to play the game
# initialize value and update later
day_with_most_friends = ''
number_of_most_friends = 0

for day in week_schedule:
    if len(week_schedule[day]) > number_of_most_friends:
        number_of_most_friends = len(week_schedule[day])
        day_with_most_friends = day

attend = week_schedule[day_with_most_friends]

# who is not attend
not_attend = [name for name in availability if name not in attend]
print(not_attend)