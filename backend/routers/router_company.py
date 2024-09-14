from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud import crud_company
from backend.database import get_async_session
from backend.schemas import CompanySchema

router = APIRouter(prefix="/company", tags=["Company"])


@router.post(
    "/",
    status_code=201,
    response_model=CompanySchema,
)
async def create_company(
    company: CompanySchema,
    db: AsyncSession = Depends(get_async_session),
) -> CompanySchema:
    return await crud_company.create_company(
        company=company,
        db=db,
    )


@router.get(
    "/company/{company_id}",
    response_model=CompanySchema,
)
async def get_user_by_id(
    company_id: int,
    db: AsyncSession = Depends(get_async_session),
) -> CompanySchema:
    return await crud_company.get_company_by_id(
        company_id=company_id,
        db=db,
    )


@router.get(
    "/name/{company_name}",
    response_model=CompanySchema,
)
async def get_user_by_username(
    company_name: str,
    db: AsyncSession = Depends(get_async_session),
) -> CompanySchema:
    return await crud_company.get_company_by_name(
        company_name=company_name,
        db=db,
    )
