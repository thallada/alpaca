from django.db import models


class Alpaca(models.Model):
    """
    Holds a url to an alpaca image for user's viewing pleasure.

    Not currently storing images on-site because of storage space concerns. As much
    as I like alpacas, I don't need my server completely flooded with them.
    """
    url = models.URLField()
    alt = models.TextField('Alt Text', blank=True)

    def __unicode__(self):
        if self.alt and len(self.alt) > 100:
            return (self.alt[:100] + '...')
        elif self.alt:
            return self.alt
        else:
            return self.url
