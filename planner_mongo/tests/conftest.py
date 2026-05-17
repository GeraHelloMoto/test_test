from pathlib import Path
import pytest
from httpx import AsyncClient, ASGITransport
from database.connection import Settings
from models.users import User
from models.events import Event
from main import app


# @pytest.fixture(scope="session")
# def event_loop():
# 	loop = asyncio.get_event_loop()
# 	yield loop 
# 	loop.close()

async def init_db():
	test_settings = Settings()
	test_settings.DATABASE_URL = "mongodb://localhost:27017/testdb"
	await test_settings.initialize_database()

@pytest.fixture(scope="function")
async def default_client():
	await init_db()

	async with AsyncClient(
		transport=ASGITransport(app=app),
		base_url="http://app"
	) as client:
		yield client  

	await User.find_all().delete()
	await Event.find_all().delete()
	