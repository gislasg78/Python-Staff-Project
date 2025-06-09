import re

def valid_email(email):
	valid_format = r"^([a-z0-9]+[-_.])*[a-z0-9]+@[a-z0-9]+(\.[a-z]{2,})+$"

	if re.match(valid_format, email, re.IGNORECASE):
		return True
	return False

personal_email = "gislasg78@gmail.com"
valid_email = valid_email(personal_email)
print(f"Valid e-mail: [{valid_email}] : [{personal_email}].")
