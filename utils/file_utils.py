import os
import json
from datetime import datetime

class FileUtils:
    @staticmethod
    def read_json(file_path):
        """Reads a JSON file and returns the data."""
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def write_json(file_path, data):
        """Writes data to a JSON file."""
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def get_current_timestamp():
        """Returns the current timestamp in UTC formatted as YYYY-MM-DD HH:MM:SS."""
        return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def file_exists(file_path):
        """Checks if a file exists at the given path."""
        return os.path.isfile(file_path)