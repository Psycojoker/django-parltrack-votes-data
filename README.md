Introduction
============

Votes data of the European Parliament importation (from [parltrack](https://parltrack.euwiki.org)) and models extracted from [memopol](https://memopol.lqdn.fr) [code base](https://gitorious.org/memopol2-0).

In other words, this is the *RAW*"data of all the votes of the European Parliament. You won't have direct links to Member of the European parliament with this.

Data Schema
===========

There is only one model: VotesData, it contains the data from parltrack with will be used to create more useful vote data.

To import the votes, run:

    python manage.py import_ep_votes_data

Licence
=======

Like memopol: aGPLv3+
