from loguru import logger
from datetime import datetime

def add_logger(program):
    log_file_name = datetime.now().strftime("%y%m%d")
    logger.add(f".\\log\\{log_file_name}.log",
                mode = "w",
                level = "DEBUG", 
                format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <yellow>({file})</yellow> Line {line} - <b>{message}</b>", 
                colorize = False, 
                backtrace = False, 
                diagnose = True)
    program()