from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID  # ✅ UUID 타입 추가


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    username: str

# ✅ 로그인 요청 스키마


class UserLogin(BaseModel):
    email: str
    password: str

# ✅ JWT 토큰 응답 스키마


class Token(BaseModel):
    access_token: str
    token_type: str

# ✅ 사용자 정보 응답 스키마


class UserResponse(BaseModel):
    user_id: UUID  # ✅ 여기서 int → UUID 변경
    email: str
    username: str
    created_at: datetime
