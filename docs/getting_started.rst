.. _getting_started:

***************
Getting Started
***************
Learn how to use scorecard.

API Access
==========
An API key is required to use the college scorecard API. You can apply for one for free `here <https://collegescorecard.ed.gov/data/documentation/>`_.

Starter Code
============


.. code-block:: python3

	from scorecard.api import ScoreCard

	sc = ScoreCard(api_key)

	for college in sc.search('Howard'):
		print(str(college))
	
This example will search for and return the name of every college with the name "Howard" in it and return it's name and id.

If you know a specific colleges id, you can query that one specifically.

.. code-block:: python3

	from scorecard.api import ScoreCard

	sc = ScoreCard(api_key)

	print(sc.get_by_id(131520))