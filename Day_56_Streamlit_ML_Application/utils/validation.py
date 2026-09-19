def validate_house_data(
    area,
    bedrooms,
    bathrooms,
    age
):

    if area <= 0:
        return "Area must be greater than 0."

    if bedrooms <= 0:
        return "Bedrooms must be greater than 0."

    if bathrooms <= 0:
        return "Bathrooms must be greater than 0."

    if age < 0:
        return "House age cannot be negative."

    return None