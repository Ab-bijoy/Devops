port_string = "8080"
print(f"Data type: {type(port_string)}")
print(f"\nReceived port as string: '{port_string}'")

port = int(port_string)
print(f"Data type: {type(port)}")
print(f"\nConverted to integer: {port}")


if 1 <= port <= 65535:
    print("Valid")
else:
    print("Invalid")
