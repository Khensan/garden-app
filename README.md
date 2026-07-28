# Interactive Gardening Advice Script

A lightweight, beginner-friendly Python script that generates seasonal watering, protection, and cultivation tips based on user input. 

## Features
* **Seasonal Care Logic:** Tailors watering and frost-protection tips for summer and winter.
* **Plant-Specific Insights:** Provides growth and pest-control advice for flowers and vegetables.
* **Modular Structure:** Built using clear conditional logic, making it easy to extend for more seasons or plant types.

## Code Structure

```python
# Hardcoded values for the season and plant type
season = "summer"  # TODO: Replace with input() to allow user interaction.
plant_type = "flower"  # TODO: Replace with input() to allow user interaction.

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)
```

## How to Run
1. Ensure you have **Python 3.x** installed.
2. Save the code into a file named `gardening_advice.py`.
3. Open your terminal or command prompt and run:
   ```bash
   python gardening_advice.py
   ```

## Planned Enhancements (TODOs)
* [ ] Refactor the hardcoded variables to accept dynamic user input via `input()`.
* [ ] Modularise the logic by breaking conditional blocks into reusable functions.
* [ ] Transition from `if-elif` blocks to a **dictionary-based lookup map** to manage data scalably.
* [ ] Build a recommendation engine that suggests ideal plant types based on the selected season.
