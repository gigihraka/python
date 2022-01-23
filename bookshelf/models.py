from django.utils.translation import gettext_lazy as _
from django.db import models


class Bookshelf(models.Model):
    # define columns
    judul = models.CharField(max_length=100)
    penulis = models.CharField(max_length=100)
    tahun = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # define table name
        db_table = 'bookshelf'