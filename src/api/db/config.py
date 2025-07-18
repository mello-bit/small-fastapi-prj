from decouple import config
from typing import cast


DATABASE_URL = cast(str, config("DATABASE_URL", default=""))