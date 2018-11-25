from django.contrib.postgres.fields import ArrayField
from django.db import models

__all__ = (
    'Voice',
)


class Voice(models.Model):
    doll = models.ForeignKey(
        'Doll',
        on_delete=models.CASCADE,
    )
    dialogue01 = models.TextField(blank=True, null=True)
    dialogue02 = models.TextField(blank=True, null=True)
    dialogue03 = models.TextField(blank=True, null=True)
    introduce = models.TextField(blank=True, null=True)
    allhallows = models.TextField(blank=True, null=True)
    dialogue_wedding = models.TextField(blank=True, null=True)
    soul_contract = ArrayField(
        ArrayField(
            models.TextField(blank=True, null=True)
        ),
    )
    gain = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Voice : {self.doll.code_name}'
