import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import client, db
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError


class TestMongoConnection(unittest.TestCase):

    def test_connection_established(self):
        """Verifica que la conexión con MongoDB se puede establecer"""
        try:
            client.admin.command('ping')  # Simple comando para probar conexión
            connected = True
        except (ConnectionFailure, ServerSelectionTimeoutError):
            connected = False
        self.assertTrue(connected, "No se pudo conectar a MongoDB")

    def test_database_exists(self):
        """Verifica que la base de datos se haya creado o esté accesible"""
        dbs = client.list_database_names()
        self.assertIn(db.name, dbs, f"La base de datos '{db.name}' no existe en MongoDB")

    def test_users_collection_accessible(self):
        """Verifica que la colección 'users' esté accesible"""
        collections = db.list_collection_names()
        # No lanza error aunque no exista, solo verifica acceso
        self.assertIn("users", collections or [], "La colección 'users' no está accesible en la base de datos")

if __name__ == "__main__":
    unittest.main()
