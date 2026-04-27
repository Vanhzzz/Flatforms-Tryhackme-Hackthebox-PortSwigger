import requests
import json

base_url = "http://IP:PORT/api.php/user/"
all_data = []
for uid in range (1,1000):
    url = f"{base_url}{uid}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            all_data.append(data)
    except Exception as e:
        print(f"Lỗi tại {uid}: {e}")
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent = 4)
