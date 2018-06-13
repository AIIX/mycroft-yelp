# Yelp Restaurant Finder [![Build Status](https://travis-ci.org/btotharye/mycroft-yelp.svg?branch=master)](https://travis-ci.org/btotharye/mycroft-yelp) [![codecov](https://codecov.io/gh/btotharye/mycroft-yelp/branch/master/graph/badge.svg)](https://codecov.io/gh/btotharye/mycroft-yelp)
Finds restaurants/bars/and other locations via the Yelp API

## Description 
Finds restaurants/bars/and other locations via the Yelp API

## Examples 
* "I need a place to eat dinner"
* "Need a place to eat sushi"
* "find me a place to eat sushi"
* "find me a place to eat dinner"
* "comic book stores near me"
* "yelp bars"
* "sushi restaurants by me"
* "sushi restaurants nearby"
* "more information" - Will give more information about the current restaurant using the context method
* "next restaurant" - Will go to next result and you can then ask for more information for the address and such 
* "previous restaurant" - Will go to the previous result
* "send info" - sends text message of restaurant name, rating, and yelp url
* "send information" - sends text message of restaurant name, rating, and yelp url
* "send it to me" - sends text message of restaurant name, rating, and yelp url
* "send me the results" - sends text message of restaurant name, rating, and yelp url

## Setting Up API Token
You will need to go to https://www.yelp.com/developers/v3/manage_app and create a app which will then give you a api token you will put into the home.mycroft.ai settings page for this skill.

The zip code is not required, if you don't put a zip code in it will use the location from the mycroft home settings.

## Setting up IFTTT Webhook for Text
In order to get the text messages when you ask `send info` we need to setup IFTTT webhook.

Follow [This](https://ifttt.com/create) link to setup a Webhook.  You will want to create a New Applet and select Webhook

1. Click the +this blue icon and select webhook.
2. Select the option "Receive a web request"
3. Put `mycroft_yelp` as the name of the event.
4. Select +that and select sms
5. Select send me a sms
6. Put the following as the message - `{{Value1}} Star Rating: {{Value2}} {{Value3}}`
7. Select create action
8. Hit finish on the next screen.
9. Now go to https://ifttt.com/maker_webhooks and select the Documentation section.
10. This will give you a URL that you will want to put in the home settings under the IFTTT URL section in order to receive the text messages. **Please note the {event} part of the URL is replaced with mycroft_yelp**
11. Now the skill should be able to send text messages when you say `send info`

## Screenshot Example
Here is what from the Mycroft CLI the response looks like currently, plans to have this come with all the info including the address and such as a text message using IFTTT webhooks.

![yelp screenshot](https://github.com/btotharye/mycroft-yelp/blob/master/yelp_ss.png)

![kde_screenshot](https://github.com/btotharye/mycroft-yelp/blob/master/kde_ss.jpg)

## Text Message Example
![text_ss](https://github.com/btotharye/mycroft-yelp/blob/master/text_message.jpg)

## Credits 
btotharye
