import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

# Directorio raíz de HomeStock
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Cargar las variables utilizadas por Docker Compose
load_dotenv(PROJECT_ROOT / ".env")

# Construir la conexión a PostgreSQL
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username=os.environ["POSTGRES_USER"],
    password=os.environ["POSTGRES_PASSWORD"],
    host="127.0.0.1",
    port=int(os.getenv("POSTGRES_PORT", "5434")),
    database=os.environ["POSTGRES_DB"],
)

# Motor de conexión
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

# Fábrica de sesiones
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)