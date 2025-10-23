def validate_registration_data(data):
    errors = {}
    required_fields = ["username", "email", "nama", "password"]

    for field in required_fields:
        if field not in data or not data[field]:
            errors[field] = f"{field.capitalize()} wajib diisi"

    return errors if errors else None


def validate_login_data(data):
    errors = {}
    required_fields = ["username", "password"]

    for field in required_fields:
        if field not in data or not data[field]:
            errors[field] = f"{field.capitalize()} wajib diisi"

    return errors if errors else None