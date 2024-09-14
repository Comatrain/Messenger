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


# TODO: Setup lazy loading for models
class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"), nullable=True)

    parent_company: Mapped["Company"] = relationship(
        back_populates="child_user", lazy="joined"
    )


class Company(Base):
    __tablename__ = "company"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str]
    address: Mapped[str]

    # One-to-many (Company - User)
    child_user: Mapped[list["User"]] = relationship(
        back_populates="parent_company", lazy="joined"
    )
