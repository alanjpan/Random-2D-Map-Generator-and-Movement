# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 19:05:02 2018

@author: Alan Jerry Pan, CPA, CSc
@affiliation: Shanghai Jiaotong University

Program framework for random 2D map generation and movement.

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Random 2D Map Generator and Movement [Computer software]. Github repository <https://github.com/alanjpan/Random-2D-Map-Generator-and-Movement>

Futher expansions may include additional plot objects and placement of plot objects.

Note this software's license is GNU GPLv3.
"""

import random
secure_random = random.SystemRandom()

x = 20
y = 50

plane = []
world = {}

location = [0, 0]

################################################
i = 0

props = ['buildbunker']

def buildbunker():
    global world
    global i

    obj = 'wall'
    placement = [i, (i + 1), (i + 2), (i + y + 2), (i + y*2), (i + y*2 + 1), (i + y*2 + 2)]

    try:
        for j in placement:
            world[plane[j]] = obj
    except Exception:
        print('bunker out of range')
    
    i = j - 2
    del j

"""
    0, 2    1, 2    2, 2
    0, 1            2, 1
    0, 0            2, 0
    
    2 52 102
    1    101
    0    100
    
mapi is index key for plane[] linked from populatemap()
mapi in populatemap() needs to be updated after placing prop in world
"""

################################################


def boundmap():
    global x
    global y
    
    print('Input X dimension (0 to n)')
    command = input()
    if command.isnumeric() == True:
        x = int(command)
    else:
        print('Unacceptable X input')

    print('Input Y dimension (0 to n)')
    command = input()
    if command.isnumeric() == True:
        y = int(command)
    else:
        print('Unacceptable Y input')
        
def createmap():
    global plane
    
    for i in range(x):
        for j in range(y):
            plane.append((i, j))

def populatemap():
    global world
    global i
    
    for j in plane:
        world[j] = ''
    
    print('Input random generator rate (0 to 100)')
    command = input()
    if command.isnumeric() == True and 0 <= int(command) <= 100:
        rate = int(command)
    else:
        print('Unacceptable generator input')
        populatemap()
    
    i = 0
    maxi = (x * y)
    while i <= maxi:
        obj = ''
        if random.randint(0, 100) <= rate:
            ex = secure_random.choice(props)
            exec(compile(ex + '()', '', 'exec'))
        else:
            try:
                world[plane[i]] = obj
                i += 1
            except Exception:
                break
        
########## WORLD ART #############

grass = [' ', ' ', ' ', '~', '.', '.']


##################################

def checkcollision(loc):
    exec(compile("if world[" + loc + "] == 'wall': print('COLLISION')", '', 'exec'))

def drawworld():
    line = ''
    loc = '(' + str(location[0]) + ', ' + str(location[1]) + ')'
    
    for j in range(len(plane)):
        lookup = plane[j]
        if str(lookup) == loc:
            line += '@'
        elif world[lookup] == '':
            line += secure_random.choice(grass)
        elif world[lookup] == 'wall':
            line += '#'
        
        if j % y == 0:
            print(line)
            line = ''
    checkcollision(loc)

def movement():
    route = True
    while route == True:
        print('Which way should @ move? (forward, back, right, left)')
        command = input().lower()
        if command.startswith('f'):
            forward()
        elif command.startswith('b'):
            back()
        elif command.startswith('r'):
            right()
        elif command.startswith('l'):
            left()
            
        if (location[0] < 0) or (location[1] < 0):
            print('went off the map')
            route = False
        if (location[0] > x) or (location[1] > y):
            print('went off the map')
            route = False
        drawworld()

def forward():
    global location
    location[1] += 1
def back():
    global location
    location[1] -= 1
def right():
    global location
    location[0] += 1
def left():
    global location
    location[0] -= 1