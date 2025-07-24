class UserProfile:
    def __init__(self, avatar_url="", language="es", notifications_enabled=True, favourite_players=None):
        self.avatar_url = avatar_url
        self.language = language
        self.notifications_enabled = notifications_enabled
        self.favourite_players = favourite_players or []

    def to_dict(self):
        return {
            "avatar_url": self.avatar_url,
            "language": self.language,
            "notifications_enabled": self.notifications_enabled,
            "favourite_players": self.favourite_players
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            avatar_url=data.get("avatar_url", ""),
            language=data.get("language", "es"),
            notifications_enabled=data.get("notifications_enabled", True),
            favourite_players=data.get("favourite_players", [])
        )

    def __repr__(self):
        return (f"UserProfile(avatar_url={self.avatar_url}, language={self.language}, "
                f"notifications_enabled={self.notifications_enabled}, "
                f"favourite_players={self.favourite_players})")

