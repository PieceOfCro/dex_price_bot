import logging
import sys

logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    "[%(asctime)s] [%(name)s] %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S"
)
stream_handler = logging.StreamHandler(stream=sys.stdout)
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

_discord_logging = logging.getLogger("discord")
_discord_logging.setLevel(logging.INFO)
