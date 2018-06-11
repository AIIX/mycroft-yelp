# Yelp Restaurant Finder [![Build Status](https://travis-ci.org/btotharye/mycroft-yelp.svg?branch=master)](https://travis-ci.org/btotharye/mycroft-yelp) [![Coverage Status](https://coveralls.io/repos/github/btotharye/mycroft-yelp/badge.svg?branch=master)](https://coveralls.io/github/btotharye/mycroft-yelp?branch=master)
Finds restaurants via the Yelp API

## Description 
Finds restaurants via the Yelp API

## Examples 
* "I need a place to eat dinner"
* "Need a place to eat sushi"
* "find me a place to eat sushi"
* "find me a place to eat dinner"

Can also do context so once it finds the best result "more info" will give the phone number, address and if they are open

## Setting Up API Token
You will need to go to https://www.yelp.com/developers/v3/manage_app and create a app which will then give you a api token you will put into the home.mycroft.ai settings page for this skill.

The zip code is not required, if you don't put a zip code in it will use the location from the mycroft home settings.

## Screenshot Example
Here is what from the Mycroft CLI the response looks like currently, plans to have this come with all the info including the address and such as a text message using IFTTT webhooks.

![yelp screenshot](https://github.com/btotharye/mycroft-yelp/blob/master/yelp_ss.png)


## Credits 
btotharye
