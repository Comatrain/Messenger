from sqlalchemy import Integer, String, Boolean, JSON, MetaData
from sqlalchemy.orm import mapped_column, DeclarativeBase


# configure constraint naming convention
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata_obj = MetaData(naming_convention=convention)


# Declarative base class with custom metadata
class Base(DeclarativeBase):
    metadata = metadata_obj


class Role(Base):
    __tablename__ = "role"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(length=320), nullable=False)
    permissions = mapped_column(JSON)


class User(Base):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    username = mapped_column(String(length=320), unique=True, nullable=False)
    hashed_password = mapped_column(String(length=1024), nullable=False)
    role_id = mapped_column(Integer, nullable=False)
    is_active = mapped_column(Boolean, default=True, nullable=False)
    is_superuser = mapped_column(Boolean, default=False, nullable=False)
    is_verified = mapped_column(Boolean, default=False, nullable=False)
