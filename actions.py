# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from rasa_sdk.events import SlotSet, UserUtteranceReverted
from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class BookRoomInfo(FormAction):
    def name(self) -> Text:
        return "form_book_room"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["number", "room_type"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        # utter submit template
        dispatcher.utter_message(
            template="utter_submit", number=tracker.get_slot('number'),room_type=tracker.get_slot('room_type')
            )
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "number": self.from_entity(entity="number", intent='num_rooms'),
            "room_type": self.from_entity(entity="room_type",intent="type_rooms")
        }

class BookRoomNumberInfo(FormAction):
    def name(self) -> Text:
        return "form_book_room_number"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["room_type"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        # utter submit template
        dispatcher.utter_message(template="utter_submit", 
                                room_type=tracker.get_slot('room_type'))
        return []

    # def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

    #     return {
    #         "room_type": self.from_entity(entity="room_type", intent="type_rooms")
    #     }

