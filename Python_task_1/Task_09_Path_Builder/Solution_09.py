import os

base_dir = "/var/log"
app_name = "nginx"
filename = "access.log"
full_path = os.path.join(base_dir, app_name, filename)

print(f"Base directory: {base_dir}")
print(f"App name: {app_name}")
print(f"Filename: {filename}")
print(f"\nFull path: {full_path}")
