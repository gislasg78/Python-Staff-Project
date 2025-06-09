import phonenumbers

def validate_phone(str_phone, country_code=None):
	phone_number = phonenumbers.parse(str_phone, country_code)
	return phonenumbers.is_valid_number(phone_number)

phone_number = "+525519044356"
valid_phone = validate_phone(phone_number)
print(f"Validated Phone: [{valid_phone}] : [{phone_number}].")
