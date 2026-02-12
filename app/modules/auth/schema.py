from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    """Схема токена"""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    """Схема данных внутри токена"""

    sub: int  # user_id
    type: str  # access or refresh


class LoginRequest(BaseModel):
    """Схема логина"""

    email: EmailStr
    password: str


class RefreshTokenRequest(BaseModel):
    """Схема запроса на обновление токена"""

    refresh_token: str
