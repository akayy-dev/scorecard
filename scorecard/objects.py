class College:
	def __init__(self, data: list, year: str) -> None:
		self.data = data
		self.year = year

	@property
	def name(self) -> str:
		"""The name of the college."""
		return self.data[f'{self.year}.school.name']

	@property
	def location(self) -> dict:
		"""Return the state and city of the college."""
		return {'city': self.data[f'{self.year}.school.city'], 'state': self.data[f'{self.year}.school.state'], 'zip': self.data[f'{self.year}.school.zip']}

	@property
	def gender_breakdown(self) -> dict:
		"""Return the percentage of each gender in a dictionary."""
		# Rounds the percentage to two decimal places.
		men = round((self.data[f'{self.year}.student.demographics.men'] * 100), 2)
		women = round( (self.data[f'{self.year}.student.demographics.women'] * 100), 2)
		return {'men': men, 'women': women}

	@property
	def undergrad(self) -> int:
		"""Return the amount of undergrad students in the college."""
		return self.data[f'{self.year}.student.size']

	def __str__(self) -> str:
		return f'{self.data[f"{self.year}.school.name"]} - {self.data[f"id"]}'

	def __eq__(self, other: object) -> bool:
		if self.data['id'] == other.data['id']:
			return True
		else:
			return False
