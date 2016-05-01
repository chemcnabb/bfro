from django.core.management.base import BaseCommand
import logging
import json
from bfro.apps.sighting.models import Sighting
from bs4 import BeautifulSoup
import urllib
from dateutil import parser


class Command(BaseCommand):
    help = 'migrates all tables to new database'
    logger = logging.getLogger(__name__)

    def handle(self, *args, **options):
        self.logger.info("testing log...")
        with open('bfro/apps/utility/management/sightings_report.json') as data_file:
            data = json.load(data_file)

        class_A_reports = data["kml"]["Document"]["Folder"]["Folder"][0]["Folder"]
        class_B_reports = data["kml"]["Document"]["Folder"]["Folder"][1]["Folder"]
        class_C_reports = data["kml"]["Document"]["Folder"]["Folder"][2]["Folder"]

        for report in class_A_reports:
            # pprint(report)

            latitude = report["LookAt"]["latitude"]
            longitude = report["LookAt"]["longitude"]

            placemark = []
            try:
                placemark = report["Placemark"][0]
            except KeyError:
                placemark = report["Placemark"]

            time_string = placemark["TimeStamp"]["when"]
            time = parser.parse(time_string)
            report_url = placemark["description"]['center'][0]['b']['a']['_href']
            report_id = (placemark["description"]['center'][1]['i']['a']['_href']).replace(
                "http://www.bfro.net/gdb/comments.asp?BadLocationID=", "")
            description = " ".join([d.strip() for d in (placemark["description"]["b"]).splitlines()])

            year = ""
            season = ""
            month = ""
            day = ""
            state = ""
            county = ""
            location_details = ""
            nearest_town = ""
            nearest_road = ""
            observed = ""
            also_noticed = ""
            other_witnesses = ""
            other_stories = ""
            time_and_conditions = ""

            bfro_report = urllib.urlopen(report_url).read()
            # with open('test.html') as html:
            #     bfro_report = html.read()

            soup = BeautifulSoup(bfro_report, "lxml")

            fields = soup.find_all("span", class_="field")
            for field in fields:

                if field.parent.contents[0].string == "YEAR:":
                    year = field.parent.contents[1].string
                if field.parent.contents[0].string == "SEASON:":
                    season = field.parent.contents[1].string
                if field.parent.contents[0].string == "MONTH:":
                    month = field.parent.contents[1].string
                if field.parent.contents[0].string == "DATE:":
                    day = field.parent.contents[1].string
                if field.parent.contents[0].string == "STATE:":
                    state = field.parent.contents[1].string
                if field.parent.contents[0].string == "COUNTY:":
                    county = field.parent.contents[1].string
                if field.parent.contents[0].string == "LOCATION DETAILS:":
                    location_details = field.parent.contents[1].string
                if field.parent.contents[0].string == "NEAREST TOWN:":
                    nearest_town = field.parent.contents[1].string
                if field.parent.contents[0].string == "NEAREST ROAD:":
                    nearest_road = field.parent.contents[1].string
                if field.parent.contents[0].string == "OBSERVED:":
                    observed = field.parent.contents[1].string
                if field.parent.contents[0].string == "ALSO NOTICED:":
                    also_noticed = field.parent.contents[1].string
                if field.parent.contents[0].string == "OTHER WITNESSES:":
                    other_witnesses = field.parent.contents[1].string
                if field.parent.contents[0].string == "OTHER STORIES:":
                    other_stories = field.parent.contents[1].string
                if field.parent.contents[0].string == "TIME AND CONDITIONS:":
                    time_and_conditions = field.parent.contents[1].string

            print "getting report:", report_id
            try:
                sighting = Sighting.objects.get(report_id=report_id)
            except:
                sighting = Sighting()

            sighting.latitude=latitude
            sighting.longitude=longitude
            sighting.date=time
            sighting.description=description
            sighting.url=report_url
            sighting.report_id=report_id
            sighting.year=year
            sighting.season=season
            sighting.month=month
            sighting.day=day
            sighting.state=state
            sighting.county=county
            sighting.location_details=location_details
            sighting.nearest_town=nearest_town
            sighting.nearest_road=nearest_road
            sighting.observed=observed
            sighting.also_noticed=also_noticed
            sighting.other_witnesses=other_witnesses
            sighting.other_stories=other_stories
            sighting.time_and_conditions=time_and_conditions


            sighting.save()
