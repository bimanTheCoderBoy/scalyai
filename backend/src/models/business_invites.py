from db import Base, BaseModelMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Enum, UniqueConstraint
from sqlalchemy.orm import relationship
from .business_user_mappings import BusinessUserRole


import enum
class BusinessInviteStatus(enum.Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    CANCELLED = "cancelled"

class BusinessInvite(BaseModelMixin,Base):
    __tablename__ = "business_invites"

    business_id: Mapped[int] = mapped_column(ForeignKey("businesses.id"), nullable=False)
    from_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    to_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    role: Mapped[BusinessUserRole]= mapped_column(Enum(BusinessUserRole), nullable=False)
    status: Mapped[BusinessInviteStatus]= mapped_column(Enum(BusinessInviteStatus), nullable=False)

    # Relationships
    business = relationship("Business", back_populates="invites")
    from_user = relationship("User", back_populates="sent_invites",foreign_keys=[from_user_id])
    to_user = relationship("User", back_populates="received_invites",foreign_keys=[to_user_id])

    # Constraints
    __table_args__ = (
        UniqueConstraint("business_id", "from_user_id", "to_user_id", name="uix_business_user_invite"),
    )