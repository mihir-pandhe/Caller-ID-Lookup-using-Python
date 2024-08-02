import phonenumbers
from phonenumbers import geocoder, carrier


def lookup_number(number):
    parsed_number = phonenumbers.parse(number)
    if phonenumbers.is_valid_number(parsed_number):
        country_code = parsed_number.country_code
        formatted_number = phonenumbers.format_number(
            parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
        location = geocoder.description_for_number(parsed_number, "en")
        carrier_name = carrier.name_for_number(parsed_number, "en")
        return country_code, formatted_number, location, carrier_name
    return None, None, None, None


if __name__ == "__main__":
    number = input("Enter a phone number: ")
    country_code, formatted_number, location, carrier_name = lookup_number(number)
    if country_code and formatted_number:
        print(f"The number is valid. Country code: {country_code}")
        print(f"Formatted number: {formatted_number}")
        print(f"Location: {location}")
        print(f"Carrier: {carrier_name}")
    else:
        print("The number is not valid.")
