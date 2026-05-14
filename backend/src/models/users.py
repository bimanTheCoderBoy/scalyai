from tkinter import S
from db import Base, BaseModelMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from .business_invites import BusinessInvite
from typing import Optional

class User(BaseModelMixin,Base):
    __tablename__ = "users"

    clerk_id: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index= True)


    #Relations
    business_user_mappings = relationship("BusinessUserMapping", back_populates="user", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    sent_invites = relationship("BusinessInvite", back_populates="from_user",foreign_keys=[BusinessInvite.from_user_id])
    received_invites = relationship("BusinessInvite", back_populates="to_user",foreign_keys=[BusinessInvite.to_user_id])