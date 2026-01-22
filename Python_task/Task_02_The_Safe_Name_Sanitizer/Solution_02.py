bucket_name = "My Project Backup"

print(f"Given bucket name: '{bucket_name}'")

bucket_name = bucket_name.strip()
print(f"After strip(): '{bucket_name}'")

bucket_name = bucket_name.replace(" ", "-")
print(f"After replace(): '{bucket_name}'")

bucket_name = bucket_name.lower()
print(f"After lower(): '{bucket_name}'")

print(f"\n Final valid bucket name: '{bucket_name}'")
