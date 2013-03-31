# -*- coding:Utf-8 -*-

import os
import sys
import pytz
from os.path import join
from json import loads, dumps
from dateutil.parser import parse

from django.db import transaction, connection, reset_queries
from django.utils.timezone import make_aware
from django.core.management.base import BaseCommand

from django_parltrack_votes_data.models import VotesData


class Command(BaseCommand):
    help = 'Import vote data of the European Parliament, this is needed to be able to create voting recommendations'

    def handle(self, *args, **options):
        print "Clean old downloaded files"
        os.system("rm %s %s" % (join("/tmp", "ep_votes.json"), join("/tmp", "ep_votes.json.xz")))
        print "Download vote data from parltrack"
        os.system("wget -O %s http://parltrack.euwiki.org/dumps/ep_votes.json.xz" % join("/tmp", "ep_votes.json.xz"))
        print "unxz it"
        os.system("unxz %s" % join("/tmp", "ep_votes.json.xz"))
        print "cleaning old votes data..."
        connection.cursor().execute("DELETE FROM django_parltrack_votes_data_recommendationdata")
        transaction.commit_unless_managed()
        print VotesData.objects.count()
        print "read file"
        current_json = ""
        a = 1
        with transaction.commit_on_success():
        # I need to parse the json file by hand, otherwise this eat way to much memory
            for i in open(join("/tmp", "ep_votes.json"), "r"):
                if i in ("[{\n", "{\n"):
                    # print "begin doc"
                    current_json += "{\n"
                elif "}\n" == i:
                    # print "end"
                    current_json += "\n}"
                    vote = loads(current_json)
                    VotesData.objects.create(proposal_name=vote.get("report", vote["title"]),
                                            title=vote["title"],
                                            data=dumps(vote, indent=4),
                                            date=make_aware(parse(vote["ts"]), pytz.timezone("Europe/Brussels"))),
                    reset_queries() # to avoid memleaks in debug mode
                    current_json = ""
                    sys.stdout.write("%s\r" % a)
                    sys.stdout.flush()
                    a += 1
                elif i == ",\n":
                    pass
                else:
                    current_json += i
            sys.stdout.write("\n")

# vim:set shiftwidth=4 tabstop=4 expandtab:
