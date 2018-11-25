from django.contrib.postgres.fields import ArrayField
from django.db import models

__all__ = (
    'Doll',
    'Status',
)


class Doll(models.Model):
    id = models.PositiveIntegerField(unique=True, primary_key=True)
    code_name = models.CharField(max_length=50)
    rank = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=10)
    build_time = models.PositiveIntegerField()
    grow = models.PositiveIntegerField()
    image = models.ImageField(upload_to='doll_image')
    image_d = models.ImageField(upload_to='doll_image_d')
    obtain = ArrayField(
        ArrayField(
            models.PositiveSmallIntegerField()
        ),
    )
    slot_01 = ArrayField(
        ArrayField(
            models.CharField(max_length=20, blank=True, null=True),
        ),
    )
    slot_02 = ArrayField(
        ArrayField(
            models.CharField(max_length=20, blank=True, null=True),
        ),
    )
    slot_03 = ArrayField(
        ArrayField(
            models.CharField(max_length=20, blank=True, null=True),
        ),
    )

    def __str__(self):
        return self.code_name


class Status(models.Model):
    doll = models.ForeignKey(
        'Doll',
        on_delete=models.CASCADE,
    )
    hp = models.PositiveIntegerField()
    pow = models.PositiveIntegerField()
    hit = models.PositiveIntegerField()
    dodge = models.PositiveIntegerField()
    rate = models.PositiveIntegerField()
    armor_piercing = models.PositiveIntegerField()
    critical_harm_rate = models.PositiveIntegerField()
    critical_percent = models.PositiveIntegerField()
    bullet = models.PositiveIntegerField()
    speed = models.PositiveIntegerField()
    night_view = models.PositiveIntegerField()
    armor = models.PositiveIntegerField()

    class Meta:
        ordering = ['id']
