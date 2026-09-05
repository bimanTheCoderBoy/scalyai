import enum
from datetime import datetime

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    PrimaryKeyConstraint,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import JSON

from shared.base_entity import Base, BaseModelMixin


class BusinessUserRole(enum.Enum):
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"


class Business(BaseModelMixin, Base):
    __tablename__ = "businesses"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    industry: Mapped[str] = mapped_column(String(255), nullable=False)

    business_user_mappings = relationship(
        "BusinessUserMapping",
        back_populates="business",
        cascade="all, delete-orphan",
    )
    invites = relationship(
        "BusinessInvite",
        back_populates="business",
        cascade="all, delete-orphan",
    )


class BusinessUserMapping(Base):
    __tablename__ = "business_user_mappings"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    business_id: Mapped[int] = mapped_column(
        ForeignKey("businesses.id", ondelete="CASCADE"), nullable=False, index=True
    )

    role: Mapped[BusinessUserRole] = mapped_column(
        Enum(BusinessUserRole), nullable=False
    )
    permissions: Mapped[dict] = mapped_column(JSON)

    user = relationship("User", back_populates="business_user_mappings")
    business = relationship("Business", back_populates="business_user_mappings")

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    __table_args__ = (PrimaryKeyConstraint("user_id", "business_id"),)
