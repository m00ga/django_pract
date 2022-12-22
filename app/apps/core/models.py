from django.db import models

# Create your models here.

class Table(models.Model):
    TABLE_TYPE = (
        ("O", "Oval"),
        ("R", "Rectangle")
    )
    seats = models.IntegerField()
    table_type = models.CharField(max_length=1, choices=TABLE_TYPE)
    coord_x = models.IntegerField()
    coord_y = models.IntegerField()
    size_x = models.IntegerField()
    size_y = models.IntegerField()
    is_ordered = models.BooleanField(default=False)

class Board(models.Model):
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
