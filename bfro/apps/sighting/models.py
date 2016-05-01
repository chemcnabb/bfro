from django.db import models

CLASSIFICATION_CHOICES = (

)

class Sighting(models.Model):  #a collection, arranged for display
    url = models.CharField("Report URL", blank=True, null=True, max_length=255)
    classification = models.CharField(max_length=1, choices=CLASSIFICATION_CHOICES, default='A', blank=True, null=True)
    report_id = models.PositiveIntegerField(default=0, blank=False, null=False, unique=True)
    latitude = models.DecimalField(max_digits=25, decimal_places=6)
    longitude = models.DecimalField(max_digits=25, decimal_places=6)
    date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    year = models.CharField("Year", blank=True, null=True, max_length=255)
    season = models.CharField("Season", blank=True, null=True, max_length=255)
    month = models.CharField("Month", blank=True, null=True, max_length=255)
    day = models.CharField("Day", blank=True, null=True, max_length=255)
    state = models.CharField("State", blank=True, null=True, max_length=255)
    county = models.CharField("County", blank=True, null=True, max_length=255)
    location_details = models.TextField(blank=True, null=True)
    nearest_town = models.CharField("County", blank=True, null=True, max_length=255)
    nearest_road = models.CharField("County", blank=True, null=True, max_length=255)
    observed = models.TextField(blank=True, null=True)
    also_noticed = models.TextField(blank=True, null=True)
    other_witnesses = models.TextField(blank=True, null=True)
    other_stories = models.TextField(blank=True, null=True)
    time_and_conditions = models.TextField(blank=True, null=True)
    environment = models.TextField(blank=True, null=True)
    follow_up = models.TextField(blank=True, null=True)
    about_investigator = models.TextField(blank=True, null=True)

    class Meta(object):
        ordering = ('-date',)
        verbose_name = "Sighting"
        verbose_name_plural = "Sightings"

    def __unicode__(self):
        return "%s %s %s" % (self.report_id, self.classification, self.year)

























