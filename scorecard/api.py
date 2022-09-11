"""Interface with the collegescorecard API."""
import requests
from objects import College


class ScoreCard:
	def __init__(self, API_KEY: str) -> None:
		self.API_KEY = API_KEY

	def search(self, name: str, page=0, per_page=20) -> College:
		"""Search for a college by name."""
		params = {
			'api_key': self.API_KEY,
			'school.name': name,
			'page': page,
			'per_page': per_page,
			'_fields': 'school,id'
                }
		r = requests.get(
			'https://api.data.gov/ed/collegescorecard/v1/schools.json', params=params)
		results = r.json()['results']

		college_list = []
		for i in results:
			college_list.append(College(data=i))

		return college_list
