import os
import json
import time

def ping(ip):
    response = os.system("ping -n 1 {}".format(ip))  # pour Windows
    return response == 0

while True:
    status = {
        "R1": "🟢 En marche" if ping("172.25.214.61") else "🔴 Hors ligne",
        "R2": "🟢 En marche" if ping("172.25.214.62") else "🔴 Hors ligne",
        "R3": "🟡 Maintenance"
    }

    with open("status.json", "w") as f:
        json.dump(status, f)

    time.sleep(5)  # comme une pause cyclique d'OB
