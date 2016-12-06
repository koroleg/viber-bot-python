from future.utils import python_2_unicode_compatible
from viberbot.api import messages
from viberbot.api.event_type import EventType
from viberbot.api.user_profile import UserProfile
from viberbot.api.viber_requests.viber_request import ViberRequest


class ViberMessageRequest(ViberRequest):
	def __init__(self):
		super(ViberMessageRequest, self).__init__(EventType.MESSAGE)
		self._message = None
		self._sender = None
		self._message_token = None

	def from_dict(self, request_dict):
		super(ViberMessageRequest, self).from_dict(request_dict)
		self._message = messages.get_message(request_dict['message'])
		self._sender = UserProfile(request_dict['sender']['name'],
								   request_dict['sender']['avatar'],
								   request_dict['sender']['id'])
		self._message_token = request_dict['message_token']
		return self

	@property
	def message(self):
		return self._message

	@property
	def sender(self):
		return self._sender

	@property
	def message_token(self):
		return self._message_token

	@python_2_unicode_compatible
	def __str__(self):
		return u"ViberMessageRequest [{0}, message_token={1}, sender={2}, message={3}]" \
			.format(super(ViberMessageRequest, self).__str__(),
					self._message_token,
					self._sender,
					self._message)
