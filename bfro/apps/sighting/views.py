from django.views.generic import TemplateView
from django.shortcuts import render
from timelinejs.models import Timeline
from django.http import JsonResponse
from bfro.apps.sighting.models import Sighting
from django.shortcuts import redirect
import json

from django.core.cache import cache

class MapView(TemplateView):
    template_name = "map.html"

    def get(self, request, *args, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)

        timeline = Timeline.objects.get(pk=1)




        return render(request, self.template_name, {

            'timeline': timeline


        })


def sightings_view(request):
    timeline = Timeline.objects.get(pk=1)
    json_data = """
    {
        "timeline":
        {
            "headline":"%s",
            "type":"default",
            "text":"<p>%s</p>",
            "asset": {
                "media":"/media/imgs/sasquatch.png",
                "credit":"%s",
                "caption":"%s"
            },
            "date": [
    """ % (timeline.headline, timeline.text, timeline.asset_credit, timeline.asset_caption)
    sightings = Sighting.objects.all()
    count = 1
    max = len(sightings)
    for sighting in sightings:
        #print count, max

        json_data += """

                {
                    "startDate":"%s",
                    "endDate":"%s",
                    "headline":"%s",
                    "text":"<p>%s</p>",
                    "tag":"This is Optional",
                    "classname":"%s"

                }""" % (sighting.date, sighting.date, "%s %s %s" % (sighting.report_id, sighting.season, sighting.year), sighting.description.replace('"','\\"'), sighting.report_id)
        #print count<max
        if count<max:
            json_data += ""","""

        #print json_data
        count+=1

    json_data += """
            ],
            "era": [
                {
                    "startDate":"2011,12,10",
                    "endDate":"2011,12,11",
                    "headline":"Headline Goes Here",
                    "text":"<p>Body text goes here, some HTML is OK</p>",
                    "tag":"This is Optional"
                }

            ]
        }
    }
    """
    #print json_data
    return JsonResponse(json.loads(json_data))



