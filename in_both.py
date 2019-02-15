""" __doc__ """

LST1 = []
LST2 = []

def import_text_file(text_file, lst):
    """ import text file and throw the contents into a list """
    users = open(text_file, "r")
    users = [lst.append(email) for email in users]

# import text
import_text_file('users_1.txt', LST1)
import_text_file('users_2.txt', LST2)

# find values in both lists
IN_BOTH = set(LST1) & set(LST2)

# output file
IN_BOTH_FILE = open("in_both.txt", "w")
for user in IN_BOTH:
    IN_BOTH_FILE.write(user)

# update user
print("'in_both.txt' exported successfully")
