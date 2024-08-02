import phonenumbers
from phonenumbers import geocoder, carrier, timezone


def lookup_number(number):
    try:
        parsed_number = phonenumbers.parse(number)
        if phonenumbers.is_valid_number(parsed_number):
            country_code = parsed_number.country_code
            formatted_number = phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
            location = geocoder.description_for_number(parsed_number, "en")
            carrier_name = carrier.name_for_number(parsed_number, "en")
            time_zones = timezone.time_zones_for_number(parsed_number)
            return country_code, formatted_number, location, carrier_name, time_zones
        else:
            raise ValueError("Invalid phone number")
    except phonenumbers.NumberParseException as e:
        print(f"Error: {e}")
    return None, None, None, None, None


if __name__ == "__main__":
    number = input("Enter a phone number: ")
    country_code, formatted_number, location, carrier_name, time_zones = lookup_number(
        number
    )
    if country_code and formatted_number:
        print(
            f"Number Details:\nCountry code: {country_code}\nFormatted number: {formatted_number}"
        )
        print(
            f"Location: {location}\nCarrier: {carrier_name}\nTime Zones: {', '.join(time_zones)}"
        )
    else:
        print("The number is not valid or an error occurred.")
