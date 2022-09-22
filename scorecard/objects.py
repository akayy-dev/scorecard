from typing import Dict


class Tuition:
	def __init__(self, data: dict) -> None:
		self.data = data

	@property
	def room_and_board(self) -> float:
		"""Cost of attendance: on-campus room and board"""
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


class StudentBody:
	def __init__(self, data) -> None:
		self.data = data

	@property
	def undergrad_size(self) -> int:
		"""Enrollment of undergraduate certificate/degree-seeking students """
		return self.data['size']

	@property
	def graduate_size(self) -> int:
		return self.data['grad_students']

	@property
	def racial_diversity(self) -> Dict[str, float]:
		# Student data, rounded to 2 decimal places.
		white = round(self.data['demographics.race_ethnicity.white'] * 100, 3)
		black = round(self.data['demographics.race_ethnicity.black'] * 100, 3)
		hispanic = round(self.data['demographics.race_ethnicity.hispanic'] * 100, 3)
		asian = round(self.data['demographics.race_ethnicity.asian'] * 100, 3)
		aian = round(self.data['demographics.race_ethnicity.aian'] * 100, 3)
		nhpi = round(self.data['demographics.race_ethnicity.nhpi'] * 100, 3)
		biracial = round(
			self.data['demographics.race_ethnicity.two_or_more'] * 100, 3)
		alien = round(
			self.data['demographics.race_ethnicity.non_resident_alien'] * 100, 3)
		unknown = round(self.data['demographics.race_ethnicity.unknown'] * 100, 3)

		return {'white': white,
                    'black': black,
                    'hispanic': hispanic,
                    'asian': asian,
                    'native american': aian,
                    'hawaiian': nhpi,
                    'biracial': biracial,
                    'alien': alien,
                    'unknown': unknown,
          }

	@property
	def gender_breakdown(self) -> Dict[str, float]:
		"""Return the gender breakdown of a college"""
		men = round(self.data['demographics.men'] * 100, 3)
		women = round(self.data['demographics.women'] * 100, 3)
		return {'men': men, 'women': women}


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
	def student(self) -> StudentBody:
		student_dict = {}
		keys_list = list(self.data.keys())

		key: str
		for key in keys_list:
			if key.startswith(f'{self.year}.student'):
				strip_key = len(f'{self.year}.student') + 1
				student_dict[key[strip_key:]] = self.data[key]
		return StudentBody(data=student_dict)

	@property
	def cost(self) -> Tuition:
		cost_dict = {}
		keys_list = list(self.data.keys())

		key: str
		for key in keys_list:
			if key.startswith(f'{self.year}.cost'):
				strip_key = len(f'{self.year}.cost') + 1
				cost_dict[key[strip_key:]] = self.data[key]
		return Tuition(data=cost_dict)

	def __str__(self) -> str:
		return f'{self.data[f"{self.year}.school.name"]} - {self.data[f"id"]}'

	def __eq__(self, other: object) -> bool:
		if self.data['id'] == other.data['id']:
			return True
		else:
			return False
