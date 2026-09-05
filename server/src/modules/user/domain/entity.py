from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from shared.base_entity import Base, BaseModelMixin


class User(BaseModelMixin, Base):
    __tablename__ = "users"

    clerk_id: Mapped[str] = mapped_column(
        String(255), nullable=False, unique=True, index=True
    )
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    email: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True, unique=True, index=True
    )

    business_user_mappings = relationship(
        "BusinessUserMapping", back_populates="user", cascade="all, delete-orphan"
    )
    notifications = relationship(
        "Notification", back_populates="user", cascade="all, delete-orphan"
    )
    sent_invites = relationship(
        "BusinessInvite",
        back_populates="from_user",
        foreign_keys="BusinessInvite.from_user_id",
        cascade="all, delete-orphan",
    )
    received_invites = relationship(
        "BusinessInvite",
        back_populates="to_user",
        foreign_keys="BusinessInvite.to_user_id",
        cascade="all, delete-orphan",
    )
