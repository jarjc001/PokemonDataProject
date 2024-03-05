from typing import List, Dict


class Pokemon:
    """
    id: int - the id of the pokemon
    name: str - name of the pokemon
    types: tuple(str) - (main type, sub type)
    height: float
    weight: float
    stats: dict(tuple(str,int)) - {(name,base_stat)} hp, attack, defense, special-attack, special-defense, speed
    """

    # """
    # Base init to get a new pokemon from manual input
    # """
    #
    # def __init__(self, ID: int, name: str, types: tuple, height: float, weight: float, stats: dict) -> None:
    #     self.id = ID
    #     self.name = name
    #     self.types = types
    #     self.height = height
    #     self.weight = weight
    #     self.stats = stats

    """
    Create a Pokemon object from a JSON Get request
    """
    def __init__(self, json_request: dict) -> None:
        self.id = json_request['id']
        self.name = json_request['name']
        self.types = self.marshal_pokemon_type_data(json_request['types'])
        self.height = json_request['height']
        self.weight = json_request['weight']
        self.stats = self.marshal_pokemon_stats_data(json_request['stats'])

    def __str__(self) -> str:
        return f"Pokemon: id = {self.id}, " \
               f"name = {self.name}, " \
               f"types = {self.types}, " \
               f"height = {self.height}, " \
               f"weight = {self.weight}, " \
               f"stats = {self.stats}"

    def marshal_pokemon_type_data(self, json_data: List[dict]) -> tuple:
        """
        To make the pokemon's data easy to transfer to storage,
        will change the types data from the Json into a more readable form
        :param json_data: in form of list({'slot': (1 or 2), 'type': {'name': ~, 'url': (url)}})
        :return: tuple in form (type1, type2), if no type 2 then None
        """
        output_types: List[str] = [None, None]

        for i, item in enumerate(json_data):
            output_types[i] = item['type']['name']

        return tuple(output_types)

    def marshal_pokemon_stats_data(self, json_data: List[dict]) -> dict:
        """
        To make the pokemon's data easy to transfer to storage,
        will change the stats data from the Json into a more readable form
        :param json_data: in form of list({'base_stat': ~, 'effort': ~, 'stat': {'name': ~, 'url': (url)}})
        :return: dict in form {"stat name: str", "base_stat: int") len = 6
        """
        output_stats: dict = {}

        for item in json_data:
            output_stats[item['stat']['name']] = item['base_stat']

        return output_stats
