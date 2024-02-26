"""Interface with the collegescorecard API."""
from typing import List

import requests

from scorecard.exceptions import InvalidAPIKey, MissingAPIKey
from scorecard.objects import College


class ScoreCard:
	""" This is the main class used to search for colleges and their data.

	:param API_KEY: The API key used to interact with college scorecards API.
	"""
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

	def search(self, name: str = None, page=0, per_page=20, year='latest', filters: dict = None) -> List[College]:
		"""Search for a college by name.
		
		:param name: The name of the target college
		:type name: str, optional
		:param page: What page to query the data from
		:type page: int, optional
		:param per_page: How many results to show per page, defaults to 20
		:type per_page: int, optional
		:param year: What year to retrieve the data from, defaults to latest availible year
		:type year: str, optional
		:param filters: Additional filters to apply to the search (see https://collegescorecard.ed.gov/assets/CollegeScorecardDataDictionary.xlsx)
		:type filters: dict, optional
		"""
		params = {
			'api_key': self.API_KEY,
			'school.name': name,
			'_fields': f'{year}.school,{year}.student,{year}.admissions,{year}.cost,id',
			'page': page,
			'per_page': per_page,
			}

		if filters:
			params.update(filters)

		r = requests.get(
			'https://api.data.gov/ed/collegescorecard/v1/schools.json', params=params)
		results = r.json()['results']

		college_list = []
		for i in results:
			college_list.append(College(data=i, year=year))

		return college_list

	def get_by_id(self, id: int, year='latest') -> College:
		"""Query a college by it's id.
		
		:param id: The id of the college you want to search.
		:param year: What year to retrieve the data from, defaults to latest availible year.
		:type year: str, optional
		"""
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
