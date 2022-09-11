class College:
	def __init__(self, data: list) -> None:
		self.data = data

	@property
	def name(self) -> str:
		"""The name of the college."""
		return self.data['school.name']

	@property
	def location(self) -> dict:
		"""Return the state and city of the college."""
		return {'city': self.data['school.city'], 'state': self.data['school.state']}
