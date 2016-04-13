from django.db import models

CLASSIFICATION_CHOICES = ()

class Sighting(models.Model):  #a collection, arranged for display



    url = models.CharField("Report URL", blank=True, null=True, max_length=255)
    classification = models.CharField(max_length=1, choices=CLASSIFICATION_CHOICES, default='C', blank=True, null=True)
    report_id = models.PositiveIntegerField(default=0, blank=False, null=False, unique=True)
    description = models.TextField(blank=True, null=True)
    year = Field()
    season = Field()
    month = Field()
    state = Field()
    county = Field()
    location_details = Field()
    nearest_town = Field()
    nearest_road = Field()
    observed = Field()
    also_noticed = Field()
    other_witnesses = Field()
    other_stories = Field()
    time_and_conditions = Field()
    environment = Field()
    follow_up = Field()
    about_investigator = Field()









    order = models.PositiveIntegerField(default=0, blank=False, null=False, unique=False)
    title =
    slug = models.SlugField(blank=True, null=True,
                            help_text="This will be auto generated from the title (and it will be unique).")
    cover_image = models.ImageField("Lookbook Image", upload_to="lookbooks/cover_images/",
                                  help_text="If no cover image is chosen, the first collection image will be used.",
                                  max_length=255, blank=True, null=True)

    landing_video = EmbedVideoField("Youtube Link", blank=True,
                                    help_text="This video will be linked to and displayed on the lookbook landing page.")
    video_title = models.CharField("Youtube Link Title", blank=True, null=True, default="WATCH THIS VIDEO",
                                   max_length=255)

    description =
    print_link = models.FileField("PDF", max_length=200, blank=True, upload_to="lookbooks/files/",
                                 null=True)
    published = models.BooleanField(default=False)

    class Meta(object):
        ordering = ('-order',)
        verbose_name = "Lookbook"
        verbose_name_plural = "Lookbooks"

    def __unicode__(self):
        return "%s" % (self.title)

























