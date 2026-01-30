import scanner

active_ports = [22, 80, 21, 443, 23, 8080]

print(f"Scanning ports: {active_ports}")
print(f"Checking against dangerous ports: {scanner.DANGEROUS_PORTS}\n")

scanner.check_ports(active_ports)
