DANGEROUS_PORTS = (21, 23, 445)


def check_ports(active_ports):
    for port in active_ports:
        if port in DANGEROUS_PORTS:
            print(f"WARNING: Dangerous port {port} detected!")
