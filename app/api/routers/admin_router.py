from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.models.schemas.base_response import BaseResponse
from app.core.db_config import drop_tables, create_tables
from app.utils.db_init import init_db

router = APIRouter(prefix = "/api/admin", tags = ["Admin"])

@router.post("/table/refreshAll", response_model = BaseResponse[None])
def table_refresh_all() -> BaseResponse[None]:
    """Refresh all database tables"""
    drop_tables()
    create_tables()
    init_db()
    return BaseResponse.create_success(message = "Tables refreshed successfully", data = None)
    
    


