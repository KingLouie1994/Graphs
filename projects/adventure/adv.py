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
map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

options = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
backtracked_path = []
visited = {}

visited[0] = player.current_room.get_exits()

while len(visited) < len(room_graph) - 1:
    if player.current_room.id not in visited:
        last_visited_room = backtracked_path[-1]
        visited[player.current_room.id] = player.current_room.get_exits()
        visited[player.current_room.id].remove(last_visited_room)
    while len(visited[player.current_room.id]) < 1:
        prev_path = backtracked_path.pop()
        traversal_path.append(prev_path)
        player.travel(prev_path)
    else:
        prev_exit = visited[player.current_room.id].pop()
        backtracked_path.append(options[prev_exit])
        traversal_path.append(prev_exit)
        player.travel(prev_exit)
print("You visited all rooms!")

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
