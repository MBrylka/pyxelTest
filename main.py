import random
from abc import ABC

import pyxel

TILE_GRASS = (0, 0)
TILE_WATER = (0, 1)

score = 0


class GameObject(ABC):
    x: int
    y: int
    w: int
    h: int


def check_collision(obj1: GameObject, obj2: GameObject):
    return (
        obj1.x < obj2.x + obj2.w
        and obj1.x + obj1.w > obj2.x
        and obj1.y < obj2.y + obj2.h
        and obj1.h + obj1.y > obj2.y
    )


class Map:
    def __init__(self, map_w: int, map_h: int):
        self.map_w = map_w
        self.map_h = map_h
        self.tile_map: list[list[int]] = []
        self.generate_map()

    def generate_map(self):
        for _ in range(self.map_w):
            row: list[int] = []
            for _ in range(self.map_h):
                row.append(random.randint(0, 2))
            self.tile_map.append(row)

    def draw(self):
        for i in range(self.map_w):
            for j in range(self.map_h):
                pyxel.blt(i * 8, j * 8, 0, self.tile_map[i][j] * 8, 0, 8, 8)


class Player(GameObject):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 8
        self.h = 8
        self.color_key = 0

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 1

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8, 8, self.w, self.h, self.color_key)


class Apple(GameObject):
    def __init__(self):
        self.x = random.randint(0, 19) * 8
        self.y = random.randint(0, 14) * 8
        self.w = 8
        self.h = 8

    def update(self, player: Player):
        global score
        if check_collision(self, player):
            self.x = random.randint(0, 19) * 8
            self.y = random.randint(0, 14) * 8
            pyxel.play(1, 1)
            score += 10

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 8, self.w, self.h, 0)


class App:
    def __init__(self):
        pyxel.init(160, 120, title="Pyxel test")
        pyxel.load(
            "assets/testAsset.pyxres",
            image=True,
            tilemap=True,
            sound=True,
            music=True,
        )
        pyxel.playm(1, loop=True)

        self.player = Player()
        self.apple = Apple()
        self.map = Map(20, 15)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
        self.apple.update(self.player)

    def draw(self):
        global score
        pyxel.cls(0)
        self.map.draw()
        self.apple.draw()
        self.player.draw()
        # Draw score
        s = f"SCORE {score:>4}"
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)


App()
