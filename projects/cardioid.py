import pygame as pg
# from pygame_recorder import ScreenRecorder
import math

class Cardioid:
    def __init__(self, app):
        self.app = app
        self.radius = 275
        self.num_lines = 200
        self.translate = self.app.screen.get_width() // 2, self.app.screen.get_height() // 2
        self.counter, self.inc = 0, 0.01
    
    def get_color(self):
        self.counter += self.inc
        self.counter, self.inc = (self.counter, self.inc) if 0 < self.counter < 1 else (
            max(min(self.counter, 1), 0), -self.inc)
        
        return pg.Color('red').lerp('green', self.counter)

    def draw(self):
        time = pg.time.get_ticks()
        # function abs(math.sin(x) - 0.5) ressemble battement de coeur
        self.radius = 240 + 35 * abs(math.sin(time * 0.004) - 0.5)

        # to set the type of cardioid
        factor = 1 + 0.0003 * time

        for i in range(self.num_lines):
            theta = (2 * math.pi / self.num_lines) * i
            x1 = int(self.radius * math.cos(theta)) + self.translate[0]
            y1 = int(self.radius * math.sin(theta)) + self.translate[1]

            x2 = int(self.radius * math.cos(factor * theta)) + self.translate[0]
            y2 = int(self.radius * math.sin(factor * theta)) + self.translate[1]

            pg.draw.aaline(self.app.screen, self.get_color(), (x1, y1), (x2, y2))

class App:
    def __init__(self):
        self.screen = pg.display.set_mode([1100, 618])
        self.clock = pg.time.Clock()
        self.cardioid = Cardioid(self)
        # self.recorder = ScreenRecorder(1100, 618, 30)
    
    def draw(self):
        self.screen.fill("black")
        self.cardioid.draw()
        pg.display.flip()
    
    def run(self):
        run = True
        while run:
            self.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    # self.recorder.end_recording()
                    exit()
            # self.recorder.capture_frame(self.screen)
            self.clock.tick(30)

if __name__ == "__main__":
    app = App()
    app.run()