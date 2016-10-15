from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from config import (
    FLASHCARD_DB_USERNAME,
    FLASHCARD_DB_PASSWORD,
    FLASHCARD_TNS_NAME
)


class DBAccess(object):
    """This class allows the subclasses to have access to the SQLAlchemy session."""

    def __init__(self):
        self.session = self._get_orm_session()

    def _get_orm_session(self):
        connection_string = 'oracle+cx_oracle://{username}:{password}@{tnsname}'.format(username=FLASHCARD_DB_USERNAME,
                                                                                        password=FLASHCARD_DB_PASSWORD,
                                                                                        tnsname=FLASHCARD_TNS_NAME)
        engine = create_engine(connection_string)
        session = sessionmaker(bind=engine)

        return session
