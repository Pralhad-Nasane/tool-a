"""
Handles asset naming conventions.
"""

class AssetNamer:
    def __init__(self, prefix):
        self.prefix = prefix

    def generate_name(self, base_name):
        return f"{self.prefix}_{base_name}"
