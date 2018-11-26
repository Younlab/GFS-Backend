import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from doll.models import *


class Command(BaseCommand):
    help = 'Update Database data, doll model'

    def __init__(self):
        super().__init__()
        self.base_url = 'https://raw.githubusercontent.com/36base/'
        self.doll_data = requests.get(f'{self.base_url}girlsfrontline-core/master/data/doll.json').json()
        self.doll_image_data = 'https://github.com/36base/girlsfrontline-resources/blob/master/pic/pic_'
        self.skill_image_data = f'{self.base_url}girlsfrontline-resources/master/icon/skillicon/'
        self.voice_data = requests.get(
            f'{self.base_url}girlsfrontline-extra-data/master/data/locale/ko-KR/NewCharacterVoice.json'
        ).json()

    def handle(self, *args, **options):
        def none_zero(value):
            if not value:
                value = 0
            return value

        def skill_value_data(key, value):
            items = key[value]
            skill_data = {
                'data': {
                    'code_name': items['codename'],
                    'cool_down_type': items['cooldownType'],
                    'initial_cool_down': items['initialCooldown'],
                    'consumption': items['consumption']
                },
                'data_pool': items.get('dataPool')
            }
            return skill_data

        for item in self.doll_data:
            default_data = {
                'id': item['id'],
                'code_name': item['codename'],
                'type': item['type'].upper(),
                'rank': item['rank'],
                'grow': item['grow'],
                'build_time': item['buildTime'],
                'obtain': item['obtain'],
                'slot_01': item['equip1'],
                'slot_02': item['equip2'],
                'slot_03': item['equip3'],
            }
            status_data = {
                'hp': item['stats']['hp'],
                'pow': item['stats']['pow'],
                'hit': item['stats']['hit'],
                'dodge': item['stats']['dodge'],
                'rate': item['stats']['rate'],
                'armor_piercing': item['stats']['armorPiercing'],
                'critical_harm_rate': none_zero(item['stats'].get('criticalHarmRate')),
                'critical_percent': none_zero(item['stats']['criticalPercent']),
                'bullet': none_zero(item['stats'].get('bullet')),
                'speed': none_zero(item['stats'].get('speed')),
                'night_view': none_zero(item['stats'].get('nightView')),
                'armor': none_zero(item['stats'].get('armor')),
            }

            image = f'{self.doll_image_data}{item.get("codename").lower()}.png?raw=true'
            image_d = f'{self.doll_image_data}{item.get("codename").lower()}_D.png?raw=true'

            effect_data = {
                'type': item['effect']['effectType'].upper(),
                'center': item['effect']['effectCenter'],
                'pos': item['effect']['effectPos'],
            }

            effect_grid_data = {
                'pow': none_zero(item['effect']['gridEffect'].get('pow')),
                'hit': none_zero(item['effect']['gridEffect'].get('hit')),
                'rate': none_zero(item['effect']['gridEffect'].get('rate')),
                'dodge': none_zero(item['effect']['gridEffect'].get('dodge')),
                'critical_percent': none_zero(item['effect']['gridEffect'].get('critical_percent')),
                'cool_down': none_zero(item['effect']['gridEffect'].get('cool_down')),
                'armor': none_zero(item['effect']['gridEffect'].get('armor')),
            }

            doll, doll_create = Doll.objects.prefetch_related('voice_set', 'status_set').update_or_create(
                id=item['id'],
                defaults=default_data,
            )

            doll.image.save(
                f'{item["codename"]}.png', ContentFile(requests.get(image).content)
            )
            doll.image_d.save(
                f'{item["codename"]}_d.png', ContentFile(requests.get(image_d).content)
            )

            doll.status_set.update_or_create(
                defaults=status_data,
            )

            effect, effect_create = Effect.objects.prefetch_related('effectgrid_set').update_or_create(
                doll_id=item['id'],
                defaults=effect_data,
            )
            effect.effectgrid_set.update_or_create(
                defaults=effect_grid_data,
            )

            voice_item = self.voice_data.get(item['codename'])
            if not voice_item:
                pass
            else:
                voice_data = {
                    'dialogue01': voice_item.get('dialogue1'),
                    'dialogue02': voice_item.get('dialogue2'),
                    'dialogue03': voice_item.get('dialogue3'),
                    'introduce': voice_item.get('introduce'),
                    'allhallows': voice_item.get('allhallows'),
                    'soul_contract': voice_item.get('soulcontract'),
                    'dialogue_wedding': voice_item.get('dialoguewedding'),
                    'gain': voice_item.get('gain'),
                }

                doll.voice_set.update_or_create(
                    defaults=voice_data
                )

            skill_data = skill_value_data(item, 'skill1')
            skill_image = f'{self.skill_image_data}{skill_data["data"]["code_name"].lower()}.png?raw=true'
            skill, skill_create = Skill.objects.prefetch_related('skilldata_set').update_or_create(
                doll_id=item['id'],
                skill_type='Basic',
                defaults=skill_data['data']
            )

            skill.skill_image.save(
                f'{skill_data["data"]["code_name"]}.png', ContentFile(requests.get(skill_image).content)
            )
            for data_pool in skill_data['data_pool']:
                skill.skilldata_set.update_or_create(
                    level=data_pool.get('level'),
                    cool_down=data_pool.get('cooldown')
                )

            if not item.get('skill2'):
                pass
            else:
                skill_data = skill_value_data(item, 'skill2')
                skill, skill_create = Skill.objects.prefetch_related('skilldata_set').update_or_create(
                    doll_id=item['id'],
                    skill_type='Additional',
                    defaults=skill_data['data']
                )
                skill.skill_image.save(
                    f'{skill_data["data"]["code_name"]}.png', ContentFile(requests.get(skill_image).content)
                )
                for data_pool in skill_data['data_pool']:
                    skill.skilldata_set.update_or_create(
                        level=data_pool.get('level'),
                        cool_down=data_pool.get('cooldown')
                    )

            if doll_create is True:
                print(f'{item.get("codename")} 생성 완료')
            else:
                print(f'{item.get("codename")} 업데이트 완료')
