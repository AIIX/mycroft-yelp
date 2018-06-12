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
        self.is_closed = False
        self.json_response = ''
        self.index = 0

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
        longitude = location['coordinate']['longitude']
        latitude = location['coordinate']['latitude']
        search_results = yelp_api.search_query(term=food_type,
                                               latitude=latitude,
                                               longitude=longitude,
                                               limit='5',
                                               sort_by='best_match')
        businesses = search_results['businesses'][self.index]
        restaurant_name = businesses['name']
        restaurant_phone = businesses['phone']
        restaurant_rating = businesses['rating']
        restaurant_location = businesses['location']['display_address'][0] + \
            " " + \
            businesses['location']['display_address'][1]
        restaurant_open = businesses['is_closed']
        self.json_response = search_results
        self.set_context('RestaurantName', restaurant_name)
        self.restaurant_phone = restaurant_phone
        self.rating = restaurant_rating
        self.restaurant_address = restaurant_location
        self.is_closed = restaurant_open
        rating = businesses['rating']
        self.speak_dialog("restaurant", data={
                          "restaurant_name": restaurant_name,
                          "rating": rating})

    @intent_handler(IntentBuilder("")
                    .require('RestaurantName')
                    .require('MoreInformation'))
    def handle_more_info(self, message):
        json_response = self.json_response
        businesses = json_response['businesses'][int(self.index)]
        restaurant_name = businesses['name']
        restaurant_phone = businesses['phone']
        restaurant_location = businesses['location']['display_address'][0] + \
            " " + \
            businesses['location']['display_address'][1]
        if businesses['is_closed'] is True:
            restaurant_open = 'closed'
        else:
            restaurant_open = 'open'
        self.speak_dialog("moreinfo", data={
                          "restaurant_name": restaurant_name,
                          "phone_number": restaurant_phone,
                          "address": restaurant_location,
                          "is_closed": restaurant_open})

    @intent_handler(IntentBuilder("")
                    .require("NextResult"))
    def handle_next_result(self, message):
        self.index += 1
        print(self.index)
        json_response = self.json_response
        print("This is the json response: {}".format(json_response))
        if int(self.index) <= 4:
            businesses = json_response['businesses'][int(self.index)]
            restaurant_name = businesses['name']
            restaurant_phone = businesses['phone']
            restaurant_location = businesses['location']['display_address'][0] + \
                " " + \
                businesses['location']['display_address'][1]
            if businesses['is_closed'] is True:
                restaurant_open = 'closed'
            else:
                restaurant_open = 'open'
            self.speak_dialog("next.result", data={
                "restaurant_name": restaurant_name,
                "rating": businesses['rating']})
        else:
            response = self.get_response('startover')
            if response == 'yes':
                self.index = 0
                json_response = self.json_response
                businesses = json_response['businesses'][int(self.index)]
                restaurant_name = businesses['name']
                restaurant_phone = businesses['phone']
                restaurant_location = businesses['location']['display_address'][0] + \
                    " " + \
                    businesses['location']['display_address'][1]
                if businesses['is_closed'] is True:
                    restaurant_open = 'closed'
                else:
                    restaurant_open = 'open'
                self.speak_dialog("restaurant", data={
                    "restaurant_name": restaurant_name,
                    "rating": businesses['rating']})
            if response == 'no':
                self.speak("Ok, thanks for using the yelp restaurant finder.")


# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return YelpRestaurant()
