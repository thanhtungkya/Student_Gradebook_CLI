import json
import os

class UserManager:
    def __init__(self, filename="user.json"):
        self.filename = filename
        self.user = None
        self.load_user()

    def load_user(self):
        """Load user profile if exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    self.user = json.load(f)
            except json.JSONDecodeError:
                self.user = None
        else:
            self.user = None

    def save_user(self, name):
        """Save user profile to file."""
        self.user = {"name": name}
        with open(self.filename, "w") as f:
            json.dump(self.user, f, indent=4)

    def get_username(self):
        """Return the stored username or None."""
        if self.user:
            return self.user.get("name")
        return None
