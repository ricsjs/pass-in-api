from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class CheckInsRepository:
  def insert_check_in(self, attendeeId: str) -> str:
    with db_connection_handler as database:
      try:
        checkIn = CheckIns(attendeeId=attendeeId)
        database.session.add(checkIn)
        database.session.commit()
        return attendeeId
      
      except IntegrityError:
        raise Exception('CheckIn já realizado!')
      
      except Exception as exception:
        database.session.rollback()
        raise exception
        