#!/usr/bin/python3

# net = ([],[],[],[])
#
# Where the first list is the places
# the second list is the transitions
# the third is the edges
# and the fourth is the tokens

def input_arc_sane(net, a):
    places = net[0]
    trans = net[1]


    if a not in places:
        if a not in trans:
            print("Error: Loose arc!")
            return False

    return True

def input_arc_really_sane(net, a, b):
    places = net[0]
    trans = net[1]

    if a in places and b in trans:
        return True

    if b in places and a in trans:
        return True

    print("Error: ???")
    return False

def insert_edge(net, a, b, weigth=1):
    if input_arc_sane(net, a) == False or input_arc_sane(net, b) == False:
        return

    if input_arc_really_sane(net, a, b) == False:
        return

    net[2].append((a, b, weigth))

def insert_place(net, place):
    if place not in net[0]:
        net[0].append(place)

def insert_transtion(net, transition):
    if transition not in net[1]:
        net[1].append(transition)

def print_places(net):
    if len(net[0]) > 0:
        print("Places are:")
        for place in net[0]:
            print(place, end=" ")
        print("")
    else:
        print("No place yet.")

def print_transitions(net):
    if len(net[0]) > 0:
        print("Transitions are:")
        for transition in net[1]:
            print(transition, end=" ")
        print("")
    else:
        print("No transition yet.")

def print_edges(net):
    if len(net[0]) > 0:
        print("Edges are:")
        for edge in net[2]:
            print(edge, end=" ")
        print("")
    else:
        print("No edge yet.")

def print_tokens(net):
    if len(net[0]) > 0:
        print("Tokens are:")
        for token in net[3]:
            print(token, end=" ")
        print("")
    else:
        print("No token yet.")

def print_net(net):
    print_places(net)
    print_transitions(net)
    print_edges(net)
    print_tokens(net)

def menu():
    nets = []
    nets.append(([],[],[],[]))

    active_net = nets[0]

    while True:
        cmd = input('> ').split(' ')

        print(cmd)

        if cmd[0] in ['quit','exit','close']:
            break

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

def main():
    menu()

main()
