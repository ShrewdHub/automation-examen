from netmiko import ConnectHandler

switches = [
    {"name": "SW1", "ip": "10.0.20.100"},
    {"name": "SW2", "ip": "10.0.20.200"},
]

for sw in switches:
    print(f"Connecting to {sw['name']}...")

    device = {
        "device_type": "cisco_ios",
        "host": sw["ip"],
        "username": "admin",
        "password": "cisco",
        "secret": "cisco",
    }

    conn = ConnectHandler(**device)
    conn.enable()

    output = conn.send_command("show running-config | include version")
    print(output)

    conn.disconnect()