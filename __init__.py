import base64
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from yelpapi import YelpAPI
from requests import get
from mycroft.messagebus.message import Message


class YelpRestaurant(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(YelpRestaurant, self).__init__(name="YelpRestaurant")
        self.restaurant_phone = ''
        self.restaurant_address = ''
        self.rating = ''
        self.is_closed = False
        self.json_response = ''
        self.index = 0

    # This handle is used to lookup a restaurant near the person's location
    @intent_handler(IntentBuilder("")
                    .require("YelpPlace")
                    .require("place"))
    def handle_find_restaurant_intent(self, message):
        dt = self.settings.get('key')
        api_key = base64.b64decode(dt).decode("utf-8")
        zip_code = self.settings.get('zipcode')
        yelp_api = YelpAPI(api_key)
        location = self.location
        place = message.data['place']
        longitude = location['coordinate']['longitude']
        latitude = location['coordinate']['latitude']
        search_results = yelp_api.search_query(term=place,
                                               latitude=latitude,
                                               longitude=longitude,
                                               limit='5',
                                               sort_by='best_match')
        print(search_results)
        businesses = search_results['businesses'][self.index]
        restaurant_name = businesses['name']
        restaurant_phone = businesses['display_phone']
        restaurant_rating = int(businesses['rating'])
        restaurant_location = businesses['location']['display_address'][0] + \
            " " + \
            businesses['location']['display_address'][1]
        restaurant_open = businesses['is_closed']
        restaurant_url = businesses['url']
        restaurant_imageurl = businesses['image_url']
        restaurant_price = businesses['price']
        self.json_response = search_results
        self.set_context('RestaurantName', restaurant_name)
        self.restaurant_phone = restaurant_phone
        self.rating = restaurant_rating
        self.restaurant_address = restaurant_location
        self.is_closed = restaurant_open
        rating = businesses['rating']
        resultstospeak = "{0} was the best match with a rating of {1} stars".format(restaurant_name, restaurant_rating)
        self.speak(resultstospeak)
        self.enclosure.bus.emit(
            Message(
                "metadata",
                { 'type': "mycroft-yelp",
                  'datablob': search_results
                }
            )
        )

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return YelpRestaurant()
