# create_db.py

import asyncio
from database import engine, Base

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create_db())
