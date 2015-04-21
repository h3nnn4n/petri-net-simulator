#!/usr/bin/python3

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Wrote in April 2015 by Renan S. Silva

"""


# net = ([],[],[],[])
#
# Where the first list is the places
# the second list is the transitions
# the third is the edges
# and the fourth is the tokens

def get_poscondition_matrix(net):
    places = net[0]
    trans = net[1]
    edges = net[2]

    matrix = []

    for i in range(len(places)):
        matrix.append([0 for x in range(len(trans))])

    pl = dict(zip(places,[x for x in range(len(places))]))
    tr = dict(zip(trans ,[x for x in range(len(trans ))]))

    for edge in edges:
        if edge[0] in trans:
            matrix[pl[edge[1]]][tr[edge[0]]] = 1

    return matrix

def print_poscondition_matrix(net):

    matrix = get_poscondition_matrix(net)

    for i in matrix:
        print(i)

def get_precondition_matrix(net):
    places = net[0]
    trans = net[1]
    edges = net[2]

    matrix = []

    for i in range(len(places)):
        matrix.append([0 for x in range(len(trans))])

    pl = dict(zip(places,[x for x in range(len(places))]))
    tr = dict(zip(trans ,[x for x in range(len(trans ))]))

    for edge in edges:
        if edge[0] in places:
            matrix[pl[edge[0]]][tr[edge[1]]] = 1

    return matrix

def print_precondition_matrix(net):

    matrix = get_precondition_matrix(net)

    for i in matrix:
        print(i)

def get_incidence_matrix(net):
    places = net[0]
    trans = net[1]
    edges = net[2]

    matrix = []

    for i in range(len(places)):
        matrix.append([0 for x in range(len(trans))])

    I = get_precondition_matrix(net)
    O = get_poscondition_matrix(net)

    for x in range(len(places)):
        for y in range(len(trans)):
            matrix[x][y] = O[x][y] - I[x][y]

    return matrix

def print_incidence_matrix(net):

    matrix = get_incidence_matrix(net)

    for i in matrix:
        print(i)

def test_conectivity(net):
    places = net[0]
    trans = net[1]
    edges = net[2]

    # Makes a list with both places and transitions
    todo = []
    todo.extend(places)
    todo.extend(trans)

    # Makes a second set for the visited vertex
    x = todo.pop()
    do = set()
    do.add(x)

    while todo:
        old = todo.copy()
        doing = do.copy()

        for x in doing:
            for i in edges:

                if i[0] == x:
                    do.add(i[1])
                    if i[1] in todo:
                        todo.remove(i[1])

                if i[1] == x:
                    do.add(i[0])
                    if i[0] in todo:
                        todo.remove(i[0])
                        if old == todo:
                            return False

    return True

def is_pure(net):
    edges = set()

    for edge in net[2]:
        edges.add((edge[0], edge[1]))

    for edge in edges:
        if (edge[1], edge[0]) in edges:
            return False

    return True

def input_arc_sane(net, a):
    places = net[0]
    trans = net[1]
    if a not in places:
        if a not in trans:
            print("Error: Loose arc!")
            return False

    if a in places and a in trans:
        print("Error: Duplicated state")
        return False

    return True

def input_arc_really_sane(net, a, b):
    places = net[0]
    trans = net[1]

    if a in places and b in trans:
        return True

    if b in places and a in trans:
        return True

    print("Error: Something is messy!")
    return False

def insert_edge(net, a, b, weigth=1):
    if input_arc_sane(net, a) == False or input_arc_sane(net, b) == False:
        return

    if input_arc_really_sane(net, a, b) == False:
        return

    net[2].append((a, b, weigth))

def insert_place(net, place):
    if place not in net[0] and place not in net[1]:
        net[0].append(place)
    else:
        print("Error: This already exists!")

def insert_transtion(net, transition):
    if transition not in net[1] and transition not in net[0]:
        net[1].append(transition)
    else:
        print("Error: This already exists!")

def set_token(net, place, token):
    for i in net[3]:
        if i[0] == place:
            i[0] = token
            return

    net[3].append((place,token))

def print_places(net):
    if len(net[0]) > 0:
        print("Places are:")
        for place in net[0]:
            print(place, end=" ")
            print("")
    else:
        print("No place yet.")

def print_transitions(net):
    if len(net[1]) > 0:
        print("Transitions are:")
        for transition in net[1]:
            print(transition, end=" ")
            print("")
    else:
        print("No transition yet.")

def print_edges(net):
    if len(net[2]) > 0:
        print("Edges are:")
        for edge in net[2]:
            print(str(edge[0]) + ' -> ' + str(edge[1]))
            print("")
    else:
        print("No edge yet.")

def print_tokens(net):
    if len(net[3]) > 0:
        print("Tokens are:")
        for token in net[3]:
            print(str(token[0]) + ' = ' + str(token[1]))
            print("")
    else:
        print("No token yet.")

def print_net(net):
    print_places(net)
    print_transitions(net)
    print_edges(net)
    print_tokens(net)

def main():
    nets = []
    nets.append(([],[],[],[]))

    active_net = nets[0]

    while True:
        cmd = input('> ').split(' ')

        if cmd[0] not in ['#','%','//'] and cmd[0] != '':
        print(cmd)

        if cmd[0] in ['quit','exit','close']:
            break

        if cmd[0] in ['#','%','//']:
        continue

        if cmd[0] == 'test':
            if len(cmd) > 1:
                if cmd[1] in 'connectivity':
                    print(test_conectivity(active_net))
                    if cmd[1] in ['purity','pure']:
                        print(is_pure(active_net))
                    else:
                        pass

        if cmd[0] == 'print':
            if len(cmd) > 1:
                if cmd[1] in 'transitions':
                    print_transitions(active_net)
                elif cmd[1] in 'places':
                    print_places(active_net)
                elif cmd[1] in 'edges':
                    print_edges(active_net)
                elif cmd[1] in 'tokens':
                    print_tokens(active_net)
                elif cmd[1] in 'precondition':
                    print_precondition_matrix(active_net)
                elif cmd[1] in 'poscondition':
                    print_poscondition_matrix(active_net)
                elif cmd[1] in 'incidence':
                    print_incidence_matrix(active_net)
                else:
                    print_net(active_net)

        if cmd[0] == 'insert':
            if len(cmd) > 2:
                if cmd[1] in 'places':
                    argc = len(cmd) - 2
                    for i in range(0,argc):
                        insert_place(active_net, cmd[i+2])
                elif cmd[1] in 'transitions':
                    argc = len(cmd) - 2
                    for i in range(0, argc):
                        insert_transtion(active_net, cmd[i+2])
                elif cmd[1] in ['arc','vertex']:
                    argc = len(cmd) - 2
                    if argc < 3 or argc > 4:
                        print("Error: Unexpected something!")
                    else:
                        if argc == 3:
                            insert_edge(active_net, cmd[2], cmd[4])
                        else:
                            insert_edge(active_net, cmd[2], cmd[4], cmd[5])

        if cmd[0] == 'set':
            if len(cmd) > 1:
                if cmd[1] in 'tokens':
                    if len(cmd) == 4:
                        set_token(active_net, cmd[2], cmd[3])

main()
