import fetcher
import json

def cache():
    # try:
    #     with open("cache/data.json", "r") as json_file:
    #         return json.load(json_file)
    # except Exception as e:
    f = fetcher.sww_all()

        # with open("cache/data.json", "w+") as json_file:
        #     json.dump(f, json_file)

    return f
