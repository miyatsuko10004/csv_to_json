import csv
import json
import time

def csv_to_json(csv_file_path, json_file_path):
    data = []

    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            mansion = {
                "outPutName1": row["rowName1"],
                "outPutName2": row["rowName2"],
                "outPutName3": row["rowName3"],
                "outPutName4": f"{row['rowName4']} {row['rowName5']} {row['rowName6']} {row['rowName7']} {row['rowName8']}", #結合して文字列にするケース
                "outPutName5": f"https://www.example.com/{row['rowName9']}/{row['rowName10']}/", #URLの一部にするケース
                "outPutName6": f"/image/{row['rowName11']}_{row['rowName12']}.jpg?t={int(time.mktime(time.strptime(row['rowName13'], '%Y-%m-%d %H:%M:%S')))}" #時間の変換もするケース
            }
            data.append(mansion)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# 実行処理
csv_to_json("input.csv", "output.json"
