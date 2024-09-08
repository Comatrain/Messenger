from fastapi import APIRouter

router = APIRouter(prefix="/pages", tags=["Pages"])


@router.get("/test")
def get_test():
    return "This is test"
