import os
from configparser import ConfigParser

class ConfigReader:
    @staticmethod
    def read_config(section, key):
        config = ConfigParser()
        config.optionxform = str  # preserve case sensitivity if needed
        # Dynamically resolve the path to config.ini (assumes it's in the project root)
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        config_path = os.path.join(project_root, "config.ini")
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"[ConfigReader] Config file not found at: {config_path}")
        config.read(config_path)
        if not config.has_section(section):
            raise KeyError(f"[ConfigReader] Section '{section}' not found in config.ini")
        if not config.has_option(section, key):
            raise KeyError(f"[ConfigReader] Key '{key}' not found under section '{section}'")

        return config.get(section, key)
