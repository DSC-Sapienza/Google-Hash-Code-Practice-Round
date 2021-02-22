from dataclasses import dataclass
from typing import *



@dataclass
class Input:
    #teams[card] e' il numero di teams che ha "card" membri
    teams: dict

    # la lista di pizze, dove una pizza e' un insieme di ingr.
    pizzas: list

    @property
    def total_pizzas(self):
        return len(self.pizzas)

    @staticmethod
    def from_string(file_name):
        with open(file_name, 'r') as file_reader:
            list_of_line: List[str] = file_reader.readlines() # list of string where string is a line with the '\n'
            
            _, num_team_2, num_team_3, num_team_4 = [int(elem) for elem in list_of_line[0].strip().split(" ")]

            return Input(
                teams= { 2: num_team_2, 3: num_team_3, 4: num_team_4 },
                pizzas=[
                    set(line.strip().split(" ")[1:]) for idx, line in enumerate(list_of_line) if idx != 0
                ]
            )


@dataclass
class Delivery:
    team_card: int
    pizzas_received: List[int]


@dataclass
class Output:
    receives: List[Delivery]

    def to_string(self):
        pizzas_card = len(self.receives)
        header = [str(pizzas_card)]
        rest = [" ".join([str(receive.team_card) ] + [str(pizza_id) for pizza_id in receive.pizzas_received]) for receive in self.receives]
        return "\n".join(header + rest)


def wrap_solution(filename):
    def decorator(solution):
        inp = Input.from_string(filename)
        output = solution(inp).to_string()
        # print(output) # or write in file?
        with open(filename+'.out.txt', 'w') as file_writer:
            file_writer.write(output)
    return decorator

