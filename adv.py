from room import Room
from player import Player
from world import World

from util import Stack, Queue
from graph import Graph

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# reverse helper


def reverse(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'


# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []
prev_room = None
all_exits = None
directions = None
curr_room = player.current_room.id

visited = {}

s = Stack()
s.push([directions, curr_room, prev_room])


while s.size() > 0:
    path = s.pop()
    direction = path[0]
    current_room = path[1]
    prev_room = path[2]

    print(current_room)

    if current_room not in visited:

        visited[current_room] = {}
        exits = player.current_room.get_exits()

        for room_exit in exits:
            visited[current_room][room_exit] = '?'

        print(visited, "this is visited")

        for key, value in visited.items():

            for index, item in value.items():

                print(item, "item")
                if item == '?':
                    prev_room = current_room
                    print(prev_room, "------------")
                    player.travel(index)
                    traversal_path.append(index)
                    value[index] = player.current_room.id
                    s.push([index,  player.current_room.id, prev_room])

print(visited)


# ALL ITEMS ARE IN THE
# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
