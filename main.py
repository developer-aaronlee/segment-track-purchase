import pandas as pd
import requests
import json

segment_track = "https://api.segment.io/v1/track"

qa_headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic dnJPdHdtWlU1Q25LN0RsQVFoQ1N1RzdjeFhSU3dZQmM6"
}

prod_headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic aktFVHNnQzBJWlg4SExyRzl4VFNXYVQ1dzZhcWZTb3U6"
}


df = pd.read_csv("order_completed_manualbackfill_20221113.csv")
# print(df)

df.fillna("", inplace=True)
isna_rows = df[df.isna().values.any(axis=1)]
# print(isna_rows)

all_data = df.to_numpy()
# print(all_data)

columns = df.columns
# print(columns)

"""Method 1"""
# for x in range(len(all_data)):
#     data = {
#         columns[0]: all_data[x][0],
#         "event": "Order Completed",
#         "properties": {
#             columns[1]: all_data[x][1],
#             columns[2]: all_data[x][2],
#             columns[3]: all_data[x][3],
#             columns[4]: all_data[x][4],
#             columns[5]: all_data[x][5],
#             columns[6]: all_data[x][6],
#             columns[7]: all_data[x][7],
#             columns[8]: all_data[x][8],
#             columns[9]: all_data[x][9],
#             columns[10]: all_data[x][10],
#             columns[11]: all_data[x][11],
#             columns[12]: all_data[x][12],
#             columns[13]: all_data[x][13],
#             columns[14]: json.loads(all_data[x][14]),
#             columns[15]: all_data[x][15],
#             columns[16]: all_data[x][16],
#             columns[17]: all_data[x][17],
#             columns[18]: all_data[x][18],
#             columns[19]: all_data[x][19],
#             columns[20]: all_data[x][20]
#         },
#         columns[21]: all_data[x][21].split(".")[0].replace(" ", "T") + "Z"
#     }
#
#     body = json.dumps(data)
#     print(body)

"""Method 2"""
# def set_properties(num):
#     properties = {}
#     for i in range(1, 21):
#         if i == 14:
#             properties[columns[i]] = json.loads(all_data[num][i])
#         else:
#             properties[columns[i]] = all_data[num][i]
#
#     return properties
#
#
# for x in range(len(all_data)):
#     data = {
#         columns[0]: all_data[x][0],
#         "event": "Order Completed",
#         "properties": set_properties(x),
#         columns[21]: all_data[x][21].split(".")[0].replace(" ", "T") + "Z"
#     }
#
#     body = json.dumps(data)
#     print(data)

"""Method 3"""
for x in range(len(all_data)):
    data = {
        columns[0]: all_data[x][0],
        "event": "Order Completed",
        "properties": {
            columns[i]: (json.loads(all_data[x][i]) if i == 14 else all_data[x][i]) for i in range(1, 21)
        },
        columns[21]: all_data[x][21].split(".")[0].replace(" ", "T") + "Z"
    }

    body = json.dumps(data)
    # print(data)

    # response = requests.post(url=segment_track, data=body, headers=qa_headers)
    # print(f"Row {x + 1}: {all_data[x][0]} Response:", response.json())
