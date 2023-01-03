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
colleges = sc.search('Howard')
```

`search()` will return a list of `College` objects.

You can also search for a specific college using it's id.

```python
howard = sc.search(id=131520)
```

For further information you can read the [documentation](https://scorecard.readthedocs.io/en/latest/)
