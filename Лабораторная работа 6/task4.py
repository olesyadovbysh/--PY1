import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as f:
        data = f.readlines()
        headers = data[0].strip(new_line).split(delimiter)
        list_dict = []
        for row in data[1:]:
           rows = row.strip(new_line).split(delimiter)
           dict_ = {h: r for h, r in zip(headers, rows)}
           list_dict.append(dict_)
        return list_dict

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
