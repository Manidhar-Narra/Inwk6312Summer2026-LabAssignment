from jinja2 import Environment, FileSystemLoader

# Load template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.j2')

# Dictionary containing interface information
interface = {
    "name": "GigabitEthernet0/1",
    "description": "Server Port",
    "vlan": 10
}

# Render template
output = template.render(interface=interface)

# Print configuration
print(output)
