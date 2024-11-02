import json
import random
import glob
from ResponseInfo import ResponseInfo
from Order import Order


class Automaton:
    def __init__(self, mt, states, finals, initialState):
        self.mt = mt
        self.states = states
        self.state = initialState
        self.finals = finals
        self.order = Order()
        self.responses = self.load_responses()

    def extract_menu(self):
        for response in self.responses:
            if 'menu' in response:
                return response['menu']
        return None

    def print_menu(self):
        for item in self.extract_menu():
            print(
                f"{item['title']} - ${item['price']:.2f}")

    def print_menu_item_description(self, menuItem):
        menu = self.extract_menu()
        for item in menu:
            if item["name"] == menuItem:
                print(item["description"])
                break

    def print_menu_item_price(self, menuItem):
        menu = self.extract_menu()
        for item in menu:
            if item["name"] == menuItem:
                print(item["price"])
                break

    def get_menu_item(self, words):
        best_item = None
        highest_weight = 0
        potential_items = []

        for response in self.responses:
            if 'menu_items' in response:
                menu_items = response['menu_items']
                for item_key, item in menu_items.items():
                    total_weight = 0
                    triggers = item.get("triggers")

                    if triggers:
                        for trigger, weight in triggers.items():
                            if trigger in words:
                                total_weight += weight

                    if total_weight > highest_weight:
                        highest_weight = total_weight
                        best_item = item["name"]
                        potential_items = [best_item]

                    elif total_weight == highest_weight and total_weight > 0:
                        potential_items.append(item["name"])

        if len(potential_items) > 1 or (best_item and highest_weight < 100):
            print("Sé más específico referente al producto, por favor.")
        elif best_item and highest_weight >= 100:
            return best_item
        else:
            print("Lo siento, no entiendo.")

        return None

    def load_responses(self):
        responses = []
        for filename in glob.glob('data/*.json'):
            with open(filename, 'r', encoding='utf-8') as f:
                responses.append(json.load(f))
        return responses

    def check_word(self, word):
        words = word.lower().split()
        responseInfo = ResponseInfo()

        for responseData in self.responses:
            transitionValue = responseData.get("transition")
            dialogue = responseData.get("dialogue")

            if dialogue:
                for itemKey, item in dialogue.items():
                    totalWeight = 0
                    triggers = item.get("triggers")

                    if triggers:
                        for trigger, weight in triggers.items():
                            if trigger in words:
                                totalWeight += weight

                    if totalWeight > responseInfo.highestWeight:
                        responseInfo.highestWeight = totalWeight
                        responseInfo.bestResponse = random.choice(
                            item['responses'])
                        responseInfo.bestTransition = transitionValue
                        responseInfo.potentialResponses = [
                            responseInfo.bestResponse]
                        responseInfo.itemKey = itemKey

                    elif totalWeight == responseInfo.highestWeight and totalWeight > 0:
                        responseInfo.potentialResponses.append(
                            random.choice(item['responses']))

        if len(responseInfo.potentialResponses) > 1 or responseInfo.bestResponse and responseInfo.highestWeight < 100:
            print("Sé más específico porfavor.")

        elif responseInfo.bestResponse and responseInfo.highestWeight >= 100:
            self.state = self.mt[self.state][responseInfo.bestTransition]
            print("new State: ", self.state)
            if self.state in self.finals:
                exit()
            print(responseInfo.bestResponse)

            if self.state == 2:
                if responseInfo.itemKey == "1":
                    self.print_menu()

                elif responseInfo.itemKey == "2":
                    menuItem = self.get_menu_item(words)
                    self.print_menu_item_description(menuItem)

                elif responseInfo.itemKey == "3":
                    menuItem = self.get_menu_item(words)
                    self.print_menu_item_price(menuItem)

            elif self.state == 3:
                if responseInfo.itemKey == "1":
                    menuItem = self.get_menu_item(words)
                    for item in self.extract_menu():
                        if item["name"] == menuItem:
                            self.order.add_item(menuItem, item["price"])
                            break

                if responseInfo.itemKey == "2":
                    menuItem = self.get_menu_item(words)
                    self.order.remove_item(menuItem)
        else:
            print("Lo siento, no entiendo.")

    def run(self):
        while True:
            userInput = input(">> ")
            if userInput.lower() == 'salir':
                print("bye.")
                break

            self.check_word(userInput)


mt = [
    [1, 2, 3, 0, 0, 0, 8],
    [1, 2, 3, 1, 1, 1, 8],
    [2, 2, 3, 2, 2, 2, 8],
    [3, 4, 3, 5, 6, 7, 8],
    [4, 4, 3, 5, 6, 7, 8],
    [5, 4, 3, 5, 6, 7, 8],
    [6, 4, 3, 5, 6, 7, 8],
    [7, 7, 7, 7, 7, 7, 8],
    [8, 8, 8, 8, 8, 8, 8],
]
states = [0, 1, 2, 3, 4, 5, 6, 7, 8]
initialState = 0
finals = [8]

automaton = Automaton(mt, states, finals, initialState)
automaton.run()
