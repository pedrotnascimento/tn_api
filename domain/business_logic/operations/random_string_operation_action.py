import requests
from domain.business_logic.operation_action_abstract import OperationActionAbstract


class RandomStringGenerationOperationAction(OperationActionAbstract):
    def __init__(self):
        self.type = "random_string_generation"

    def operate(self) -> str:
        api = "https://www.random.org/strings/?num=1&len=8&digits=on&upperalpha=on&loweralpha=on&format=plain"
        response= requests.get(api)
        random_string =response.text
        return str.strip(random_string)
