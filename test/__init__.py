from test.integrationtests.skills.skill_tester import SkillTest
from unittest.mock import MagicMock

json_response = {'id': 'LeHWKBOD_klTuyOOROBnRQ',
                 'alias': 'sushi-iwa-clayton-clayton-2',
                 'name': 'Sushi Iwa Clayton',
                 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/VCpbqrIJE9pFjhUbidyn0Q/o.jpg',
                 'is_closed': False,
                 'url': 'https://www.yelp.com/biz/sushi-iwa-clayton-clayton-2?adjust_creative=q-p1D6Eu9I--5Izrrb1AuA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=q-p1D6Eu9I--5Izrrb1AuA',
                 'review_count': 32,
                 'categories': [{'alias': 'sushi', 'title': 'Sushi Bars'},
                                {'alias': 'asianfusion', 'title': 'Asian Fusion'},
                                {'alias': 'thai', 'title': 'Thai'}],
                 'rating': 4.5,
                 'coordinates':
                     {'latitude': 35.65473,
                      'longitude': -78.47785},
                 'transactions': [],
                 'price': '$$',
                 'location': {
                     'address1': '11629 US-70 Bus',
                     'address2': None,
                     'address3': '',
                     'city': 'Clayton',
                     'zip_code': '27520',
                     'country': 'US',
                     'state': 'NC',
                     'display_address': [
                         '11629 US-70 Bus',
                         'Clayton, NC 27520']},
                 'phone': '+19195856140',
                 'display_phone': '(919) 585-6140',
                 'distance': 1751.161429011724}


def test_runner(skill, example, emitter, loader):
    s = [s for s in loader.skills if s and s.root_dir == skill]
    s[0].yelp_api = mock.MagicMock()
    s[0].yelp_api.search_query.return_value = json_response
    return SkillTest(skill, example, emitter).run(loader)