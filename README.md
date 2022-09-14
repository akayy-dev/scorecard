# scorecard

A python library for collegescorecard.ed.gov

## Getting Started

Before you do anything, you're going to need an API key. You can apply for one [here](https://collegescorecard.ed.gov/data/documentation/).

Then import the `ScoreCard` class.

```python
from scorecard.api import ScoreCard
```

Create a `ScoreCard` instance.

```python
sc = ScoreCard(API_KEY='your api key')
```

Search for a college

```python
colleges = sc.search('Howard University')
```

`search()` will return a list of `College` objects.

You can also search for a specific college using it's id.

```python
howard = sc.search(id=131520)
```

## The `College` Object

- `College.name` returns the name of the college.
- `College.location` returns a dictionary with the city, state, and zip code of the campus.
- `College.gender_breakdown` returns a dictionary with the percentage of males and females.
- `College.undergrad` returns the amount of undergrad students.
- `College.acceptance_rate` returns the acceptance rate.
- `College.sat_scores` returns a dictionary with the math, writing, critical reading, and overall SAT scores.
- `College.tuition` returns a dictionary with the in-state and out-of-state tuition. If the university is a private one, both the in-state and out-of-state tuition will be the same,
