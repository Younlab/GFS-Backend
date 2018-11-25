from django.db import models

from .doll import Doll

__all__ = (
    'Skill',
    'SkillData',
)


class Skill(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
    )
    code_name = models.CharField(max_length=50)
    skill_image = models.ImageField(upload_to='skill_image', blank=True, null=True)
    skill_type = models.CharField(max_length=20)
    cool_down_type = models.CharField(max_length=30)
    initial_cool_down = models.PositiveIntegerField()
    consumption = models.PositiveIntegerField()


class SkillData(models.Model):
    skill = models.ForeignKey(
        'Skill',
        on_delete=models.CASCADE,
    )
    level = models.PositiveSmallIntegerField(blank=True, null=True)
    cool_down = models.PositiveIntegerField(blank=True, null=True)
