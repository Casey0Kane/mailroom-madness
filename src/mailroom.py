"""Pseudo code for mailroom madness project 401 python."""

import sys
import io
DATABASE = {}


def initial_prompt():
    """Prompt the user to send a Thank you or Create a report."""
    choice = input("Send a (T)hank You Note or (C)reate a Report, or (Q)uit: ")
    return choice


def initialize_dictionary():
    """Open database file call donators.txt and construct the dictionary."""
    f = io.open("donators.txt", "r")
    for word in list(f.readline().split(',')):
        if not word.isnumeric():
            key = word.lower()
            amount_list = []
        else:
            amount_list.append(int(word))
        DATABASE[key] = amount_list
    f.close()
    print("dictionary is : ", DATABASE)  # for debugging purpose


def quit_prompt():
    """Prompt user to quit or restart from the beginning."""
    choice = input("Go back to the (T)op Menu or (K)eep going")
    return choice


def donor_name_list():
    """Prompt user to enter a name or view the donor list."""
    choice = input("Please enter a name to add a donor or 'list' to list existing donors.")
    return choice


def list_of_donors():
    """Print a list of donors."""
    for name in DATABASE:
        print(name)


def sum_donations(name):
    """Add all the donations for a particular individual."""
    total = 0
    for n in range(len(DATABASE[name])):
        total = total + float(DATABASE[name][n])
    return total


def get_max_key_val(dict_obj):
    """Get the key with max sum of values."""
    max_key = next(iter(dict_obj))
    for n in dict_obj:
        if sum_donations(n) > sum_donations(max_key):
            max_key = n
    return max_key


def create_report():
    """Print list of donor names and amount donated."""
    temp_dict = dict(DATABASE)
    print("{:<15}{:<18}{:<18}{:<15}".format('Name', 'Sum of Donations', 'Times Donated', 'Average Donation'))
    for n in range(len(DATABASE)):
        key = get_max_key_val(temp_dict)
        print("{:<15}{:<18.2f}{:<18d}{:<15.2f}".format(key, sum_donations(key), len(DATABASE[key]), sum_donations(key) / len(DATABASE[key])))
        del temp_dict[key]


def donation():
    """Prompt the user for a valid value to donate."""
    amount = input("Please input a dollar amount to be added to the Donator's history : ")
    return amount


def update_donation(name, amount):
    """Update donation value and save it to text file."""
    DATABASE[name].append(float(amount))


def create_text_file():
    """Write list of donors to text file named output.txt."""
    output_file = open("output.txt", "w")
    first_key = True
    for key, val in DATABASE.items():
        if first_key:
            output_file.write(key)
        else:
            output_file.write("," + key)
        for x in val:
            output_file.write("," + str(x))
        first_key = False
    output_file.close()


def create_email(name):
    """Send thank you email to donor."""
    """This will print email to screen then user can just print-screen."""
    last_donation = DATABASE[name][len(DATABASE[name]) - 1]
    print("Dear {0},\n\n        Thank you so much for donating to our ch\
arity with an amount of {1}.\n\n        Your support is very much apprec\
iated.  We look forward to your support in 2018.\n\n\n\
                                                              Regards,\n\
                                                              John Doe\n\
                                         Community Support Coordinator\
    ".format(name, last_donation))


def main():
    """Main program."""
    initialize_dictionary()
    create_report()
    # choice = initial_prompt().lower()
    # while choice != "q":
    #     if choice == 't':
    #         list_of_donors()
    #         DATABASE[input("Please type a donor name: ")].append(float(input("Please enter a dollar amount: ")))
    #     elif choice == 'c':
    #         print('it"s a C')
    #     else:
    #         if choice == 'q':
    #             sys.exit()
    #     choice = initial_prompt().lower()


if __name__ == "__main__":
    """Handle console user input"""
    main()
