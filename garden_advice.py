def get_season_advice(season):
    """Return advice based on the provided season."""
    season = season.lower()
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """Return advice based on the provided plant type."""
    plant_type = plant_type.lower()
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    return "No advice for this type of plant."


def main():
    # Prompt user for dynamic inputs
    season = input("Enter current season (e.g., summer, winter): ").strip()
    plant_type = input("Enter plant type (e.g., flower, vegetable): ").strip()

    # Generate and print advice
    advice = get_season_advice(season) + get_plant_advice(plant_type)
    print("\n--- Gardening Advice ---")
    print(advice)


if __name__ == "__main__":
    main()