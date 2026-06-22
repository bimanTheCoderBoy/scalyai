from enum import Enum
from db import Base, BaseModelMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Enum, UniqueConstraint, Index , PrimaryKeyConstraint
from sqlalchemy.types import JSON
from sqlalchemy.orm import relationship

import enum
class BusinessUserRole(enum.Enum):
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"


class BusinessUserMapping(BaseModelMixin,Base):
    __tablename__ = "business_user_mappings"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    business_id: Mapped[int] = mapped_column(ForeignKey("businesses.id"), nullable=False, index=True)

    role: Mapped[BusinessUserRole]= mapped_column(Enum(BusinessUserRole), nullable=False)
    permissions: Mapped[dict] = mapped_column(JSON)

    # Relationships
    user = relationship("User", back_populates="business_user_mappings")
    business = relationship("Business", back_populates="business_user_mappings")

    # Constraints
    __table_args__ = (
        UniqueConstraint("user_id", "business_id", name="uix_user_business_mapping"),
        PrimaryKeyConstraint("user_id", "business_id"),
    )