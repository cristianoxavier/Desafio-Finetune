import os

DBCONN = os.getenv("DBCONN")
HOST = os.getenv("IP_ADDRESS") or "localhost"
PORT = os.getenv("SERVER_PORT") or 8080