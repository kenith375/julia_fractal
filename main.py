import pygame, moderngl
from array import array
pygame.init()
WIDTH = 1920
HEIGHT = 1080
pygame.display.set_mode(
    (WIDTH, HEIGHT),
    pygame.OPENGL | pygame.DOUBLEBUF
)

ctx = moderngl.create_context()
with open("basic.vert") as f:
    vertex_shader = f.read()

with open("basic.frag") as f:
    fragment_shader = f.read()

prog = ctx.program(
    vertex_shader=vertex_shader,
    fragment_shader=fragment_shader,
)
vertices = array('f', [
    -1.0, -1.0,
     1.0, -1.0,
    -1.0,  1.0,
     1.0,  1.0,
])

vbo = ctx.buffer(vertices)

vao = ctx.vertex_array(
    prog,
    [
        (vbo, "2f", "vert"),
    ],
)


prog["resolution"] = (WIDTH, HEIGHT)




running = True
x=0.6
y=0
a=0
glow=(-0.5,0.5)
while running:
    prog["r_offset"] = (x, y)
    #prog["circle"] = glow
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x-=y/5000
    y+=x/5000
    #ctx.clear()
    vao.render(moderngl.TRIANGLE_STRIP)
    #data = ctx.screen.read(components=3)
    #surface = pygame.image.fromstring(data, (WIDTH, HEIGHT), "RGB", True)
    #pygame.image.save(surface, f"frames/{frame:04d}.png")
    pygame.display.flip()

pygame.quit()