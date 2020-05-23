"""Compare two lists. Write the values in both lists to a file."""


def import_text_file(text_file):
    """Import text file and throw the contents into a list."""
    lst = []
    lst = open(text_file).readlines()
    return lst


LST1 = import_text_file('users_1.txt')
LST2 = import_text_file('users_2.txt')

IN_BOTH = set(LST1) & set(LST2)

if IN_BOTH:
    IN_BOTH_FILE = open('in_both.txt', 'w')
    for user in IN_BOTH:
        IN_BOTH_FILE.write(user)
    print("'in_both.txt' exported successfully")
else:
    print('There are no items in common.')
