"""Interface with the collegescorecard API."""
from typing import List

import requests

from scorecard.exceptions import InvalidAPIKey, MissingAPIKey

from .objects import College


class ScoreCard:
	def __init__(self, API_KEY: str) -> None:
		self.API_KEY = API_KEY

		# Chek API key for validity.
		params = {'api_key': self.API_KEY}

		try:
			r = requests.get(
				'https://api.data.gov/ed/collegescorecard/v1/schools.json', params=params)
			error_code = r.json()['error']['code']
			print(error_code)

			# If the API key is invalid.
			if error_code == 'API_KEY_INVALID':
				raise InvalidAPIKey()
			# If user inputs a blank string as a key.
			elif error_code == 'API_KEY_MISSING':
				raise MissingAPIKey()

		# If API key is valid.
		except KeyError:
			pass

	def search(self, name: str, page=0, per_page=20, year='latest') -> List[College]:
		"""Search for a college by name."""
		params = {
			'api_key': self.API_KEY,
			'school.name': name,
			'page': page,
			'per_page': per_page,
			'_fields': f'{year}.school,{year}.student,{year}.admissions,{year}.cost,id',
                    }
		r = requests.get(
			'https://api.data.gov/ed/collegescorecard/v1/schools.json', params=params)
		results = r.json()['results']

		college_list = []
		for i in results:
			college_list.append(College(data=i, year=year))

		return college_list

	def get_by_id(self, id: int, year='latest') -> College:
		"""Query a college by it's id."""
		params = {
			'api_key': self.API_KEY,
			'_fields': f'{year}.school,{year}.student,{year}.admissions,{year}.cost,id',
			'id': id,
                    }
		r = requests.get(
			'https://api.data.gov/ed/collegescorecard/v1/schools.json', params=params)

		# Despite only returning one result, the API returns a list with one element.
		# So I need to append the [0] to select the first result.
		results = r.json()['results'][0]

		return College(data=results, year=year)
