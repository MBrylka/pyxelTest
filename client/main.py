from abc import ABC

import pyxel

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
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pass


App()
