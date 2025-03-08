import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

# List of files to create
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

# Create files if they don't exist
for file_path in list_of_files:
    file = Path(file_path)
    filedir, filename = os.path.split(file_path)

    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Corrected function name
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create file if it doesn't exist or is empty
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w") as f:
            pass
        logging.info(f"Created: {file_path}")
    else:
        logging.info(f"Already exists: {filename}")
