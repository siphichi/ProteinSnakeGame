import pygame, random, sys
from pygame.math import Vector2
from seqanalysis import Protein

# Hydrophobic = green
# Polar = Yellow
# Acidic = Blue
# Basic = Red



class PROTEIN:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0,0)
        self.new_block = False
        
        self.curr_domains = ['#0ed145']
        self.sequence = ['N-teminus', 'M', 'C-terminus']
        
        self.head_up = pygame.image.load('graphics2/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('graphics2/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('graphics2/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('graphics2/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('graphics2/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('graphics2/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('graphics2/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('graphics2/tail_left.png').convert_alpha()
        
        self.crunch_sound = pygame.mixer.Sound('Sound/Sound_crunch.wav')
        
    def insert_domain(self, index):
        # ACIDIC(), BASIC(), HYDROPHOBIC(), POLAR()
        if index == 0: # green = hydrophobic
            self.curr_domains.insert(-1, '#0ed145')
            self.sequence[1] = self.sequence[1] + 'W'
        elif index == 1: # red K
            self.curr_domains.insert(-1, '#ec1c24')
            self.sequence[1] = self.sequence[1] + 'K'
        elif index == 2: # blue D
            self.curr_domains.insert(-1, '#00a8f3')
            self.sequence[1] = self.sequence[1] + 'D'
        else: # yellow S
            self.curr_domains.insert(-1, '#fff200')
            self.sequence[1] = self.sequence[1] + 'S'
            
        print(self.sequence)
        
    def draw_protein(self):
        self.update_head_graphics()
        self.update_tail_graphics()
#         for block in self.body:
#             block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
#             pygame.draw.rect(screen, colour, block_rect)


        for index, block in enumerate(self.body):
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) -1:
                screen.blit(self.tail, block_rect)
            else:
                pygame.draw.rect(screen, self.curr_domains[index-2], block_rect)
                
            # else:
                # This is where different graphics were
                
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down
            
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down
    
    def move_protein(self):
        if self.new_block:
            body_copy = self.body[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        self.new_block = True
        
    def play_crunch_sound(self):
        self.crunch_sound.play()
        
    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0,0)
        self.curr_domains = ['#0ed145']
        self.sequence = ['N-teminus', 'M', 'C-terminus']
        game_active = False
    
class BASIC:
    def __init__(self):
        self.randomise()
        
    def draw_domain(self):
        domain_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, domain_rect)

    def randomise(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        
class ACIDIC:
    def __init__(self):
        self.randomise()
        
    def draw_domain(self):
        domain_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(blue, domain_rect)
        
    def randomise(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        
class HYDROPHOBIC:
    def __init__(self):
        self.randomise()
        
    def draw_domain(self):
        domain_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(green, domain_rect)
        
    def randomise(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        
class POLAR:
    def __init__(self):
        self.randomise()
        
    def draw_domain(self):
        domain_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(lemon, domain_rect)
        
    def randomise(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        
class MAIN:
    def __init__(self):
        self.protein = PROTEIN()
        self.domain = [ACIDIC(), BASIC(), HYDROPHOBIC(), POLAR()]
        self.seq = Protein(self.protein.sequence[1])
    
    def update(self):
        self.protein.move_protein()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_message, score_message_rect)
        for i in range(4):
            self.domain[i].draw_domain()    
        self.protein.draw_protein()
        self.draw_score()

        
    def check_collision(self):
        for i in range(4):
            if self.domain[i].pos == self.protein.body[0]:
                self.domain[i].randomise()
                self.protein.add_block()
                self.protein.play_crunch_sound()
                self.protein.insert_domain(i)
        
        for i in range(4):
            for block in self.protein.body[1:]:
                if block == self.domain[i].pos:
                    self.domain[i].randomise()
    
    def check_fail(self):
        if not 0 <= self.protein.body[0].x < cell_number or not 0 <= self.protein.body[0].y < cell_number:
            self.game_over()
    
        for block in self.protein.body[1:]:
            if block == self.protein.body[0]:
                self.game_over()
    
    def game_over(self):
#         self.test_protein()
        self.protein.reset()
        game_over = False
        
    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(0, cell_number, 2):
            for col in range(0, cell_number, 2):
                grass_rect = pygame.Rect(col*cell_size, row*cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, grass_color, grass_rect)
        for row in range(1, cell_number, 2):
            for col in range(1, cell_number, 2):
                grass_rect = pygame.Rect(col*cell_size, row*cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, grass_color, grass_rect)
                
    def seq_analysis(self):
        self.seq = Protein(self.protein.sequence[1])
        
    def draw_score(self):
        # This should be changed based on protein trying to recreate
        score_text = str(len(self.protein.body) - 3)
        score_surf = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surf.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, (apple_rect.width + score_rect.width +6), apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surf, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 6)
        
#         if 'Transmembrane' in protein_type:
#             print('hi')
        
        
    def generate_challenge(self):
        types_list = ['Soluble', 'Soluble ER', 'Type 1 Transmembrane', 'Type 2 Transmembrane']
        self.protein_type = types_list[random.randint(0, 3)]
        self.target_length = random.randint(15, 20)
        self.protein_type = 'Soluble'
        self.target_length = 3
        return 'Make a ' + self.protein_type + ' protein with ' + str(self.target_length) + ' residues'
    
    def correct_type(self):
        if self.seq.has_signal_seq():
            if self.seq.has_tm_seq():
                return 'Type 1 Transmembrane'
            return 'ER Soluble'
        if self.seq.has_tm_seq():
            return 'Type 2 Transmembrane'
        return 'Soluble'
    
    def test_protein(self):
        if len(self.protein.sequence[1]) -1 == self.target_length:
            if self.correct_type() == self.protein_type:
                print("Correct length and correct protein")
            else:
                print("Correct length but incorrect protein")
        else:
            if self.correct_type() == self.protein_type:
                print('Incorrect length but correct protein')
            else:
                print('Incorrect length and incorrect protein')
    
    def correct_protein(self):
        if len(self.protein.sequence[1]) -1 == self.target_length:
            if self.correct_type() == self.protein_type:
                return True
        return False

        
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
pygame.display.set_caption('Protein Maker')
clock = pygame.time.Clock()
apple = pygame.image.load('graphics2/apple.png').convert_alpha()
lemon = pygame.image.load('graphics2/lemon.png').convert_alpha()
blue = pygame.image.load('graphics2/green.png').convert_alpha()
green = pygame.image.load('graphics2/blue.png').convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

#bg_music = pygame.mixer.Sound('happy-14585.mp3')
#bg_music.set_volume(0.5)
#bg_music.play()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

score_message = game_font.render(main_game.generate_challenge(), False, '#04631f')
score_message_rect = score_message.get_rect(center = (10*cell_size, 2*cell_size))
bg_rect = pygame.Rect(score_message_rect.left -6, score_message_rect.top, (score_message_rect.width + 6), score_message_rect.height)
score = 0
global game_active
game_active = False

while True:
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == SCREEN_UPDATE:
            main_game.update()
        
        if game_active:
            screen.fill((175, 215, 70))
            main_game.draw_elements()
            pygame.display.update()
            clock.tick(60)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and main_game.protein.direction.y != 1:
                    main_game.protein.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN and main_game.protein.direction.y != -1:
                    main_game.protein.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT and main_game.protein.direction.x != 1:
                    main_game.protein.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT and main_game.protein.direction.x != -1:
                    main_game.protein.direction = Vector2(1, 0)
                if event.key == pygame.K_SPACE and not main_game.correct_protein():
                    main_game.test_protein()
            if main_game.correct_protein():
                main_game.game_over()
            
            #main_game.test_protein()

        else:
            screen.fill((94, 129, 162))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
            
            
            
                # blit all the off screen stuff
#             score_message = game_font.render(main_game.generate_challenge(), False, 'Green')
#             score_message_rect = score_message.get_rect(center = (5*cell_size, 5*cell_size))
#             screen.blit(score_message, score_message_rect)

            
            
#             if event.key == pygame.K_SPACE:
#                 self.generate_challenge()
#             if event.key == pygame.K_ENTER:
#                 self.test_protein(type_of_protein)
            
#                 screen.blit(player_stand, player_stand_rect)
#                 obstacle_rect_list.clear()
#                 player_rect.midbottom = (80, 318)
#                 player_gravity = 0
#                 
#                 score_message = test_font.render("Your score: " + str(score), False, 'Green')
#                 score_message_rect = score_message.get_rect(center = (400, 320))
#                 
#                 screen.blit(game_name, game_name_rect)
            
            
            
#             if event.key == pygame.K_SPACE:
#                 self.generate_challenge()
#             if event.key == pygame.K_ENTER:
#                 self.test_protein(type_of_protein)

# add if game is active, then it gives you challenge, then space to start, then when you're done press enter
                
    pygame.display.update()
    clock.tick(60)
# Using somewhere else      
#     screen.fill((175, 215, 70))
#     main_game.draw_elements()
#     pygame.display.update()
#     clock.tick(60)
    