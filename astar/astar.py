import random
from queue import PriorityQueue

# Konfigurationer för kartan
MAP_SIZE_X = 20
MAP_SIZE_Y = 10
OBSTACLES = 20

class Graph():
    """Klass för skapandet av en karta."""
    def __init__(self, xmax, ymax):
        self.map = self.generate_map(xmax, ymax)
        self.xmax = xmax
        self.ymax = ymax

    def generate_map(self, xmax, ymax):
        """Metod som skapar kartans koordinater och bestämmer vilka som är hinder."""
        map_ = {}

        # Initierar möjliga x- och y-koordinater samt ger dem värdet 1.
        for x in range(xmax):
            for y in range(ymax):
                map_[(x, y)] = 1

        x = random.randint(0, xmax - 1)
        y = random.randint(0, ymax - 1)

        # Bestämmer vilka rutor som är hinder och ger dem värdet -1.
        for obstacle in range(OBSTACLES):
            while map_[(x, y)] < 0:
                x = random.randint(0, xmax - 1)
                y = random.randint(0, ymax - 1)
            map_[(x, y)] = -1

        return map_

    def neighbors(self, coords):
        """Metod för att hitta grannar för en given koordinat."""
        x, y = coords
        possible_steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        nbs = []

        for x_step, y_step in possible_steps:
            nb = (x + x_step, y + y_step)
            if self.map.get(nb, -1) > 0:
                nbs.append(nb)
        return nbs

    def cost(self, current, next):
        """Metod för kostnaden att gå från den nuvarande till den undersökta rutan."""
        return 1


def heuristic(goal, next):
    """Funktion som beräknar manhattanavståndet mellan den undersökta rutan och målet."""
    x1, y1 = goal
    x2, y2 = next
    return abs(x1 - x2) + abs(y1 - y2)

def astar(graph, start, goal):
    """Funktion som beräknar närmsta väg mellan start och mål i en given karta."""
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    came_from[start] = None
    cost_so_far = {}
    cost_so_far[start] = 0

    while not frontier.empty():
       current = frontier.get()[1]

       # Sätter ihop vägen från mål tillbaka till start.
       if current == goal:
           path = []
           while current:
               path.append(current)
               current = came_from[current]
           return path

       # Väljer bästa väg utifrån lägsta kostnad.
       for next in graph.neighbors(current):
           new_cost = cost_so_far[current] + graph.cost(current, next)
           if next not in cost_so_far or new_cost < cost_so_far[next]:
               cost_so_far[next] = new_cost
               priority = new_cost + heuristic(goal, next)
               frontier.put((priority, next))
               came_from[next] = current

    return []


if __name__ == "__main__":
    # Skapar en karta.
    graph = Graph(MAP_SIZE_X, MAP_SIZE_Y)

    # Hittar närmsta vägen från det övre vänstra hörnet till det nedre högra hörnet.
    path = astar(graph, (0, 0), (MAP_SIZE_X - 1, MAP_SIZE_Y - 1))

    SYMBOLS = { 1: '.',
               -1: '#'}

    # Ritar upp kartan med "." som tomma ruton, "#" som hinder och "X" som den närmsta vägen.
    for y in range(MAP_SIZE_Y):
        line = ''
        for x in range(MAP_SIZE_X):
            if (x, y) in path:
                line += 'X'
            else:
                line += SYMBOLS[graph.map.get((x, y))]
        print(line)
