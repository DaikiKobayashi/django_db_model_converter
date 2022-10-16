from django.db import models 

class PlayerLevelMaster(models.Model):
    level = models.IntegerField(null=True, blank=True, default=0)
    exp = models.BigIntegerField(null=True, blank=True, default=0)

    class Meta:
        app_label = 'app'

class CardLevelMaster(models.Model):
    level = models.IntegerField(null=True, blank=True, default=0)
    rank = models.IntegerField(null=True, blank=True, default=0)
    exp = models.BigIntegerField(null=True, blank=True, default=0)

    class Meta:
        app_label = 'app'

