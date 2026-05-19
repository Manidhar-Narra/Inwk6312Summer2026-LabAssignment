from netmiko import Netmiko

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.104",
        "username": "student",
        "password": "Meilab123",
    }
]

for device in devices:

    net_connect = Netmiko(**device)

    output = net_connect.send_command(
        "show ip route",
        use_textfsm=True
    )

    net_connect.disconnect()

    print("\n" + "=" * 70)
    print(f"DEVICE: {device['ip']}")
    print("=" * 70)

    for route in output:

        print(
            route.get("protocol", "-"),
            route.get("network", "-"),
            route.get("distance", "-"),
            route.get("metric", "-"),
            sep=" | "
        )
