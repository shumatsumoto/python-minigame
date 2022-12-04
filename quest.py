import pgzrun

GRID_WIDTH=16
GRID_HEIGHT=12
GRID_SIZE=50

WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
MAP=["WWWWWWWWWWWWWWWW",
     "W           K  W",
     "W  K           W",
     "W  W  KG       W",
     "W  WWWWWWWWWW  W",
     "W         K    W",
     "WK     P       W",
     "W  WWWWWWWWWW  W",
     "W      GK   W  W",
     "W              W",
     "W  K       K   D",
     "WWWWWWWWWWWWWWWW"]

def screen_coords(x, y):
  return(x * GRID_SIZE, y * GRID_SIZE)

def setup_game():
  global player
  player = Actor("player", anchor = ("left", "top"))
  for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
      square = MAP[y][x]
      if square == "P":
        player.pos = screen_coords(x, y)

def draw_background():
  for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
      screen.blit("floor1", screen_coords(x, y))

def draw_scenery():
  for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
      square = MAP[y][x]
      if square == "W":
        screen.blit("wall", screen_coords(x, y))
      elif square == "D":
        screen.blit("door", screen_coords(x, y))

def draw_actors():
  player.draw()

def draw():
  draw_background()
  draw_scenery()
  draw_actors()

setup_game()
pgzrun.go()
