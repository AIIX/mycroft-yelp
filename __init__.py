from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from yelpapi import YelpAPI


class YelpRestaurant(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(YelpRestaurant, self).__init__(name="YelpRestaurant")
        self.restaurant_phone = ''
        self.restaurant_address = ''
        self.rating = ''
        self.is_open = False

    # This handle is used to lookup a restaurant near the person's location
    @intent_handler(IntentBuilder("")
                    .require("Restaurant")
                    .require("food_type"))
    def handle_find_restaurant_intent(self, message):
        api_key = self.settings.get('key')
        zip_code = self.settings.get('zipcode')
        yelp_api = YelpAPI(api_key)
        location = self.location
        food_type = message.data['food_type']
        if zip_code:
            print("The zip code is: {}".format(zip_code))
        longitude = location['coordinate']['longitude']
        latitude = location['coordinate']['latitude']
        search_results = yelp_api.search_query(term=food_type,
                                               latitude=latitude,
                                               longitude=longitude,
                                               limit='5',
                                               sort_by='best_match')
        restaurant_name = search_results['businesses'][0]['name']
        restaurant_phone = search_results['businesses'][0]['phone']
        restaurant_rating = search_results['businesses'][0]['rating']
        restaurant_location = search_results['businesses'][0]['location']['display_address'][0] + \
            " " + \
            search_results['businesses'][0]['location']['display_address'][1]
        restaurant_open = search_results['businesses'][0]['is_closed']
        self.set_context('RestaurantName', restaurant_name)
        self.restaurant_phone = restaurant_phone
        self.rating = restaurant_rating
        self.restaurant_address = restaurant_location
        self.is_closed = restaurant_open
        rating = search_results['businesses'][0]['rating']
        print(search_results['businesses'][0])
        self.speak_dialog("restaurant", data={
                          "restaurant_name": restaurant_name,
                          "rating": rating})

    @intent_handler(IntentBuilder("")
                    .require('RestaurantName')
                    .require('MoreInformation'))
    def handle_more_info(self, message):
        print(message.data)
        restaurant_name = message.data.get('RestaurantName')
        restaurant_phone = self.restaurant_phone
        restaurant_location = self.restaurant_address
        if self.is_closed is True:
            restaurant_open = 'closed'
        else:
            restaurant_open = 'open'

        restaurant_rating = self.rating
        print("This is the restaurant name: {}".format(restaurant_name))
        print("This is the restaurant phone: {}".format(restaurant_phone))
        self.speak_dialog("moreinfo", data={
                          "restaurant_name": restaurant_name,
                          "phone_number": restaurant_phone,
                          "address": restaurant_location,
                          "is_closed": restaurant_open})


# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return YelpRestaurant()
