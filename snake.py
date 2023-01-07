class snake(object):
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body = [self.head]
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        # Update the snake's position based on its direction
        self.head.pos = (self.head.pos[0] + self.dirnx, self.head.pos[1] + self.dirny)
        self.body.insert(0, self.head)
        self.body.pop()

    def reset(self, pos):
        # Reset the snake to its starting position
        self.head = cube(pos)
        self.body = [self.head]
        self.dirnx = 0
        self.dirny = 1

    def add_cube(self):
        # Add a new cube to the snake's body
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        # Draw the snake to the screen
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)
