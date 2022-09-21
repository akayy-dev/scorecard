class Tuition:
	def __init__(self, data: dict, year: int) -> None:
		self.data = data
		self.year = year

	@property
	def room_and_board(self) -> float:
		"""Cost of attendance: off-campus room and board"""
		return self.data['roomboard.oncampus']

	@property
	def overall_median(self) -> int:
		"""Overall median for average net price"""
		return self.data['avg_net_price.consumer.overall_median']

	def get_tuition(self, in_state=True) -> int:
		"""Tuition and fees """
		if in_state:
			return self.data['tuition.in_state']
		else:
			return self.data['tuition.out_of_state']


class College:
	def __init__(self, data: dict, year: str) -> None:
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
	def cost(self) -> Tuition:
		# Send ONLY the cost data to the Tuition object.
		# TODO: Strip the self.year from the key name, as to avoid needing to pass the year to Tuition.
		cost_dict = {}
		keys_list = list(self.data.keys())

		key: str
		for key in keys_list:
			if key.startswith(f'{self.year}.cost'):
				strip_key = len(f'{self.year}.cost') + 1
				cost_dict[key[strip_key:]] = self.data[key]
		return Tuition(data=cost_dict, year=self.year)

	def __str__(self) -> str:
		return f'{self.data[f"{self.year}.school.name"]} - {self.data[f"id"]}'

	def __eq__(self, other: object) -> bool:
		if self.data['id'] == other.data['id']:
			return True
		else:
			return False
