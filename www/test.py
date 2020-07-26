import orm
from models import User
import asyncio


async def test():
    await orm.create_pool(loop, user='root', password='password', db='awesome')
    u = User(name='test_again', email='test@example.com', passwd='abc123456', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
print('Test finished.')
