from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG


class YelpRestaurant(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(YelpRestaurant, self).__init__(name="YelpRestaurant")

    # This handle is used to lookup a restaurant near the person's location
    @intent_handler(IntentBuilder("").require("Restaurant").require("food_type"))
    def handle_find_restaurant_intent(self, message):
        food_type = message.data['food_type']
        print(food_type)
        self.speak_dialog("restaurant")


# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return YelpRestaurant()
