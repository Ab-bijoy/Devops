servers = ["web01", "db01", "app01", "web02"]

print(f"Original servers list: {servers}")

web_servers = [servers[0], servers[-1]]

print(f"Web servers (first and last): {web_servers}")
