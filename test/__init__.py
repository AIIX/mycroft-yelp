from test.integrationtests.skills.skill_tester import SkillTest
from unittest.mock import MagicMock, patch
from mycroft.util.log import getLogger

LOGGER = getLogger(__name__)

json_response = {'businesses': [{'alias': 'sushi-iwa-clayton-clayton-2',
   'categories': [{'alias': 'sushi', 'title': 'Sushi Bars'},
    {'alias': 'asianfusion', 'title': 'Asian Fusion'},
    {'alias': 'thai', 'title': 'Thai'}],
   'coordinates': {'latitude': 35.65473, 'longitude': -78.47785},
   'display_phone': '(919) 585-6140',
   'distance': 1751.161429011724,
   'id': 'LeHWKBOD_klTuyOOROBnRQ',
   'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/VCpbqrIJE9pFjhUbidyn0Q/o.jpg',
   'is_closed': False,
   'location': {'address1': '11629 US-70 Bus',
    'address2': None,
    'address3': '',
    'city': 'Clayton',
    'country': 'US',
    'display_address': ['11629 US-70 Bus', 'Clayton, NC 27520'],
    'state': 'NC',
    'zip_code': '27520'},
   'name': 'Sushi Iwa Clayton',
   'phone': '+19195856140',
   'price': '$$',
   'rating': 4.5,
   'review_count': 32,
   'transactions': [],
   'url': 'https://www.yelp.com/biz/sushi-iwa-clayton-clayton-2?adjust_creative=q-p1D6Eu9I--5Izrrb1AuA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=q-p1D6Eu9I--5Izrrb1AuA'}]}


def test_runner(skill, example, emitter, loader):
    s = [s for s in loader.skills if s and s.root_dir == skill]
    with patch(s[0].__module__ + '.YelpAPI.search_query') as m:
        s[0].is_closed = json_response['businesses'][0]['is_closed']
        s[0].restaurant_phone = json_response['businesses'][0]['phone']
        s[0].restaurant_address = json_response['businesses'][0]['location']['display_address'][0] + \
                              " " + json_response['businesses'][0]['location']['display_address'][1]
        m.return_value = json_response
        return SkillTest(skill, example, emitter).run(loader)