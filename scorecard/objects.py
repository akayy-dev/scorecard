from typing import Dict


class Admissions:
	"""Data relating to a colleges admissions"""
	def __init__(self, data) -> None:
		self.data = data

	@property
	def rate(self) -> float:
		"""Admission rate"""
		return round(self.data['admission_rate.overall'] * 100, 3)

	# Test related properties
	@property
	def test_required(self) -> bool:
		"""Test score requirements for admission"""
		num = self.data['test_requirements']
		if num == 1:
			return True
		else:
			return False

	@property
	def act_scores(self) -> Dict[str, int]:
		"""Midpoint of the ACT scores"""
		math = self.data['act_scores.midpoint.math']
		english = self.data['act_scores.midpoint.english']
		cumulative = self.data['act_scores.midpoint.cumulative']

		return {'math': math, 'english': english, 'cumulative': cumulative}

	@property
	def sat_scores(self) -> Dict[str, int]:
		"""Midpoint of SAT scores at the institution"""
		english = self.data['sat_scores.midpoint.critical_reading']
		math = self.data['sat_scores.midpoint.math']
		cumulative = english + math

		return {'english': english, 'math': math, 'cumulative': cumulative}


class Tuition:
	def __init__(self, data: dict) -> None:
		self.data = data

	@property
	def room_and_board(self) -> float:
		"""Cost of attendance: on-campus room and board"""
		return self.data['roomboard.oncampus']

	@property
	def booksupply(self) -> int:
		"""Cost of attendance: estimated books and supplies"""
		return self.data['booksupply']

	@property
	def overall_median(self) -> int:
		"""Overall median for average net price"""
		return self.data['avg_net_price.consumer.overall_median']

	def get_tuition(self, in_state=True) -> int:
		"""Average cost of a year at the college.
		
		:param in_state: Return a colleges in-state tuition or out of state tuition, defaults to true.
		:type in_state: bool, optional
		"""
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
		"""Number of graduate students """
		return self.data['grad_students']

	@property
	def racial_diversity(self) -> Dict[str, float]:
		"""Racial diversity statistics, rounded to 2 decimal places."""
		# Student data, rounded to 2 decimal places.
		white = self.data['demographics.race_ethnicity.white']
		black = self.data['demographics.race_ethnicity.black']
		hispanic = self.data['demographics.race_ethnicity.hispanic']
		asian = self.data['demographics.race_ethnicity.asian']
		aian = self.data['demographics.race_ethnicity.aian']
		nhpi = self.data['demographics.race_ethnicity.nhpi']
		biracial =  self.data['demographics.race_ethnicity.two_or_more']
		alien =  self.data['demographics.race_ethnicity.non_resident_alien']
		unknown = self.data['demographics.race_ethnicity.unknown']

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
		"""Return the gender breakdown of a college."""
		men = round(self.data['demographics.men'] * 100, 3)
		women = round(self.data['demographics.women'] * 100, 3)
		return {'men': men, 'women': women}


class College:
	def __init__(self, data: dict, year: str) -> None:
		self.data = data
		self.year = year

	def __clean_dict(self, category: str) -> dict:
		"""Strip the year and category from a dictionarys keys."""
		clean_dict = {}
		keys_list = list(self.data.keys())

		key: str
		for key in keys_list:
			if key.startswith(f'{self.year}.{category}'):
				strip_key = len(f'{self.year}.{category}') + 1
				clean_dict[key[strip_key:]] = self.data[key]
		return clean_dict

	@property
	def accreditor(self) -> str:
		"""Accreditor for institution """
		return self.data[f'{self.year}.school.accreditor']
		
	@property
	def ownership(self) -> int:
		"""Control of institution, returns either 1, 2, or 3. \n
			1 - Public \n
			2 - Private, Nonprofit \n
			3 - Private, for-profit"""
		return self.data[f'{self.year}.school.ownership']
	
	@property
	def operating(self) -> bool:
		"""Flag for currently operating institution"""
		flag = self.data[f'{self.year}.school.operating']

		if flag:
			return True
		else:
			return False
	
	@property
	def endowment_begin(self) -> int:
		"""Value of school's endowment at the beginning of the fiscal year """
		return self.data[f'{self.year}.school.endowment.begin']
	@property
	def endowment_end(self) -> int:
		"""Value of school's endowment at the end of the fiscal year """
		return self.data[f'{self.year}.school.endowment.end']

	@property
	def name(self) -> str:
		"""Institution name"""
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
	def admissions(self) -> Admissions:
		data = self.__clean_dict(category='admissions')
		return Admissions(data=data)

	@property
	def student(self) -> StudentBody:
		data = self.__clean_dict(category='student')
		return StudentBody(data=data)

	@property
	def cost(self) -> Tuition:
		data = self.__clean_dict(category='cost')
		return Tuition(data=data)

	def __str__(self) -> str:
		return f'{self.data[f"{self.year}.school.name"]} - {self.data[f"id"]}'

	def __eq__(self, other: object) -> bool:
		if self.data['id'] == other.data['id']:
			return True
		else:
			return False
