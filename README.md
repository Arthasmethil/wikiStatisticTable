# wikiStatisticTable

The project that uses Pytest, Request, bs4 

Its algorithm:
1. Gets access to the table on the [wiki](https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites)
2. Receives and processes table into dataclass Website.
3. Parametrized test checks popularity of the programming languages on websites from the table on wiki.
4. Asserts data and prints error_log if it finds an error.
