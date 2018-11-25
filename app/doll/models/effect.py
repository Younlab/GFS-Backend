from django.contrib.postgres.fields import ArrayField
from django.db import models

__all__ = (
    'Effect',
    'EffectGrid',
)


class Effect(models.Model):
    doll = models.ForeignKey(
        'Doll',
        on_delete=models.CASCADE,
    )
    type = models.CharField(max_length=10)
    center = models.PositiveSmallIntegerField()
    pos = ArrayField(
        ArrayField(
            models.PositiveSmallIntegerField(),
        ),
    )


class EffectGrid(models.Model):
    effect = models.ForeignKey(
        'Effect',
        on_delete=models.CASCADE,
    )
    pow = models.PositiveIntegerField()
    hit = models.PositiveIntegerField()
    rate = models.PositiveIntegerField()
    dodge = models.PositiveIntegerField()
    critical_percent = models.PositiveIntegerField()
    cool_down = models.PositiveIntegerField()
    armor = models.PositiveIntegerField()
