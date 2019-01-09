""" __doc__ """

LST1 = []
LST2 = []

def import_text_file(text_file, lst):
    """ import text file and throw the contents into a list """
    users = open(text_file, "r")
    for email in users:
        lst.append(email)
    return lst

import_text_file('users_1.txt', LST1)
import_text_file('users_2.txt', LST2)

IN_BOTH = set(LST1) & set(LST2)

# for user in IN_BOTH:
	# print user

IN_BOTH_FILE = open("in_both.txt", "w")
for user in IN_BOTH:
    IN_BOTH_FILE.write(user)

# update user
print "'in_both.txt' exported successfully"
