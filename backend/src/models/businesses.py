from db import Base, BaseModelMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text
from sqlalchemy.orm import relationship

class Business(BaseModelMixin,Base):
    __tablename__ = "businesses"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    industry: Mapped[str] = mapped_column(String(255), nullable=False)
   
    # Relationships
    business_user_mappings = relationship("BusinessUserMapping", back_populates="business", cascade="all, delete-orphan")
    invites=relationship('BusinessInvite', back_populates='business', cascade="all, delete-orphan")