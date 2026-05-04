from netmiko import ConnectHandler
from dotenv import dotenv_values
import os

env = dotenv_values()

os.makedirs("configbackups", exist_ok=True)

switches = [
    {"name": "SW1", "ip": "10.0.20.100"},
    {"name": "SW2", "ip": "10.0.20.200"},
]

for sw in switches:
    print(f"Backing up {sw['name']}...")

    device = {
        "device_type": "cisco_ios",
        "host": sw["ip"],
        "username": env["USERNAME"],
        "password": env["PASSWORD"],
        "secret": env["SECRET"],
    }

    conn = ConnectHandler(**device)
    conn.enable()

    config = conn.send_command("show running-config")

    filename = f"configbackups/{sw['name']}-backup.ios"

    with open(filename, "w") as f:
        f.write(str(config))

    conn.disconnect()