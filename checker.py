import parser
import json

def get_new_in_radius(radius):
    houses = parser.results_in_radius(radius)

    with open("cache/checked.json", "r") as json_file:
        checked = json.load(json_file)
        new = []

        for house in houses:
            if house["PublicatieId"] in checked:
                continue
            else:
                new.append(house)
                checked.append(house["PublicatieId"])

    with open("cache/checked.json", "w") as json_file:
        json.dump(checked, json_file)


    return new
