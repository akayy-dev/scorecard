
class InvalidAPIKey(Exception):
	def __init__(self, message="Attempt to connect to collegescorecard with an invalid API key"):
		self.message = message
		super().__init__(self.message)


class MissingAPIKey(Exception):
	def __init__(self, message="Attempt to connect to collegescorecard with no API key"):
		self.message = message
		super().__init__(self.message)
