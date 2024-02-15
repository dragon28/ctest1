from django.db import models

class DemoTable(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)

    class Meta:
        db_table = 'demo_table'
