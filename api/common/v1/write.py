import json

from api.common.main.models import Country

f = open('../../../country.json', 'r')

obj = json.load(f)

for i in obj:
    country = Country.objects.create(
        name=i['name'],
        flag_img=i['flag'],
        code=i['number']
    )
    country.save()

print('Vse')
