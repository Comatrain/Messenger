from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped, relationship

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

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str]


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[bytes]
    salt: Mapped[bytes]
    role_id: Mapped[int]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)

    # children
    cookie_session: Mapped[list["CookieSession"]] = relationship()


class CookieSession(Base):
    __tablename__ = "cookie_session"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    username_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    cookie: Mapped[str]
