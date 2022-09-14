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
		women = round(
			(self.data[f'{self.year}.student.demographics.women'] * 100), 2)
		return {'men': men, 'women': women}

	@property
	def undergrad(self) -> int:
		"""Return the amount of undergrad students in the college."""
		return self.data[f'{self.year}.student.size']

	@property
	def region(self) -> int:
		'''Return the colleges region code.'''
		return self.data[f'{self.year}.school.region_id']

	@property
	def acceptance_rate(self) -> float:
		'''Return the admission rate.'''
		# Make the rate a percentage with two decimal places.
		percentage = round(
			(self.data[f'{self.year}.admissions.admission_rate.overall'] * 100), 2)
		return percentage

	@property
	def sat_scores(self) -> dict:
		'''Return the midpoint of SAT scores.'''
		math = self.data[f'{self.year}.admissions.sat_scores.midpoint.math']
		writing = self.data[f'{self.year}.admissions.sat_scores.midpoint.writing']
		critical_reading = self.data[f'{self.year}.admissions.sat_scores.midpoint.critical_reading']
		overall = self.data[f'{self.year}.admissions.sat_scores.average.overall']

		return {'math': math, 'writing': writing, 'critical_reading': critical_reading, 'overall': overall}

	@property
	def tuition(self) -> dict:
		return {'in state': self.data[f'{self.year}.cost.tuition.in_state'], 'out of state': self.data[f'{self.year}.cost.tuition.out_of_state']}

	def __str__(self) -> str:
		return f'{self.data[f"{self.year}.school.name"]} - {self.data[f"id"]}'

	def __eq__(self, other: object) -> bool:
		if self.data['id'] == other.data['id']:
			return True
		else:
			return False
