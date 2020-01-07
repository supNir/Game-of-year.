import pygame, os, random, time

pygame.init()
size = height, width = 900, 1000
screen = pygame.display.set_mode(size)
sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
walls = pygame.sprite.Group()
grass = pygame.sprite.Group()
main_person = pygame.sprite.Group()
person_height, person_width = 100, 50
wall_height, wall_width = 50, 50
enemy_height, enemy_width = 150, 100


def load_image(name, colorkey=None):
    file_name = os.path.join("data", name)
    image = pygame.image.load(file_name)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(file_name):
    file_name = "data/" + file_name
    with open(file_name, "r") as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


def generate_level(level):
    player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == ".":
                Grass(x, y)
            elif level[y][x] == "!":
                Grass(x, y)
                DoorLight(x, y)
            elif level[y][x] == "H":
                Grass(x, y)
                player = Person(x, y)
            elif level[y][x] == "#":
                Wall(x, y)
            elif level[y][x] == "*":
                Grass(x, y)
                Enemy(x, y)
    return player


class Enemy(pygame.sprite.Sprite):
    enemy = pygame.transform.scale(load_image("mar.png"), (enemy_width, enemy_height))

    def __init__(self, x, y):
        super().__init__(sprites)
        self.add(enemies)
        self.image = Enemy.enemy
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(enemy_width // 2 * x, enemy_height // 3 * y)
        self.hp = 500
        self.damage = 25
        self.fps = 20


class Person(pygame.sprite.Sprite):
    person = pygame.transform.scale(load_image("wizard\\PNG\\wizard\\1_IDLE_000.png"), (50, 50))

    def __init__(self, x, y):
        super().__init__(sprites)
        self.add(main_person)
        self.image = Person.person
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(person_width * x, person_height // 2 * y)
        self.hp = 100
        self.damage = 25
        self.armor = 50

    def update(self, y, x, *args):
        self.rect = self.rect.move(x, y)
        if not pygame.sprite.spritecollideany(self, walls) and \
                not pygame.sprite.spritecollideany(self, enemies):
            self.rect = self.rect.move(x, y)
        else:
            self.rect = self.rect.move(-x, -y)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(sprites)
        self.add(walls)
        self.image = pygame.transform.scale(load_image("wall.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(wall_width * x, wall_height * y)


class DoorLight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(sprites)
        self.add(walls)
        self.image = pygame.transform.scale(pygame.image.load("data/f.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(wall_width * x, wall_height * y)


class Fon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(sprites)
        self.image = load_image("background.jpg")
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(wall_width * x, wall_height * y)


class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(sprites)
        self.add(grass)
        self.image = pygame.transform.scale(load_image("grass.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(wall_width * x, wall_height * y)


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


def main():
    background_image = pygame.image.load("data/back.jpg")
    screen.blit(background_image, (0, 0))
    person = generate_level(load_level("level2.txt"))
    clock = pygame.time.Clock()
    fps = 80
    running = True
    sprites.draw(screen)
    enemies.draw(screen)
    main_person.draw(screen)
    camera = Camera()
    pygame.display.flip()
    while running:
        y, x = 0, 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background_image, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y = -3
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y = 3
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x = -3
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x = 3
        enemies.update()
        main_person.update(y, x)
        camera.update(person)
        for sprite in sprites:
            camera.apply(sprite)
        sprites.draw(screen)
        enemies.draw(screen)
        main_person.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


main()
