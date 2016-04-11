from django.views.generic import TemplateView
from django.shortcuts import render


from django.shortcuts import redirect


from django.core.cache import cache

class MapView(TemplateView):
    template_name = "map.html"

    def get(self, request, *args, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        sightings = []




        return render(request, self.template_name, {
            'sightings': sightings


        })




