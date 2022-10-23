from django.db import models 

class PlayerLevelMaster(models.Model):
    level = models.IntegerField(null=True, blank=True, default=0)
    exp = models.BigIntegerField(null=True, blank=True, default=0)
    test1 = models.BooleanField(null=True, blank=True)
    test2 = models.TextField(null=True, blank=True, max_length=100)
    test3 = models.DateTimeField(null=True, blank=True, default='2001-01-20')
    test4 = models.FloatField(null=True, blank=True, default=0.001)
    test5 = models.PositiveIntegerField(null=True, blank=True, default=1000)

    class Meta:
        app_label = 'app'

class CardLevelMaster(models.Model):
    level = models.IntegerField(null=True, blank=True, default=0)
    rank = models.IntegerField(null=True, blank=True, default=0)
    exp = models.BigIntegerField(null=True, blank=True, default=0)

    class Meta:
        app_label = 'app'

