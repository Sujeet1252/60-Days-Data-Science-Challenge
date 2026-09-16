def validate_house_data(data):

    if not data:
        return "JSON body is required"

    required_fields = [
        "area",
        "bedrooms",
        "bathrooms",
        "age"
    ]

    for field in required_fields:

        if field not in data:
            return f"{field} is required"

    for field in required_fields:

        if not isinstance(
            data[field],
            (int, float)
        ):
            return f"{field} must be a number"

    if data["area"] <= 0:
        return "Area must be greater than 0"

    if data["bedrooms"] <= 0:
        return "Bedrooms must be greater than 0"

    if data["bathrooms"] <= 0:
        return "Bathrooms must be greater than 0"

    if data["age"] < 0:
        return "Age cannot be negative"

    return None