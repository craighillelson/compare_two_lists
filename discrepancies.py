"""
Compare two lists.
Output a text file with the discrepancies between the two.
"""


def import_text_file(text_file):
    return open(text_file).readlines()


def compare_sets(lst_1, lst_2):
    return set(lst_1) - set(lst_2)


def find_discrepancies():
    if DISCREPANCIES:
        discrepancies_file = open("discrepancies.txt", "w")
        for user in DISCREPANCIES:
            discrepancies_file.write(user)
        print('"discrepancies.txt" exported successfully')
    else:
        print('There are no discrepancies.')


LST1 = import_text_file("users_1.txt")
LST2 = import_text_file("users_2.txt")
LST1_LST2 = compare_sets(LST1, LST2)
LST2_LIST1 = compare_sets(LST2, LST1)
DISCREPANCIES = list(LST1_LST2) + list(LST2_LIST1)
find_discrepancies()
