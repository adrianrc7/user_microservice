from datetime import datetime, timezone
import bcrypt
from user_profile import UserProfile  # Asumiendo que el archivo se llama user_profile.py

class User:
    def __init__(self, id, username, email, is_admin, password,
                 created_at=None, profile=None, is_active=True, password_hashed=False):
        self.id = id
        self.username = username
        self.email = email
        self.is_admin = is_admin
        self.password_hash = password if password_hashed else bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.created_at = created_at or datetime.now(timezone.utc)
        self.profile = profile or UserProfile()  # Instancia de UserProfile
        self.is_active = is_active

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password_hash)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_admin": self.is_admin,
            "password_hash": self.password_hash,
            "created_at": self.created_at.isoformat(),
            "profile": self.profile.to_dict(),  # Convertir perfil a dict
            "is_active": self.is_active
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            username=data["username"],
            email=data["email"],
            is_admin=data["is_admin"],
            password=data["password_hash"],
            created_at=datetime.fromisoformat(data["created_at"]),
            profile=UserProfile.from_dict(data.get("profile", {})),
            is_active=data.get("is_active", True),
            password_hashed=True
        )

    def __repr__(self):
        return (f"User(id={self.id}, username={self.username}, email={self.email}, "
                f"is_admin={self.is_admin}, created_at={self.created_at}, "
                f"profile={self.profile}, is_active={self.is_active}, "
                f"favourite_players={self.profile.favourite_players})")
