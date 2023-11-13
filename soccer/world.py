collision_pair = {}
objects = [[],[],[]]


def add_collision_pair(group, a, b):
    if group not in collision_pair:
        print(f'add group {group}')
        collision_pair[group] = [[], []]
    if a:
        collision_pair[group][0].append(a)
    if b:
        collision_pair[group][1].append(b)

def remove_collision_pair(o):
    for pairs in collision_pair.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


def add_object(o, depth = 0):
     objects[depth].append(o)

def add_objects(ol, depth = 0):
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_pair(o)
            return
    raise ValueError('None')

def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()

def collide(a,b):
    left_a,bottom_a,right_a,top_a = a.get_bb()
    left_b,bottom_b,right_b,top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def handle_collisions():
    for group, pairs in collision_pair.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)
