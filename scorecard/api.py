"""Interface with the collegescorecard API."""
import requests
from .objects import College


class ScoreCard:
	def __init__(self, API_KEY: str) -> None:
		self.API_KEY = API_KEY

	def search(self, name: str, page=0, per_page=20, year='latest') -> College:
		"""Search for a college by name."""
		params = {
			'api_key': self.API_KEY,
			'school.name': name,
			'page': page,
			'per_page': per_page,
			'_fields': f'{year}.school,{year}.student,id'
                    }
		r = requests.get(
			'https://api.data.gov/ed/collegescorecard/v1/schools.json', params=params)
		results = r.json()['results']

		college_list = []
		for i in results:
			college_list.append(College(data=i, year=year))

		return college_list

	def get_by_id(self, id: int, year='latest'):
		"""Query a college by it's id."""
		params = {
			'api_key': self.API_KEY,
			'_fields': f'{year}.school,{year}.student,id',
			'id': id,
                    }
		r = requests.get(
			'https://api.data.gov/ed/collegescorecard/v1/schools.json', params=params)

		# Despite only returning one result, the API returns a list with one element.
		# So I need to append the [0] to select the first result.
		results = r.json()['results'][0]

		return College(data=results, year=year)
