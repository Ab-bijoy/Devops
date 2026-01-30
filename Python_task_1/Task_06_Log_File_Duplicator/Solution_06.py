import os
import shutil

source_file = "app.log"

if os.path.exists(source_file):
    for i in range(1, 6):
        destination = f"app_{i}.log"
        shutil.copy(source_file, destination)
        print(f"Log File Name: {destination}")
