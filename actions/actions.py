import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from dotenv import load_dotenv
import os

load_dotenv()
class ActionFetchWeather(Action):
    def name(self):
        return "action_fetch_weather"

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot("location")
        if not location:
            dispatcher.utter_message("Please tell me your destination.")
            return []

        api_key = os.getenv("OPENWEATHER_API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url).json()

        if "main" in response:
            temp = response["main"]["temp"]
            desc = response["weather"][0]["description"]
            dispatcher.utter_message(f"The weather in {location} is {desc}, around {temp}°C.")
        else:
            dispatcher.utter_message("Couldn't fetch weather details.")
        return []

class ActionRecommendPacking(Action):
    def name(self):
        return "action_recommend_packing"

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot("location")
        suggestion = (
            f"For {location}, consider packing light clothes, sunscreen, and sunglasses. "
            "Also carry a jacket and umbrella just in case!"
        )
        dispatcher.utter_message(suggestion)
        return []