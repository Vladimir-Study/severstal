from loguru import logger

logger.add('./logs/logs.log', rotation='1 week', compression='zip', colorize=True,
           format="{time} {level} {message}", encoding='utf-8')