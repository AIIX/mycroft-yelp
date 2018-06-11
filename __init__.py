from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from yelpapi import YelpAPI


class YelpRestaurant(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(YelpRestaurant, self).__init__(name="YelpRestaurant")

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
        rating = search_results['businesses'][0]['rating']
        print(search_results['businesses'][0])
        self.speak_dialog("restaurant", data={
                          "restaurant_name": restaurant_name,
                          "rating": rating})


# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return YelpRestaurant()
