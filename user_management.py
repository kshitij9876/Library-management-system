from models import User
import storage

class UserManager:
    #Class for managing users in the library.
    def __init__(self):
        self._users = storage.load_users()

    def add_user(self, name, user_id):
        #Adds a new user to the library.
        if not any(user.user_id == user_id for user in self._users):
            user = User(name, user_id)
            self._users.append(user)
            storage.save_users(self._users)
            print("User added successfully.")
        else:
            print("User ID already exists.")

    def list_users(self):
        #Lists all users in the library.
        if self._users:
            for user in self._users:
                print(user)
        else:
            print("No users available.")

    def update_user(self, user_id, **kwargs):
        #Updates the details of a user by user ID.
        for user in self._users:
            if user.user_id == user_id:
                for key, value in kwargs.items():
                    if value is not None:
                        setattr(user, key, value)
                storage.save_users(self._users)
                print("User updated successfully.")
                return
        print("User not found.")

    def delete_user(self, user_id):
        # Deletes a user by user ID.
        self._users = [user for user in self._users if user.user_id != user_id]
        storage.save_users(self._users)
        print("User deleted successfully.")

    def get_user(self, user_id):
        for user in self._users:
            if user.user_id == user_id:
                return user
        return None
