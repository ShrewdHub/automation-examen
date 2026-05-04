from netmiko import ConnectHandler
from getpass import getpass

username = input("Username: ")
password = getpass("Password: ")
secret = getpass("Enable secret: ")

switches = [
    {"name": "SW1", "ip": "10.0.20.100"},
    {"name": "SW2", "ip": "10.0.20.200"},
]

for sw in switches:
    print(f"Connecting to {sw['name']}...")

    device = {
        "device_type": "cisco_ios",
        "host": sw["ip"],
        "username": username,
        "password": password,
        "secret": secret,
    }

    conn = ConnectHandler(**device)
    conn.enable()

    output = conn.send_command("show running-config | include version")
    print(output)

    conn.disconnect()