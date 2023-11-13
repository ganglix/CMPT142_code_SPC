# Suppose you have a dictionary of survey responses:
# •keys are student names
# •values are favourite ice cream flavours (one of
# "chocolate", "vanilla", "strawberry")
# Write a function that takes a dictionary of survey responses
# and returns a new dictionary where:
# •keys are ice cream flavours
# •values are number of students with that favourite flavour

survey = {"Sam": "chocolate",
          "Chase": "vanilla",
          "Uday": "vanilla",
          "James": "vanilla",
          "Brayden": "chocolate",
          "Toryn": "chocolate",
          "Lyndon": "strawberry",
          "Dima": "vanilla",
          "Justin": "vanilla",
          "Gang": "strawberry"}

def icecream_survey(survey):
    """takes a dictionary of survey responses and
    returns a new dictionary where: keys are ice cream flavours
    values are number of students with that favourite flavour

    :param survey: dict, survey record, name:flavour
    :return: dict, survey result, flavour: number of votes
    """
    result = {}    # flavour: number of votes

    for name in survey:  # name:flavour
        flavour = survey[name]
        if flavour not in result:  # check if flavour is one of the keys in result
            result[flavour] = 0    # flavour is first seen, initialize a value, to be added later
        result[flavour] += 1

    return result
print(icecream_survey(survey))