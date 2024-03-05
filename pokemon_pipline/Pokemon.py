from typing import List


class Pokemon:
    """
    id: int - the id of the pokemon
    name: str - name of the pokemon
    types: tuple(str) - (main type, sub type)
    height: float
    weight: float
    stats: dict(tuple(str,int)) - {(name,base_stat)} hp, attack, defense, special-attack, special-defense, speed
    """

    def __init__(self, ID: int, name: str, types: List[dict], height: float, weight: float, stats: dict) -> None:
        self.id = ID
        self.name = name
        self.types = self.marshal_pokemon_type_data(types)
        self.height = height
        self.weight = weight
        self.stats = stats

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
        :param json_data: len either 1 or 2, in form : list({'slot': (1 or 2), 'type': {'name': (type), 'url': (url)}})
        :return: tuple in form (type1, type2), if no type 2 then None
        """
        size_json: int = len(json_data)
        output_types: List[str] = [None, None]

        for i, item in enumerate(json_data):
            output_types[i] = item['type']['name']

        return tuple(output_types)

