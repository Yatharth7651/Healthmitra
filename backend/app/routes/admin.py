from fastapi import APIRouter, HTTPException, status, Depends
from app.services.admin_service import AdminService
from app.utils.jwt_handler import get_current_user

router = APIRouter(prefix="/admin", tags=["Admin"])
admin_service = AdminService()


@router.get("/stats", response_model=dict)
async def get_stats(current_user: dict = Depends(get_current_user)):
    """Get system statistics"""
    try:
        stats = await admin_service.get_system_stats()
        return {"stats": stats}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.get("/triage-trends", response_model=dict)
async def get_triage_trends(current_user: dict = Depends(get_current_user)):
    """Get triage distribution trends"""
    try:
        trends = await admin_service.get_triage_trends()
        return {"trends": trends}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/ashaworker-stats", response_model=dict)
async def get_ashaworker_stats(current_user: dict = Depends(get_current_user)):
    """Get stats for the currently logged in Ashaworker/Admin"""
    try:
        user_id = current_user.get("user_id") or str(current_user.get("_id") or current_user.get("id"))
        stats = await admin_service.get_ashaworker_stats(user_id)
        return {"stats": stats}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )