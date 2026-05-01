from typing import NoReturn

from fastapi import HTTPException, status


class HTTPError:
    """
    Utility class to raise formatted HTTP exceptions.
    """

    @staticmethod
    def bad_request(detail: str = "The request is invalid or malformed") -> NoReturn:
        """400 - Bad Request"""
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

    @staticmethod
    def unauthorized(detail: str = "Authentication is required") -> NoReturn:
        """401 - Unauthorized"""
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )

    @staticmethod
    def forbidden(detail: str = "Permission denied") -> NoReturn:
        """403 - Forbidden"""
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=detail)

    @staticmethod
    def not_found(detail: str = "Resource not found") -> NoReturn:
        """404 - Not Found"""
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

    @staticmethod
    def conflict(detail: str = "Conflict with current state") -> NoReturn:
        """409 - Conflict"""
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=detail)
