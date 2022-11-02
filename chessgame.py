import pygame, sys, random, chess

pygame.init()
pygame.mixer.init()

fps = pygame.time.Clock()
screen = pygame.display.set_mode([1280, 720])

WHITE = (255, 255, 255)

gui_font = pygame.font.SysFont("Futura", 65)

boardimg = pygame.image.load("assets\images\\board.png")
boardimg = pygame.transform.scale(boardimg, (720, 720)) 

class Button:
	def __init__(self,text,width,height,pos,elevation):
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#80a454'

		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#537133'
  
		self.text_surf = gui_font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self): 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)

	def check_click(self, position):
		if position[0] in range(self.top_rect.left, self.bottom_rect.right) and position[1] in range(self.top_rect.top, self.top_rect.bottom):
			self.dynamic_elecation = 0
			return True
		self.dynamic_elecation = self.elevation
		return False

	def changeColor(self, position):
		if position[0] in range(self.top_rect.left, self.top_rect.right) and position[1] in range(self.top_rect.top, self.top_rect.bottom):
			self.top_color = '#95bb4a'
		else:
			self.top_color = '#80a454'

def game_loop():
	pygame.display.set_caption("Chess")
	
	while True:
		screen.fill((49, 46, 43))
		screen.blit(boardimg, (280, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
		pygame.display.update()
		fps.tick(60)
	
def game_over():
	pygame.display.set_caption("Game Over!")

	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
		pygame.display.update()
		fps.tick(60)

def main_menu():
	pygame.display.set_caption("Main Menu")
	
	title_font = pygame.font.SysFont("Futura", 100)
	title = title_font.render('Chess!', True, WHITE)
	title_rect = title.get_rect(center= (640, 100))
	
	play_btn = Button('Play', 250, 80, (515, 300), 5)
	quit_btn = Button('Quit', 250, 80, (515, 500), 5)
	
	while True:
		screen.fill((49, 46, 43))
		screen.blit(title, title_rect)

		MENU_MOUSE_POS = pygame.mouse.get_pos()
		
		for button in [play_btn, quit_btn]:
			button.changeColor(MENU_MOUSE_POS)
			button.draw()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if play_btn.check_click(MENU_MOUSE_POS):
					game_loop()
				if quit_btn.check_click(MENU_MOUSE_POS):
					sys.exit(0)
		
		pygame.display.update()
		fps.tick(60)

main_menu()