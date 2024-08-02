import phonenumbers


def lookup_number(number):
    parsed_number = phonenumbers.parse(number)
    if phonenumbers.is_valid_number(parsed_number):
        country_code = parsed_number.country_code
        formatted_number = phonenumbers.format_number(
            parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
        return country_code, formatted_number
    return None, None


if __name__ == "__main__":
    number = input("Enter a phone number: ")
    country_code, formatted_number = lookup_number(number)
    if country_code and formatted_number:
        print(
            f"The number is valid. Country code: {country_code}, Formatted number: {formatted_number}"
        )
    else:
        print("The number is not valid.")
