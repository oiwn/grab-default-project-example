# -*- coding: utf-8 -*-
"""
Configs for default spider
"""
from models import init_engine
from sqlalchemy.orm import sessionmaker

# save or not
MAX_THREADS = 3
USE_CACHE = True
SAVE_TO_DB = USE_CACHE
CACHE_DB = 'default_project'

db_engine = init_engine()
Session = sessionmaker(bind=db_engine)

def default_spider_params():
    params = {
        'thread_number': MAX_THREADS,
        'network_try_limit': 20,
        'task_try_limit': 20,
    }
    if USE_CACHE:
        params.update({
            'use_cache': USE_CACHE,
            'cache_db': CACHE_DB,
            'debug_error' :True,
        })
        
    return params