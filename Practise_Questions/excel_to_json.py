import pandas as pd


def excel_to_json(excel_data):
    # Declare schema
    jsonData = {"employees": []}
    # Read excel
    df = pd.read_excel(excel_data)
    # convert the data into a dictionary
    data = df.to_dict(orient="records")
    # Append the data one by one
    for i in range(len(data)):
        jsonData["employees"].append(data[i])
    print(jsonData)


excel_to_json("excel_output.xlsx")
