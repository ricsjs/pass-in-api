from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendee_handler import AttendeeHandler
from src.errors.error_handler import handle_error

attendee_route_bp = Blueprint("attendee_route", __name__)

@attendee_route_bp.route("/events/<event_id>/register", methods=["POST"])
def create_attendee(event_id):
  try:
    attendees_handler = AttendeeHandler()
    http_request = HttpRequest(param={ "event_id": event_id }, body=request.json)
    
    http_response = attendees_handler.register(http_request)
    return jsonify(http_response.body), http_response.status_code
  except Exception as exception:
    http_response = handle_error(exception)
    return jsonify(http_response.body), http_response.status_code

@attendee_route_bp.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendees_badge(attendee_id):
  try:
    attendees_handler = AttendeeHandler()
    http_request = HttpRequest(param={ "attendee_id": attendee_id })
    
    http_response = attendees_handler.find_attendee_badge(http_request)
    return jsonify(http_response.body), http_response.status_code
  
  except Exception as exception:
    http_response = handle_error(exception)
    return jsonify(http_response.body), http_response.status_code

@attendee_route_bp.route("/events/<event_id>/attendees", methods=["GET"])
def get_attendees(event_id):
  try:
    attendees_handler = AttendeeHandler()
    http_request = HttpRequest(param={ "event_id": event_id })
    
    http_response = attendees_handler.finds_attendees_from_event(http_request)
    return jsonify(http_response.body), http_response.status_code
  
  except Exception as exception:
    http_response = handle_error(exception)
    return jsonify(http_response.body), http_response.status_code