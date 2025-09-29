# alembic/env.py
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

import sys
import os

# Ensure "src" is on the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

# Import your Base and settings
from src.infrastructure.db.models import Base
from src.config.settings import settings

# this is the Alembic Config object
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- ✅ Ensure Alembic uses a sync DB driver (psycopg2) ---
def make_sync_url(async_url: str) -> str:
    return async_url.replace("postgresql+asyncpg", "postgresql+psycopg2")

# Override sqlalchemy.url with sync URL
config.set_main_option("sqlalchemy.url", make_sync_url(settings.database_url))

# Point Alembic’s metadata to your models
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
