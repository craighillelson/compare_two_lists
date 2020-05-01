"""Compare two lists. Output the differences between the two."""

LST1 = []
LST2 = []

def import_text_file(text_file, lst):
    """Import text file and populate a list with its contents."""
    users = open(text_file, 'r')
    users = [lst.append(email) for email in users]

# run import_text_file for both files
import_text_file('users_1.txt', LST1)
import_text_file('users_2.txt', LST2)

# find discrepancies and concatenate both lists of same
LST1_LST2 = set(LST1) - set(LST2)
LST2_LIST1 = set(LST2) - set(LST1)
DISCREPANCIES = list(LST1_LST2) + list(LST2_LIST1)

# output file
DISCREPANCIES_FILE = open('discrepancies.txt', 'w')
for user in DISCREPANCIES:
    DISCREPANCIES_FILE.write(user)

# update user
print('"discrepancies.txt" exported successfully')
