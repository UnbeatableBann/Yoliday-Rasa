import os
import requests
import csv
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from dotenv import load_dotenv
from rasa_sdk.events import AllSlotsReset
from sanic.response import json
from rapidfuzz import process, fuzz

load_dotenv()

# This file contains custom actions for the Rasa chatbot to handle weather queries and packing recommendations.
class ActionFetchWeather(Action):
    def name(self) -> Text:
        return "action_fetch_weather"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        API_KEY = os.getenv("OPENWEATHER_API_KEY")
        if not API_KEY:
            dispatcher.utter_message("Error: OpenWeatherMap is not available. Please set the OPENWEATHER_API_KEY environment variable.")
            return []
        
        location = tracker.get_slot("location")
        if not location:
            dispatcher.utter_message("I don't know the city. Please specify a destination.")
            return []
        """# Fuzzy match the location to known cities
        best_match, score, _ = process.extractOne(location, CITIES, scorer=fuzz.ratio)
        if score < 80:
            dispatcher.utter_message(f"Sorry, I couldn't recognize the city '{location}'. Please check the spelling or try another city.")
            return [SlotSet("weather_description", None)]
        location = best_match"""
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url)
            response.raise_for_status()
            response = response.json()

            if response["cod"] != 200:
                dispatcher.utter_message(f"Sorry, I couldn't find the weather for given location: {location}.")
                return [SlotSet("weather_description", None)]
            
            desc = response["weather"][0]["description"]
            temp = response["main"]["temp"]
            dispatcher.utter_message(f"The current weather in {location} is {desc} with a temperature of {temp}°C.")
            return [SlotSet("weather_description", desc)]
        
        except requests.exceptions.RequestException as e:
            dispatcher.utter_message(f"{e}")
            return [SlotSet("weather_description", None)]
        except KeyError:
            dispatcher.utter_message(f"Sorry, I couldn't find the weather for {location}. Please check the city name and try again.")
            return [SlotSet("weather_description", None)]

# This action fetches the weather for a specified city using the OpenWeatherMap API and sets the weather description slot.
class ActionRecommendPacking(Action):

    def name(self) -> Text:
        return "action_recommend_packing"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        weather_desc = tracker.get_slot("weather_description")
        location = tracker.get_slot("location")
        if not weather_desc:
            dispatcher.utter_message(f"I don't have the weather information for {location}. Please check the city name and try again.")
            return []
        
        packing_list = []
        if "rain" in weather_desc or "drizzle" in weather_desc:
            packing_list.append("an umbrella")
            packing_list.append("a raincoat")
        if "clear" in weather_desc or "sun" in weather_desc:
            packing_list.append("sunglasses")
            packing_list.append("sunscreen")
        if "clouds" in weather_desc:
            packing_list.append("a light jacket")
        if "snow" in weather_desc:
            packing_list.append("a warm coat, gloves, and a scarf")
        if not packing_list:
            message = "Based on the weather, standard clothing should be fine. Enjoy your trip!"
        else:
            recommendation = ", ".join(packing_list)
            message = f"Based on the weather in {location}, I recommend you to pack: {recommendation}."
        dispatcher.utter_message(message)
        return []

# This action resets all slots in the tracker, allowing the user to start a new conversation without previous context.
class ActionResetSlots(Action):

    def name(self) -> Text:
        return "action_reset_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [AllSlotsReset()]

# This action provides an advanced itinerary plan for popular locations and a generic plan for others, using location and dates from slots.
class ActionPlanItineraryAdvanced(Action):
    def name(self) -> Text:
        return "action_plan_itinerary_advanced"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("location")
        start_date = tracker.get_slot("start_date")
        end_date = tracker.get_slot("end_date")

        if not location or not start_date or not end_date:
            dispatcher.utter_message("Please provide your destination and travel dates so I can plan your itinerary!")
            return []

        # Generate a generic, dynamic itinerary for any location
        plan = [
            f"Arrive in {location}, check-in and relax.",
            f"Explore local attractions, museums, or parks in {location}.",
            f"Try popular local food and visit a cultural site.",
            f"Enjoy leisure activities, shopping, or a day trip nearby.",
            f"Wrap up your trip, last-minute sightseeing, and prepare for departure."
        ]

        message = (
            f"Here’s a suggested itinerary for your trip to {location} from {start_date} to {end_date}:\n\n" +
            "\n".join([f"Day {i+1}: {activity}" for i, activity in enumerate(plan)]) +
            f"\n\nLet me know if you want more details or recommendations for {location}!"
        )
        dispatcher.utter_message(message)
        return []