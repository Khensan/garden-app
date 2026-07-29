# Accept dynamic, sanitised user inputs
season = input("Enter the current season (summer/winter): ").strip().lower()
plant_type = input("Enter your plant type (flower/vegetable): ").strip().lower()

advice = ""

if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

print(advice)

