from logging.config import dictConfig




LOGGING_CONFIG = {
    'version': 1,
    'loggers': {
        '': {  # root logger
            'level': 'DEBUG',
            'handlers': ['debug_console_handler', 'file_handler'],
        }
    },
    'handlers': {
        'debug_console_handler': {
            'level': 'DEBUG',
            'formatter': 'info',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'file_handler': {
            'level': 'DEBUG',
            'formatter': 'info',
            'class': 'logging.FileHandler',
            'filename': 'ECOMMERCE.log',
            'mode': 'a+',
        }
    },
    'formatters': {
        'info': {
            'format': '%(asctime)s %(levelname)s %(name)s :: %(module)s|%(lineno)s ::  %(message)s',
            'datefmt':'%Y-%m-%d , %H:%M:%S'
            }
    }
}


dictConfig(LOGGING_CONFIG)
