from db.session import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


from fastapi import Depends, HTTPException, status, Request

def get_current_user(request: Request):
    user = request.state.user  # set by middleware

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )

    return user




# def require_business_member(
#     business_id: int,
#     user = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     mapping = db.query(BusinessUserMapping).filter_by(
#         user_id=user["id"],
#         business_id=business_id
#     ).first()

#     if not mapping:
#         raise HTTPException(
#             status_code=403,
#             detail="User is not a member of this business"
#         )

#     return mapping  # IMPORTANT: pass forward