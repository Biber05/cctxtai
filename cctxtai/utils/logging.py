def create_logger(name: str, log_lvl: str = "INFO"):
    """
    Creates a file logger with given name. Sets log level based on ENV 'LOG_LVL'

    :param log_lvl: level of logging as string
    :param name: string of logger name
    :return: logging.Logger
    """
    import os
    import logging

    lvl = logging.getLevelName(os.getenv("LOG_LVL", log_lvl))

    formatter = logging.Formatter(
        "%(asctime)s;%(name)s;%(levelname)s;%(module)s;%(funcName)s;%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger = logging.getLogger(f"{name.upper()}-Logger")

    from pathlib import Path

    path = Path.cwd().joinpath("logs")
    path.mkdir(parents=True, exist_ok=True)
    path = path.joinpath(f"{name}.log")

    mode = "a" if lvl != 10 else "w"
    handler = logging.FileHandler(path, mode=mode)
    handler.setFormatter(formatter)
    handler.setLevel(lvl)

    logger.addHandler(handler)
    logger.setLevel(level=lvl)

    print(
        f"INIT_LOGGER: name={name}, LVL={logger.level} FILE={path.__str__()}, MODE={mode}"
    )

    return logger
