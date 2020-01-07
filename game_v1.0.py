import pygame, os, random, time

pygame.init()
size = height, width = 1000, 1000
screen = pygame.display.set_mode(size)
sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
walls = pygame.sprite.Group()
boxes = pygame.sprite.Group()
portal = pygame.sprite.Group()
floor = pygame.sprite.Group()
main_person = pygame.sprite.Group()
person_height, person_width = 100, 50
wall_height, wall_width = 50, 50
enemy_height, enemy_width = 150, 100
number_of_hero = 1
level = []


def load_level(file_name):
    file_name = "levels/" + file_name
    with open(file_name, "r") as mapFile:
        level_map = [line.strip() for line in mapFile]
    str_number = ""
    for i in file_name:
        if i.isdigit():
            str_number = str_number + i
    number = int(str_number)
    return level_map


def generate_level(level, number):
    player = None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == ".":
                Floor(x, y, number)
            elif level[y][x] == "!":
                Floor(x, y, number)
                DoorLight(x, y)
            elif level[y][x] == "H":
                Floor(x, y, number)
                if number_of_hero == 1:
                    player = KnightWithSpear(x, y)
                elif number_of_hero == 2:
                    player = Mage(x, y)
            elif level[y][x] == "#":
                Wall(x, y, number)
            elif level[y][x] == "-":
                Box(x, y, number)
            elif level[y][x] == "?":
                Portal(x, y)
            elif level[y][x] == "O":
                ork = 1
                if ork == 1:
                    Floor(x, y, number)
                    FirstOrk(x, y)
    return player


class Floor(pygame.sprite.Sprite):
    file_name = "images/blocks/"
    floor = [pygame.image.load(file_name + "grass.png")]

    def __init__(self, x, y, number):
        super().__init__(sprites)
        self.add(floor)
        self.image = self.floor[number]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(wall_width * x, wall_height * y)


class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(sprites)
        self.add(portal)
        self.image = pygame.transform.scale(pygame.image.load("images/portal/portal.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(wall_width * x, wall_height * y)


class DoorLight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(sprites)
        self.add(walls)
        self.image = pygame.transform.scale(pygame.image.load("images/blocks/f.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(wall_width * x, wall_height * y)


class Wall(pygame.sprite.Sprite):
    walls = [pygame.image.load("images/blocks/wall.png")]

    def __init__(self, x, y, number):
        super().__init__(sprites)
        self.add(walls)
        self.image = self.walls[number]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(wall_width * x, wall_height * y)


class Box(pygame.sprite.Sprite):
    boxes = [pygame.image.load("images/blocks/box.png")]

    def __init__(self, x, y, number):
        super().__init__(sprites)
        self.add(boxes)
        self.image = self.boxes[number]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(wall_width * x, wall_height * y)


class FirstOrk(pygame.sprite.Sprite):
    file_name = "images/characters/enemies/ORK1/"
    attack_right_images = [pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_000.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_001.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_002.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_003.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_004.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_005.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_006.png")]
    attack_left_images = [pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_000.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_001.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_002.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_003.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_004.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_005.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_006.png")]
    die_images = [pygame.image.load(file_name + "_DIE/_DIE_000.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_001.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_002.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_003.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_004.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_005.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_006.png")]
    run_right_images = [pygame.image.load(file_name + "_RUN_RIGHT/_RUN_000.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_001.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_002.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_003.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_004.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_005.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_006.png")]
    run_left_images = [pygame.image.load(file_name + "_RUN_LEFT/_RUN_000.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_001.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_002.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_003.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_004.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_005.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_006.png")]

    def __init__(self, x, y):
        super().__init__(sprites)
        self.add(enemies)
        self.image = self.attack_right_images[0]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(50 * x, 50 * y)
        self.hp = 100
        self.damage = 1
        self.armor = 100
        self.speed = 2
        self.alive = True
        self.left = False
        self.right = False
        self.pred_left = True
        self.pred_right = True
        self.figth = False
        self.stop = True
        self.idle_animation = 0
        self.run_animation = 0
        self.attack_animation = 0
        self.die_animation = 0
        self.pos_attack = self.rect
        self.width = len(level[0])
        self.height = len(level)

    def search_hero(self, x, y):
        if self.color[x][y] == 0 and self.color[self.hero_x][self.hero_y] == 0:
            self.color[x][y] = 1
            print(x, y, )
            if y + 1 < self.width:
                if level[x][y + 1] != "#":
                    self.pred[x][y + 1] = (x, y)
                    self.search_hero(x, y + 1)
            if x + 1 < self.height:
                if level[x + 1][y] != "#":
                    self.pred[x + 1][y] = (x, y)
                    self.search_hero(x + 1, y)
            if y - 1 > -1:
                if level[x][y - 1] != "#":
                    self.pred[x][y - 1] = (x, y)
                    self.search_hero(x, y - 1)
            if x - 1 > -1:
                if level[x - 1][y] != "#":
                    self.pred[x - 1][y] = (x, y)
                    self.search_hero(x - 1, y)

    def update(self, hero_x, hero_y, *args):
        if self.hp <= 0 and self.die_animation <= 6:
            self.image = self.die_images[self.die_animation]
            self.die_animation += 1
        else:
            self.color = [[0 for i in range(self.width + 1)] for j in range(self.height + 1)]
            self.pred = [[(-1, -1) for i in range(self.width + 1)] for j in range(self.height + 1)]
            self.hero_x, self.hero_y = hero_x // 50, hero_y // 50
            self.search_hero(self.rect[1] // 50, self.rect[0] // 50)
            if self.color[self.hero_x][self.hero_y] == 1:
                pass


class KnightWithSpear(pygame.sprite.Sprite):
    file_name = "images/characters/heroes/Knight_with_spear/"
    attack_right_images = [pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_000.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_001.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_002.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_003.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_004.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_005.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_006.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_007.png")]
    attack_left_images = [pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_000.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_001.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_002.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_003.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_004.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_005.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_006.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_007.png")]
    die_images = [pygame.image.load(file_name + "_DIE/_DIE_000.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_001.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_002.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_003.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_004.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_005.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_006.png")]
    idle_right_images = [pygame.image.load(file_name + "_IDLE_RIGHT/_IDLE_000.png"),
                         pygame.image.load(file_name + "_IDLE_RIGHT/_IDLE_001.png"),
                         pygame.image.load(file_name + "_IDLE_RIGHT/_IDLE_002.png"),
                         pygame.image.load(file_name + "_IDLE_RIGHT/_IDLE_003.png"),
                         pygame.image.load(file_name + "_IDLE_RIGHT/_IDLE_004.png"),
                         pygame.image.load(file_name + "_IDLE_RIGHT/_IDLE_005.png"),
                         pygame.image.load(file_name + "_IDLE_RIGHT/_IDLE_006.png")]
    idle_left_images = [pygame.image.load(file_name + "_IDLE_LEFT/_IDLE_000.png"),
                        pygame.image.load(file_name + "_IDLE_LEFT/_IDLE_001.png"),
                        pygame.image.load(file_name + "_IDLE_LEFT/_IDLE_002.png"),
                        pygame.image.load(file_name + "_IDLE_LEFT/_IDLE_003.png"),
                        pygame.image.load(file_name + "_IDLE_LEFT/_IDLE_004.png"),
                        pygame.image.load(file_name + "_IDLE_LEFT/_IDLE_005.png"),
                        pygame.image.load(file_name + "_IDLE_LEFT/_IDLE_006.png")]
    run_right_images = [pygame.image.load(file_name + "_RUN_RIGHT/_RUN_000.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_001.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_002.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_003.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_004.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_005.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_006.png")]
    run_left_images = [pygame.image.load(file_name + "_RUN_LEFT/_RUN_000.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_001.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_002.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_003.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_004.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_005.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_006.png")]

    def __init__(self, x, y):
        super().__init__(sprites)
        self.add(main_person)
        self.image = self.idle_right_images[0]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(person_width * x, person_height // 2 * y)
        self.hp = 100
        self.damage = 25
        self.armor = 150
        self.speed = 3
        self.alive = True
        self.left = False
        self.right = False
        self.pred_left = True
        self.pred_right = True
        self.figth = False
        self.stop = True
        self.idle_animation = 0
        self.run_animation = 0
        self.attack_animation = 0
        self.die_animation = 0
        self.pos_attack = self.rect

    def update(self, y, x, *args):
        if self.hp <= 0:
            self.image = self.die_images[self.die_animation]
            self.die_animation += 1
        else:
            self.rect = self.rect.move(x, y)
            if not pygame.sprite.spritecollideany(self, walls) and \
                    not pygame.sprite.spritecollideany(self, enemies):
                self.rect = self.rect.move(x, y)
                if self.left:
                    self.pred_right = False
                    self.pred_left = True
                    self.image = self.run_left_images[self.run_animation]
                    self.run_animation = (self.run_animation + 1) % 7
                elif self.right:
                    self.pred_right = True
                    self.pred_left = False
                    self.image = self.run_right_images[self.run_animation]
                    self.run_animation = (self.run_animation + 1) % 7
                if self.figth:
                    if self.pos_attack[0] < self.rect.x:
                        self.pred_right = False
                        self.pred_left = True
                        self.image = self.attack_left_images[self.attack_animation]
                    else:
                        self.pred_right = True
                        self.pred_left = False
                        self.image = self.attack_right_images[self.attack_animation]
                    self.attack_animation = (self.attack_animation + 1) % 8
            else:
                self.idle_animation = 0
                for sprite in enemies:
                    opa = pygame.sprite.Group()
                    sprite.add(opa)
                    if pygame.sprite.spritecollideany(self, opa):
                        if self.armor > 0:
                            self.armor -= sprite.damage
                        else:
                            self.hp -= sprite.damage + self.armor
                            self.armor = 0
                        if sprite.armor > 0:
                            sprite.armor -= sprite.damage
                        else:
                            sprite.hp -= sprite.damage + sprite.armor
                            sprite.armor = 0
                self.rect = self.rect.move(-x, -y)
            if self.stop:
                if self.pred_left:
                    self.image = self.idle_left_images[self.idle_animation]
                else:
                    self.image = self.idle_right_images[self.idle_animation]
                self.idle_animation = (self.idle_animation + 1) % 7


class Mage(pygame.sprite.Sprite):
    file_name = "images/characters/heroes/Mage/"
    attack_right_images = [pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_000.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_001.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_002.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_003.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_004.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_005.png"),
                           pygame.image.load(file_name + "_ATTACK_RIGHT/ATTACK_006.png")]
    attack_left_images = [pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_000.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_001.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_002.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_003.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_004.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_005.png"),
                          pygame.image.load(file_name + "_ATTACK_LEFT/ATTACK_006.png")]
    die_images = [pygame.image.load(file_name + "_DIE/_DIE_000.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_001.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_002.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_003.png"),
                  pygame.image.load(file_name + "_DIE/_DIE_004.png")]
    idle_right_images = [pygame.image.load(file_name + "_IDLE_RIGHT/_IDLE_000.png"),
                         pygame.image.load(file_name + "_IDLE_RIGHT/_IDLE_001.png"),
                         pygame.image.load(file_name + "_IDLE_RIGHT/_IDLE_002.png"),
                         pygame.image.load(file_name + "_IDLE_RIGHT/_IDLE_003.png"),
                         pygame.image.load(file_name + "_IDLE_RIGHT/_IDLE_004.png"),
                         pygame.image.load(file_name + "_IDLE_RIGHT/_IDLE_005.png"),
                         pygame.image.load(file_name + "_IDLE_RIGHT/_IDLE_006.png")]
    idle_left_images = [pygame.image.load(file_name + "_IDLE_LEFT/_IDLE_000.png"),
                        pygame.image.load(file_name + "_IDLE_LEFT/_IDLE_001.png"),
                        pygame.image.load(file_name + "_IDLE_LEFT/_IDLE_002.png"),
                        pygame.image.load(file_name + "_IDLE_LEFT/_IDLE_003.png"),
                        pygame.image.load(file_name + "_IDLE_LEFT/_IDLE_004.png"),
                        pygame.image.load(file_name + "_IDLE_LEFT/_IDLE_005.png"),
                        pygame.image.load(file_name + "_IDLE_LEFT/_IDLE_006.png")]
    run_right_images = [pygame.image.load(file_name + "_RUN_RIGHT/_RUN_000.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_001.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_002.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_003.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_004.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_005.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_006.png"),
                        pygame.image.load(file_name + "_RUN_RIGHT/_RUN_007.png")]
    run_left_images = [pygame.image.load(file_name + "_RUN_LEFT/_RUN_000.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_001.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_002.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_003.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_004.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_005.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_006.png"),
                       pygame.image.load(file_name + "_RUN_LEFT/_RUN_007.png")]

    def __init__(self, x, y):
        super().__init__(sprites)
        self.add(main_person)
        self.image = self.idle_right_images[0]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(person_width * x, person_height // 2 * y)
        self.hp = 100
        self.damage = 25
        self.armor = 150
        self.speed = 3
        self.alive = True
        self.left = False
        self.right = False
        self.pred_left = True
        self.pred_right = True
        self.figth = False
        self.stop = True
        self.idle_animation = 0
        self.run_animation = 0
        self.attack_animation = 0
        self.die_animation = 0
        self.pos_attack = self.rect

    def update(self, y, x, *args):
        if self.hp <= 0:
            self.image = self.die_images[self.die_animation]
            self.die_animation += 1
        else:
            self.rect = self.rect.move(x, y)
            if not pygame.sprite.spritecollideany(self, walls) and \
                    not pygame.sprite.spritecollideany(self, enemies):
                self.rect = self.rect.move(x, y)
                if self.left:
                    self.pred_right = False
                    self.pred_left = True
                    self.image = self.run_left_images[self.run_animation]
                    self.run_animation = (self.run_animation + 1) % 8
                elif self.right:
                    self.pred_right = True
                    self.pred_left = False
                    self.image = self.run_right_images[self.run_animation]
                    self.run_animation = (self.run_animation + 1) % 8
                if self.figth:
                    if self.pos_attack[0] < self.rect.x:
                        self.pred_right = False
                        self.pred_left = True
                        self.image = self.attack_left_images[self.attack_animation]
                    else:
                        self.pred_right = True
                        self.pred_left = False
                        self.image = self.attack_right_images[self.attack_animation]
                    self.attack_animation = (self.attack_animation + 1) % 7
            else:
                self.rect = self.rect.move(-x, -y)
            if self.stop:
                if self.pred_left:
                    self.image = self.idle_left_images[self.idle_animation]
                else:
                    self.image = self.idle_right_images[self.idle_animation]
                self.idle_animation = (self.idle_animation + 1) % 5
            else:
                self.idle_animation = 0
                for sprite in enemies:
                    if pygame.sprite.spritecollideany(self, sprite):
                        if self.armor > 0:
                            self.armor -= sprite.damage
                        else:
                            self.hp -= sprite.damage + self.armor
                            self.armor = 0


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
    global level
    background_image = pygame.image.load("images/background/background32.png")
    screen.blit(background_image, (0, 0))
    level = load_level("level0.txt")
    player = generate_level(level, 0)
    clock = pygame.time.Clock()
    fps = 1000
    running = True
    sprites.draw(screen)
    enemies.draw(screen)
    main_person.draw(screen)
    camera = Camera()
    pygame.display.flip()
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background_image, (0, 0))
        if player.die_animation < 7:
            y, x = 0, 0
            keys = pygame.key.get_pressed()
            player.stop = True
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                y = -player.speed
                player.stop = False
                player.left = player.pred_left
                player.right = player.pred_right
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                y = player.speed
                player.stop = False
                player.left = player.pred_left
                player.right = player.pred_right
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                x = -player.speed
                player.stop = False
                player.left = True
                player.right = False
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                x = player.speed
                player.stop = False
                player.left = False
                player.right = True
            else:
                if y == 0:
                    player.left = False
                    player.right = False
                    player.animcount = 0
            if player.attack_animation > 0:
                player.left = False
                player.stop = False
                player.right = False
                player.figth = True
                x = 0
                y = 0
            else:
                player.figth = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and player.die_animation < 7:
                if event.button == 1:
                    player.left = False
                    player.stop = False
                    player.right = False
                    player.figth = True
                    player.pos_attack = event.pos
        if player.die_animation < 7:
            main_person.update(y, x)
            enemies.update(player.rect[1], player.rect[0])
            camera.update(player)
            for sprite in sprites:
                camera.apply(sprite)
        sprites.draw(screen)
        enemies.draw(screen)
        main_person.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


main()
