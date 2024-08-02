import phonenumbers


def lookup_number(number):
    parsed_number = phonenumbers.parse(number)
    return phonenumbers.is_valid_number(parsed_number)


if __name__ == "__main__":
    number = input("Enter a phone number: ")
    if lookup_number(number):
        print("The number is valid.")
    else:
        print("The number is not valid.")
