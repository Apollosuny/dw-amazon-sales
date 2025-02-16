import logging
import time

from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

from config.settings import POSTGRES_CONN_STRING
from plugins.models.models import base


class Initialize:
    def __init__(self, db_conn: str) -> None:
        self.engine = create_engine(db_conn)
        self.init_db()

    def init_db(self):
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
            base.metadata.create_all(self.engine, checkfirst=True)
        else:
            base.metadata.create_all(self.engine, checkfirst=True)
        time.sleep(1)
        logging.info("Sucessfully initialized database")


def initialize_db():
    Initialize(POSTGRES_CONN_STRING)
