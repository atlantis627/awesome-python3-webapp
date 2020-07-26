import logging
import asyncio
import orm
from quart import Quart, render_template
from models import User
from config import configs

logging.basicConfig(level=logging.INFO)
app = Quart(__name__)


@app.route('/')
async def index():
    users = await User.findAll()
    return await render_template('index.html', users=users)


# logging.info('server started at http://127.0.0.1:9000...')


@app.before_serving
async def startup():
    loop = asyncio.get_event_loop()
    await orm.create_pool(loop, **configs.db)


app.run(debug=True, use_reloader=True, port=9000)
