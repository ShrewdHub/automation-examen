from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException
from dotenv import dotenv_values

env = dotenv_values()

switches = [
    {"name": "SW1", "ip": "10.0.20.100"},
    {"name": "SW2", "ip": "10.0.20.200"},
]

for sw in switches:
    print(f"Connecting to {sw['name']}...")

    device = {
        "device_type": "cisco_ios",
        "host": sw["ip"],
        "username": env["USERNAME"],
        "password": env["PASSWORD"],
        "secret": env["SECRET"],
    }

    try:
        conn = ConnectHandler(**device)
        conn.enable()

        output = conn.send_command("show running-config | include version")
        print(output)

        conn.disconnect()

    except NetmikoTimeoutException:
        print(f"{sw['name']} is NOT reachable!")