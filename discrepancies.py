"""
Compare two lists.
Output a text file with the discrepancies between the two.
"""


def import_text_file(text_file):
    """Import a text file and populate a list with its contents."""
    lst = []
    return open(text_file).readlines()


def compare_sets(a, b):
    """Compare sets."""
    return set(a) - set(b)


def find_discrepancies():
    """Write discrepancies to a text file."""
    if DISCREPANCIES:
        DISCREPANCIES_FILE = open('discrepancies.txt', 'w')
        for user in DISCREPANCIES:
            DISCREPANCIES_FILE.write(user)
        print('"discrepancies.txt" exported successfully')
    else:
        print('There are no discrepancies.')


LST1 = import_text_file('users_1.txt')
LST2 = import_text_file('users_2.txt')
LST1_LST2 = compare_sets(LST1, LST2)
LST2_LIST1 = compare_sets(LST2, LST1)
DISCREPANCIES = list(LST1_LST2) + list(LST2_LIST1)
find_discrepancies()
