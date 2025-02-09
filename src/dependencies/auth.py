from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from src.core.config import settings

security = HTTPBearer()

def verify_supabase_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    print(credentials, "credentials")
    token = credentials.credentials
    print(token, "token")
    print(settings.SUPABASE_JWT_SECRET, "settings.SUPABASE_JWT_SECRET")
    print(settings.SUPABASE_JWT_ALGORITHM, "settings.SUPABASE_JWT_ALGORITHM")

    try:
        payload = jwt.decode(
            token,
            settings.SUPABASE_JWT_SECRET,
            algorithms=[settings.SUPABASE_JWT_ALGORITHM],
            verify=True,
            options={"verify_aud": False},  # Disable audience verification
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )

    return payload