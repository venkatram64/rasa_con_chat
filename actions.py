from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
"""
step 1: virtualenv con_chat

C:\Users\venkatram.veerareddy\my_rasa_chat>C:\\Users\\venkatram.veerareddy\\Anaconda3\\Scripts\activate my_con_chat

rasa-nlu-trainer --source Desktop/weather_bot/data/data.json

https://rasahq.github.io/rasa-nlu-trainer/
"""

class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = '******' # enter your api key
        client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        current = client.getCurrentWeather(q=loc)

        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temp_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']

        response = """It is currently {} in {} at the moment.  The temperature is
                        {} degrees, the humidity is {}% and the wind speed is {} mph"""\
                        .format(condition, city, temp_c, humidity, wind_mph)
        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]
