from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from backend.models import Company
from backend.schemas import CompanySchema


async def create_company(
    company: CompanySchema,
    db: AsyncSession,
) -> CompanySchema:
    model_company = Company(**company.model_dump())
    db.add(model_company)
    await db.commit()
    await db.refresh(model_company)
    return company


async def get_company_by_id(company_id: int, db: AsyncSession) -> CompanySchema:
    stmt = select(Company).filter(Company.id == company_id)
    result = await db.execute(stmt)
    company_model = result.unique().scalars().one()
    company_schema = CompanySchema.model_validate(company_model)
    return company_schema


async def get_company_by_name(company_name: str, db: AsyncSession) -> CompanySchema:
    stmt = select(Company).filter(Company.name == company_name)
    result = await db.execute(stmt)
    company_model = result.unique().scalars().one()
    company_schema = CompanySchema.model_validate(company_model)
    return company_schema
