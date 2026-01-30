env = "production"

print(f"Current environment: {env}")

if env != "production":
    print("Executing Delete")
else:
    print("Access Denied: Cannot delete in Prod!")
