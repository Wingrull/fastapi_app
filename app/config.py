import os

from starlette.config import Config

dir_path = os.path.dirname(os.path.realpath(__file__))
root_dir = dir_path[:-3]

config = Config(f'{root_dir}.env')
DATABASE_URL = config('DB_URL', cast=str)
