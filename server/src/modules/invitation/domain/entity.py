import enum

from sqlalchemy import Enum, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.business.domain.entities import BusinessUserRole
from shared.base_entity import Base, BaseModelMixin


class BusinessInviteStatus(enum.Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    CANCELLED = "cancelled"


class BusinessInvite(BaseModelMixin, Base):
    __tablename__ = "business_invites"

    business_id: Mapped[int] = mapped_column(
        ForeignKey("businesses.id", ondelete="CASCADE"), nullable=False
    )
    from_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    to_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    role: Mapped[BusinessUserRole] = mapped_column(
        Enum(BusinessUserRole), nullable=False
    )
    status: Mapped[BusinessInviteStatus] = mapped_column(
        Enum(BusinessInviteStatus), nullable=False
    )

    business = relationship("Business", back_populates="invites")
    from_user = relationship(
        "User", back_populates="sent_invites", foreign_keys=[from_user_id]
    )
    to_user = relationship(
        "User", back_populates="received_invites", foreign_keys=[to_user_id]
    )

    __table_args__ = (
        UniqueConstraint(
            "business_id",
            "from_user_id",
            "to_user_id",
            name="uix_business_user_invite",
        ),
    )
