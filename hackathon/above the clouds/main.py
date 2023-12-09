import pygame
import random
from lowPlatform import *
from settings import *
from platforms import *
from enemies import *
from Clouds import *
from store import *
vec=pygame.math.Vector2
from os import path
import os 
import time

class Game:
    def __init__(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((display_width, display_height))
        self.gameDisplay.fill(white)
        self.store = Store()
        pygame.display.set_caption("Above the clouds")
        self.clock = pygame.time.Clock()
        self.img_hero=pygame.sprite.Sprite()
        self.img_hero.image = self.store.characters[self.store.active_character].image.convert_alpha()
        self.img_hero.image = pygame.transform.scale(self.img_hero.image, (55, 55))
        self.img_hero.rect=self.img_hero.image.get_rect()
        self.background = pygame.image.load('blue_back.jpg').convert()
        self.font = pygame.font.SysFont(None, 25)
        self.gameExit = False
        self.pos=vec(display_width-100,display_height)
        self.img_hero.rect.topleft=[self.pos.x,self.pos.y]
        self.vel=vec(0,0)
        self.acc=vec(0,0)
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.platforms = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.playerSprite=pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.playerSprite.add(self.img_hero)
        p1 = lowPlatform(0, display_height - 40, display_width, 40)
        #p2 = Platform(display_width/2 - 50,display_height-150)
        #p3 = Platform(display_width/2 - 100,display_height-300)
        #p4 = Platform(display_width / 2, display_height - 450)
        #p5 = Platform(0, display_height - 600)
        platform_obj=Platform(self)
        self.platform_images=platform_obj.getImages()
        p2=Platform(self)
        p2.getPlatform(display_width/2 - 50,display_height-150,self.platform_images)
        p3 = Platform(self)
        p3.getPlatform(display_width/2 - 100,display_height-300, self.platform_images)
        p4 = Platform(self)
        p4.getPlatform(display_width / 2, display_height - 450, self.platform_images)
        p5 = Platform(self)
        p5.getPlatform(0, display_height - 600, self.platform_images)
        self.platforms.add(p1)
        self.platforms.add(p2)
        self.platforms.add(p3)
        self.platforms.add(p4)
        self.platforms.add(p5)
        self.score=0
        self.coin_score=0
        self.font_name=pygame.font.match_font(Font_Name)
        self.load_data()
        self.enemies_timer=0

        for i in range(8):
            c=Cloud(self)
            c.rect.y+= 600

    def load_data(self):
        # loading the high score from the file
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, hs_file), 'r+') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

        # load cloud images
        cloud_dir = path.join(self.dir, 'clouds_img')
        self.cloud_images=[]
        for i in range(1,4):
            self.cloud_images.append(pygame.image.load(path.join(cloud_dir,'cloud{}.png'.format(i))).convert())
        
        self.coin_image_score = pygame.image.load('./coin.png')
        # load sounds
        self.sound_dir=path.join(self.dir,'sound')
        self.jump_sound=pygame.mixer.Sound(path.join(self.sound_dir,'jump.ogg'))
        self.jump_sound.set_volume(0.1)
        self.pow_sound = pygame.mixer.Sound(path.join(self.sound_dir, 'pow.wav'))
        self.coin_sound = pygame.mixer.Sound(path.join(self.sound_dir, 'coin_sound.mp3'))
        pygame.mixer.music.load(path.join(self.sound_dir, 'main_menu_song.mp3'))
        pygame.mixer.music.set_volume(0.5)

    def updateScreen(self):

        now_time=pygame.time.get_ticks()
        if now_time-self.enemies_timer>5000 + random.choice([-1000,-500,0,500,1000]):
            self.enemies_timer=now_time
            Enemies(self)

        enemies_hits=pygame.sprite.spritecollide(self.img_hero,self.enemies,False, pygame.sprite.collide_mask)
        if enemies_hits:
            self.gameOver=True

        #Updating the sprite's position
        self.img_hero.rect.midbottom = [self.pos.x, self.pos.y]
        #Checking for collision between the player and the sprites.
        powerup_hits = pygame.sprite.spritecollide(self.img_hero, self.powerups, False)
        for x in powerup_hits:
            self.pow_sound.play()
            self.vel.y = power_up_boost
        if self.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.img_hero, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit

                if self.pos.x < lowest.rect.right + 30 and self.pos.x > lowest.rect.left - 30:
                    if self.pos.y < lowest.rect.centery:
                        self.pos.y = lowest.rect.top
                        self.vel.y = 0
        coin_hits = pygame.sprite.spritecollide(self.img_hero, self.coins, True)
        for coin in coin_hits:
            self.coin_sound.play()
            self.collectCoin(coin)
    
        #Scrolling the screen upwards as the player moves upward. Killing the platforms which are not futher required.
        if self.img_hero.rect.top <= display_height/4:

            if random.randrange(100) < 99:
                Cloud(self)

            self.pos.y+=abs(self.vel.y)

            for cloud in self.clouds:
                cloud.rect.y+=max(abs(self.vel.y / 2), 2)

            for platform in self.platforms:
                platform.rect.y+=abs(self.vel.y)
                if platform.rect.top>=display_height:
                    platform.kill()
                    self.score+=10

            for enemy in self.enemies:
                 enemy.rect.y += abs(self.vel.y)





         #GAME OVER CHECK.
        if self.img_hero.rect.bottom>display_height:
            self.gameOver=True;
            for sprite in self.platforms:
                sprite.rect.y-=max(self.vel.y,10)

        #Creating new platforms.
        while len(self.platforms)<6:#There should be atleast 6 platforms on the screen.
            width=random.randrange(50,100)
            p = Platform(self)
            p.getPlatform(random.randrange(0,display_width-width), random.randrange(-50,-30), self.platform_images)
            self.platforms.add(p)

        for x in self.powerups: #updating powerup sprites positions according to the change in platform position.
            x.update()
        
        for x in self.coins:  # updating coin sprites positions according to the change in platform position
            x.update()


        self.gameDisplay.fill(black)
        self.enemies.update()
        self.powerups.update()
        self.platforms.update()
        self.clouds.update()
        self.playerSprite.update( )
        self.gameDisplay.blit(self.background,(0,0))
        self.clouds.draw(self.gameDisplay)
        self.platforms.draw(self.gameDisplay)
        self.powerups.draw(self.gameDisplay)
        self.enemies.draw(self.gameDisplay)
        self.coins.draw(self.gameDisplay)

        self.playerSprite.draw(self.gameDisplay)
        #Displaying the score.
        self.messageToScreen("SCORE : "+(str)(self.score), 25, white, display_width / 2 , 15)
        self.drawScore()
        pygame.display.update()

    def collectCoin(self, coin):
        # Add the logic to handle collecting a coin and updating the score
        self.coin_score += 5  # You can adjust the score increment as needed

    def drawScore(self):
        self.messageToScreen(str(self.coin_score), 25, yellow, display_width - 80, 25)
        self.coin_image_score = pygame.transform.scale(self.coin_image_score, (40, 40))
        image_rect = self.coin_image_score.get_rect()
        image_rect.topright = (display_width - 10, 10)
        self.gameDisplay.blit(self.coin_image_score, image_rect)

    def run(self):
        self.score=0
        self.gameOver = False
        while not self.gameExit:
            self.checkEvent()
            self.acc.x+=self.vel.x*player_Fric
            self.vel+=self.acc
            self.pos+=self.vel+0.5*self.acc
            self.checkHorizontalCrossing()
            self.updateScreen()
            self.clock.tick(fps)
            if self.gameOver==True:
                self.gameOverScreen()
        pygame.mixer.music.fadeout(500)

        pygame.quit()
        quit()

    def checkHorizontalCrossing(self):
        if self.pos.x > display_width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = display_width
        if self.pos.y == display_height:
            self.gameOver = True
        if self.pos.y == -50:
            self.pos.y = display_height

    def checkEvent(self):
        self.acc=vec(0,gravity)
        self.jump()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.acc.x = -player_Acc

                if event.key == pygame.K_RIGHT:
                    self.acc.x = player_Acc

                if event.key == pygame.K_SPACE:
                    self.jump()

    def messageToScreen(self,msg,size, color, x, y):
        font=pygame.font.Font(self.font_name,size)
        text_surface=font.render(msg,True,color)
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        self.gameDisplay.blit(text_surface,text_rect)

    def jump(self):

            #We check if the player sprite is standing on a platform on or not.
            if self.vel.y>0:
                self.img_hero.rect.y+=1
                hits=pygame.sprite.spritecollide(self.img_hero,self.platforms,False)
                self.img_hero.rect.y -= 1
                if hits:
                    self.jump_sound.play()
                    self.vel.y = -10

    def gameMenuScreen(self):
        menu_active = True
        # Start playing the main menu music
        pygame.mixer.music.play(-1)  # -1 means loop indefinitely
        display_size = self.gameDisplay.get_size()
        while menu_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.menu_background = pygame.image.load('./background1.jpeg')
            self.menu_background = pygame.transform.scale(self.menu_background, display_size)
            self.gameDisplay.blit(self.menu_background, (0, 0))

            # Load the images
            start_button_img = pygame.image.load('./start.png')
            store_button_img = pygame.image.load('./store.png')
            self.title = pygame.image.load('./title.png')
            # Set the size of the buttons
            button_width = 140
            button_height = 40

            # Resize the images to match the button size
            start_button_img = pygame.transform.scale(start_button_img, (button_width, button_height))
            store_button_img = pygame.transform.scale(store_button_img, (button_width, button_height))
            self.title = pygame.transform.scale(self.title, (350, 80))

            # Display "Title"
            title_button_rect = self.title.get_rect(topleft=(90, 90))
            self.gameDisplay.blit(self.title, title_button_rect.topleft)

            # Display "Start" button
            start_button_rect = start_button_img.get_rect(topleft=(display_width / 2 - 60, display_height / 2 - 30))
            start_button_color = start_button_img
            if start_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1:
                # Action when "Start" button is clicked
                menu_active = False
                pygame.mixer.music.stop()  # Stop the music when leaving the menu
                self.run()  # You need to define this method
            self.gameDisplay.blit(start_button_color, start_button_rect.topleft)

            # Display "Store" button
            store_button_rect = store_button_img.get_rect(topleft=(display_width / 2 - 60, display_height / 2 + 50))
            store_button_color = store_button_img
            if store_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1:
                # Action when "Store" button is clicked
                self.storeScreen()
                print("Store button clicked")  # Add your store functionality here
            self.gameDisplay.blit(store_button_color, store_button_rect.topleft)
            pygame.display.update()
            self.clock.tick(fps) 

    def storeScreen(self):
        store_active = True
        # Start playing the main menu music
        pygame.mixer.music.play(-1)  # -1 means loop indefinitely
        display_size = self.gameDisplay.get_size()
        directory = "/Users/dimka/KBTU/pp2-fall-2023/game/DJ/characters"
        len_files = len(os.listdir(directory))
        while store_active:
            pos = pygame.mouse.get_pos()
            self.menu_background = pygame.image.load('./blue_back.jpg')
            self.menu_background = pygame.transform.scale(self.menu_background, display_size)
            self.gameDisplay.blit(self.menu_background, (0, 0))

            if self.store.characters.get(f"character{self.store.active_characted_id}").is_unlocked:
                func_img = pygame.image.load('./prehistory/continue.png')
                func_img = pygame.transform.scale(func_img, (180, 40))
                func_img_rect = func_img.get_rect(topleft=(display_width / 2 - 75, display_height / 2 + 100))
                self.gameDisplay.blit(func_img, func_img_rect.topleft)
                if func_img_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1:
                    # Action when "Select" button is clicked
                    if self.store.set_active_character(f"character{self.store.active_characted_id}"):
                        self.img_hero.image = self.store.active_character

            else:
                func_img = pygame.image.load('./buy.png')
                func_img = pygame.transform.scale(func_img, (120, 30))
                func_img_rect = func_img.get_rect(topleft=(display_width / 2 - 50, display_height / 2 + 100))
                self.gameDisplay.blit(func_img, func_img_rect.topleft)
                self.messageToScreen(f"PRICE : {self.store.characters.get(f'character{self.store.active_characted_id}').price}", 40, white, display_width / 2, display_height / 2 + 150)
                if func_img_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1:
                    # Action when "Buy" button is clicked
                    if self.store.purchase_character(f"character{self.store.active_characted_id}"):
                        func_img = pygame.image.load('./prehistory/continue.png')
                        func_img = pygame.transform.scale(func_img, (180, 40))
                        func_img_rect = func_img.get_rect(topleft=(display_width / 2 - 75, display_height / 2 + 100))
                        self.gameDisplay.blit(func_img, func_img_rect.topleft)
            
                        self.img_hero.image = self.store.active_character
                        self.coin_score = self.store.collected_coins
                    else:
                        self.messageToScreen("Coins are not enough!", 40, white, display_width / 2 - 50, display_height / 2 + 150)

            current_ch_img = pygame.image.load(f'./characters/ch{self.store.active_characted_id}.png')
            current_ch_img = pygame.transform.scale(current_ch_img, (150, 150))
            current_ch_rect = current_ch_img.get_rect(topleft=(display_width / 2 - 75, display_height / 2 - 90))
            self.gameDisplay.blit(current_ch_img, current_ch_rect.topleft)

            # Load the images
            left_button_img = pygame.image.load('./left.png')
            right_button_img = pygame.image.load('./right.png')
            title = pygame.image.load('./store.png')
            self.messageToScreen("Collected Coins : "+(str)(self.store.collected_coins), 40, yellow, display_width / 2, 150)
        
            # Resize the images to match the button size
            left_button_img = pygame.transform.scale(left_button_img, (50, 50))
            right_button_img = pygame.transform.scale(right_button_img, (50, 50))
            title = pygame.transform.scale(title, (180, 60))

            title_rect = title.get_rect(topleft=(display_width / 2 - 80, 80))
            self.gameDisplay.blit(title, title_rect.topleft)
            # Display "Left" button
            left_button_rect = left_button_img.get_rect(topleft=(display_width / 2 - 180, display_height / 2 - 40))
            self.gameDisplay.blit(left_button_img, left_button_rect.topleft)

            # Display "Right" button
            right_button_rect = right_button_img.get_rect(topleft=(display_width / 2 + 150, display_height / 2 - 40))
                 
            self.gameDisplay.blit(right_button_img, right_button_rect.topleft)
            
            go_menu = pygame.image.load('./go_menu.png')
            go_menu = pygame.transform.scale(go_menu, (100, 40))
            go_menu_rect = go_menu.get_rect(topleft=(display_width / 2 - 45, display_height / 2 + 200))
            
            if go_menu_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1:
                g.__init__()
                g.gameMenuScreen()

            self.gameDisplay.blit(go_menu, go_menu_rect.topleft)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos[0] > display_width / 2 - 180 and pos[0] < display_width / 2 - 130 and pos[1] > display_height / 2 - 40 and pos[1] < display_height / 2 + 10:
                        # Action when "Left" button is clicked
                        if self.store.active_characted_id == 0:
                            self.store.active_characted_id = len_files - 2
                        else:
                            self.store.active_characted_id -= 1
                    elif pos[0] > display_width / 2 + 150 and pos[0] < display_width / 2 + 200 and pos[1] > display_height / 2 - 40 and pos[1] < display_height / 2 + 10:
                        # Action when "Right" button is clicked
                        if self.store.active_characted_id == len_files - 2:
                            self.store.active_characted_id = 0
                        else:
                            self.store.active_characted_id += 1
        
            pygame.display.update()
            self.clock.tick(fps)

    def startScreen(self):
        display_size = self.gameDisplay.get_size()
        background_image = pygame.image.load("./prehistory/back1.jpg")  # Replace with your image
        background_image = pygame.transform.scale(background_image, display_size)
        self.gameDisplay.blit(background_image, (0,0))
        continue_image = pygame.image.load("./prehistory/continue.png")  # Replace with your image
        continue_image = pygame.transform.scale(continue_image, (100, 30))
        self.gameDisplay.blit(continue_image, (display_width / 4 * 3, display_height / 4 * 3 + 20))
        self.messageToScreen("Press any key to continue...", 25, red, display_width / 2 + 50, display_height / 4 - 20)
        #self.messageToScreen("High Score: " + str(self.highscore), 25, white, display_width / 2, 35)
        pygame.display.update()
        self.waitForKeyPress()
        com1 = pygame.image.load("./prehistory/com1.png")
        com1 = pygame.transform.scale(com1, display_size)
        self.gameDisplay.blit(com1, (0,0))
        continue_image = pygame.image.load("./prehistory/continue.png")  # Replace with your image
        continue_image = pygame.transform.scale(continue_image, (100, 30))
        self.gameDisplay.blit(continue_image, (display_width / 4 * 3, display_height / 4 * 3 + 20))
        pygame.display.update()
        self.waitForKeyPress()
        com2 = pygame.image.load("./prehistory/com2.png")
        com2 = pygame.transform.scale(com2, display_size)
        continue_image = pygame.image.load("./prehistory/continue.png")  # Replace with your image
        continue_image = pygame.transform.scale(continue_image, (100, 30))
        self.gameDisplay.blit(continue_image, (display_width / 4 * 3, display_height / 4 * 3 + 20))
        self.gameDisplay.blit(com2, (0,0))
        pygame.display.update()
        self.waitForKeyPress()
        self.gameMenuScreen()
        g.run()

    def gameOverScreen(self):
        display_size = self.gameDisplay.get_size()
        self.menu_background = pygame.image.load('./game_over.jpeg')
        self.menu_background = pygame.transform.scale(self.menu_background, display_size)

        self.gameDisplay.blit(self.menu_background, (0, 0))
        self.messageToScreen("OOPS!...GAME-OVER", 40, white, display_width / 2, 120)
        self.messageToScreen("Score : "+(str)(self.score), 40, white, display_width / 2, display_height / 2-160)
        self.messageToScreen(f"Coin score : {self.coin_score}", 40, white, display_width / 2 , display_height / 2 - 50)
        with open(path.join(self.dir, c_file), 'r') as f:                      # writing the new highscore in the file
                self.coin_score += int(f.read())
        with open(path.join(self.dir, c_file), 'w') as f:                      # writing the new highscore in the file
                f.write(str(self.coin_score))
        if self.score > self.highscore:
            self.highscore = self.score
            self.messageToScreen("CONGRATULATIONS!!!  NEW HIGH SCORE!", 30, white, display_width / 2, display_height / 2 - 90)
            with open(path.join(self.dir, hs_file), 'w') as f:                      # writing the new highscore in the file
                f.write(str(self.score))
        else:
            self.messageToScreen("High Score: " + str(self.highscore), 30, white, display_width / 2, display_height / 2 - 90)
        # Load the images
        try_again = pygame.image.load('./try_again.png')
        go_menu = pygame.image.load('./go_menu.png')
        # Resize the images to match the button size
        try_again = pygame.transform.scale(try_again, (140, 25))
        go_menu = pygame.transform.scale(go_menu, (80, 25))
    
        try_again_rect = try_again.get_rect(topleft=(display_width / 4 - 20, display_height / 2))
       
        self.gameDisplay.blit(try_again, try_again_rect.topleft)
        go_menu_rect = go_menu.get_rect(topleft=(display_width / 2 + 70, display_height / 2))

        self.gameDisplay.blit(go_menu, go_menu_rect.topleft)

        pygame.display.update()
        waiting=True
        action = ""
        print(1)
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if try_again_rect.collidepoint(event.pos):
                        # Action when "Try Again" button is clicked
                        waiting = False
                        action = "try"
                    elif go_menu_rect.collidepoint(event.pos):
                        # Action when "Menu" button is clicked
                        waiting = False
                        action = "menu"

            self.clock.tick(fps)
        if action == "try":
            pygame.mixer.music.stop()  # Stop the music when leaving the menu
            g.__init__()
            g.run()
        elif action == "menu":
            pygame.mixer.music.stop()  # Stop the music when leaving the menu
            g.__init__()
            g.gameMenuScreen()

    def waitForKeyPress(self):
        waiting=True
        while waiting:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    waiting=False
                    self.gameExit=True
                if event.type==pygame.KEYUP:
                    waiting=False
                    self.gameOver=False
                    self.gameExit=False

g=Game()
g.startScreen()
