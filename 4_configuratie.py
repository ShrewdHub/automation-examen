from netmiko import ConnectHandler
from dotenv import dotenv_values

env = dotenv_values()

switches = [
    {"name": "SW1", "ip": "10.0.20.100"},
    {"name": "SW2", "ip": "10.0.20.200"},
]

for sw in switches:
    print(f"Configuring {sw['name']}...")

    device = {
        "device_type": "cisco_ios",
        "host": sw["ip"],
        "username": env["USERNAME"],
        "password": env["PASSWORD"],
        "secret": env["SECRET"],
    }

    conn = ConnectHandler(**device)
    conn.enable()

    output = conn.send_config_from_file("4_configuratie.ios")
    print(output)

    conn.disconnect()