import pytest
from src.models.settings.connection import db_connection_handler
from .attendees_repository import AttendeesRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="do not execute to not create a new record")
def test_insert_attendee():
  event_id = "my-uuid"
  attendee = {
    "uuid": "my_uuid_attendee",
    "name": "attendee name",
    "email": "attendee email",
    "event_id": event_id
  }
  
  attendees_repository = AttendeesRepository()
  response = attendees_repository.insert_attendee(attendee)
  print(response)
  
def test_get_attendee_badge_by_id():
  attendee_id = "my_uuid_attendee"
  attendees_repository = AttendeesRepository()
  attendee = attendees_repository.get_attendee_badge_by_id(attendee_id)
  
  print(attendee)