# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from typing import Any, Text, Dict, List, Optional
from rasa_sdk import  Tracker
from rasa_sdk.executor import CollectingDispatcher, Action
from rasa_sdk.forms import FormValidationAction, REQUESTED_SLOT
from rasa_sdk.types import DomainDict
from rasa_sdk.events import AllSlotsReset, SlotSet, EventType, ConversationPaused, UserUttered, ConversationResumed, Restarted, FollowupAction, UserUtteranceReverted, ReminderScheduled, ReminderCancelled, ActionReverted
import logging
import datetime
from pytz import timezone, utc
import requests
import json





# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class SendRcForm(Action):

    def name(self) -> Text:
        return "action_send_rc_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionSetReminderUserSatisfactionCheck(Action):

    def name(self) -> Text:
        return "action_set_reminder_usat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        date = datetime.datetime.now() + datetime.timedelta(minutes=0.5)
        entities = tracker.latest_message.get("entities")
        sender_id=tracker.current_state()["sender_id"]
        reminder = ReminderScheduled(
            "EXTERNAL_ticket_reminder_user_satisfaction",
            trigger_date_time=date,
            entities=entities,
            name=sender_id,
            kill_on_user_message=False,
        )

        return [reminder]

        
