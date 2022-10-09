# Getting Started

## Importing

First, import the `ScoreCard` object to start using the library.

```python
from scorecard.api import ScoreCard
```

## Search for a College

Initialize a `ScoreCard` object with your API key.

```
sc = ScoreCard('API_KEY')
```

Replace `'API_KEY'` with your college scorecard API key.

Query for a college using it's id.

```python
sc.search('New York University')
```

`sc.search` will return a list of `College` objects.

## Query a College

If you know a college by it's id, you can query that specific college.

```python
sc.get_by_id(193900)
```
