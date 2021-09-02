import pandas as pd
import json


def json_to_excel(json_data):
    # Read json
    with open(json_data) as f:
        d = json.load(f)
    # Convert the json data in tabular form
    df = pd.DataFrame(d["employees"])
    # convert the tabular data to excel
    df.to_excel("excel_output.xlsx", index=False)

json_to_excel('data_to_create_excel.json')