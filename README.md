# Girls Frontline Simulator
- 개인적인 학습 목적으로 만드는 게임 `소녀전선` 시뮬레이터 입니다.
- 데이터는 [36Base](https://github.com/36base) 의 데이터를 사용합니다.
- 상업적으로 사용되지 않습니다.

## Requirements
- django
- psycopg2-binary
- pillow
- djangorestframework
- django-filter
- requests

## Command

Pipenv install

```sh
# Pipfile and Pipfile.lock exists
pipenv install
```

Crawling Command

```sh
./manage.py update_doll
```