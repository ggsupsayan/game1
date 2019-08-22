import pygame
pygame.init()

# window init #
win_width = 240
win_height = 160
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Quest")

# player attributes #
p_x = 16
p_y = 0
p_width = 16
p_height = 16
p_vel = 16
p_right = False
p_left = False
p_up = False
p_down = False
p_cycle_count = 0
p_floor = 0
p_atk = "none"
p_weapon_state = False
p_health = 1
p_char = None
p_stars = [0,0,0,0,0]

star_cycle = 0

# misc sprites #

f3_plat = pygame.image.load("sprites/see_through_tile.png")

star_numbers = [pygame.image.load("sprites/star_nums1.png"), 
pygame.image.load("sprites/star_nums2.png"), 
pygame.image.load("sprites/star_nums3.png"), 
pygame.image.load("sprites/star_nums4.png"),
pygame.image.load("sprites/star_nums5.png"), 
pygame.image.load("sprites/star_nums6.png"),
pygame.image.load("sprites/star_nums7.png")]

star_spr = [pygame.image.load("sprites/star_sprite1.png"),
pygame.image.load("sprites/star_sprite2.png"),
pygame.image.load("sprites/star_sprite3.png")]

demon_left = [pygame.image.load("sprites/big_demon_run_left_anim_f0.png"), 
pygame.image.load("sprites/big_demon_run_left_anim_f1.png"), 
pygame.image.load("sprites/big_demon_run_left_anim_f2.png"), 
pygame.image.load("sprites/big_demon_run_left_anim_f3.png")]

f1_spike_down = pygame.image.load("sprites/floor_spikes_anim_f0.png")
f1_side_spikes_down = pygame.image.load("sprites/f1_spikes_down.png")
f1_btn_up = pygame.image.load("sprites/btn_up.png")
f1_btn_down = pygame.image.load("sprites/btn_down.png")
f1_door = pygame.image.load("sprites/door_closed.png")

f2_sword_anim = [pygame.image.load("sprites/sword_rock_down1.png"), 
pygame.image.load("sprites/sword_rock_down2.png"), 
pygame.image.load("sprites/sword_rock_down3.png"), 
pygame.image.load("sprites/sword_rock_down4.png"),
pygame.image.load("sprites/sword_rock_down5.png"), 
pygame.image.load("sprites/sword_rock_down6.png"), 
pygame.image.load("sprites/sword_rock_down7.png"), 
pygame.image.load("sprites/sword_rock_down8.png")]
f2_wood_anim = [pygame.image.load("sprites/wood_open_anim1.png"),
pygame.image.load("sprites/wood_open_anim2.png"),
pygame.image.load("sprites/wood_open_anim3.png"),
pygame.image.load("sprites/wood_open_anim4.png")]
f2_spikes_down = pygame.image.load("sprites/floor_spikes_three_down.png")
f2_spikes_up = pygame.image.load("sprites/floor_spikes_three_up.png") 

# enemy attributes #
slime_sprite = [pygame.image.load("sprites/swampy_run_anim_f0.png"), 
pygame.image.load("sprites/swampy_run_anim_f1.png"), 
pygame.image.load("sprites/swampy_run_anim_f2.png"), 
pygame.image.load("sprites/swampy_run_anim_f3.png")]

# player sprites #
p_sprite_idle = [pygame.image.load("sprites/knight_m_idle_anim_f0.png"), 
pygame.image.load("sprites/knight_m_idle_anim_f1.png"), 
pygame.image.load("sprites/knight_m_idle_anim_f2.png"), 
pygame.image.load("sprites/knight_m_idle_anim_f3.png")]
p_sprite_down = [pygame.image.load("sprites/knight_m_run_anim_f0.png"), 
pygame.image.load("sprites/knight_m_run_anim_f1.png"), 
pygame.image.load("sprites/knight_m_run_anim_f2.png"), 
pygame.image.load("sprites/knight_m_run_anim_f3.png")]
p_sprite_up = [pygame.image.load("sprites/knight_m_up_anim_f0.png"), 
pygame.image.load("sprites/knight_m_up_anim_f1.png"), 
pygame.image.load("sprites/knight_m_up_anim_f2.png"), 
pygame.image.load("sprites/knight_m_up_anim_f3.png")]
p_sprite_left = [pygame.image.load("sprites/knight_m_left_anim_f0.png"), 
pygame.image.load("sprites/knight_m_left_anim_f1.png"), 
pygame.image.load("sprites/knight_m_left_anim_f2.png"), 
pygame.image.load("sprites/knight_m_left_anim_f3.png")]
p_sprite_right = [pygame.image.load("sprites/knight_m_idle_anim_f0.png"), 
pygame.image.load("sprites/knight_m_run_anim_f1.png"), 
pygame.image.load("sprites/knight_m_run_anim_f2.png"), 
pygame.image.load("sprites/knight_m_run_anim_f3.png")]
p_weapon = pygame.image.load("sprites/weapon_rusty_sword.png")
p_heart = pygame.image.load("sprites/heart.png")

curr_floor = None 

colors = {
	"black" : (0,0,0),
	"grey" : (125,125,125),
	"white" : (255,255,255),
	"red" : (255,0,0),
	"orange" : (255,117,26),
	"yellow" : (255,255,0),
	"green" : (0,255,0),
	"blue" : (0,0,255),
	"purple" : (153,0,204)
}

# __________floor zero stuff___________ #
f0 = [
 ["W"," ","W","W","W","W","W","W","W","W","W","W","W","W","W"],
 [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
 ["W"," "," "," "," "," "," "," "," "," "," "," "," "," ","W"],
 ["W"," "," "," "," "," "," "," "," "," "," "," "," "," ","W"],
 ["W"," "," "," "," "," "," "," "," "," "," "," "," "," ","W"],
 ["W"," "," "," "," "," "," "," "," "," "," "," "," "," ","W"],
 ["W"," "," "," "," "," "," "," "," "," "," "," "," "," ","W"],
 ["W"," "," "," "," "," "," "," "," "," "," "," "," "," ","W"],
 ["W"," "," "," "," "," "," "," "," "," "," "," "," "," ","W"],
 ["W"," ","W","W","W","W","W","W","W","W","W","W","W","W","W"]]


f0_cycle_count = 2
f0_mov_count = 0
f0_cursor = 0
f0_run_state = 0
f0_cs_state = False


# __________floor one stuff___________ #
f1 = [
 ["W","W","W","W","W","W","W","W","W","W","W","W","W","W","W"],
 ["W","P"," "," ","s"," "," "," "," "," "," "," ","X","E","W"],
 ["W"," "," ","s","s","s"," "," "," "," "," "," ","X","X","W"],
 ["W"," "," "," "," "," "," "," "," "," "," "," "," "," ","W"],
 ["W"," "," "," "," "," ","X","X","X","X","X","X","X","X","W"],
 ["W"," "," "," "," "," ","X","X","X","X","X","X","X","X","W"],
 ["W"," "," "," "," "," ","X","X","X","X","X","X"," "," ","W"],
 ["W"," "," "," "," "," "," "," "," "," "," "," "," ","B","W"],
 ["W"," "," "," "," "," ","X","X","X","X","X","X"," "," ","W"],
 ["W","W","W","W","W","W","W","W","W","W","W","W","W","W","W"]]


f1_btn_state = False
f1_sec_co = 0


# __________floor two stuff___________ #
f2 = [
 ["W","W","W","W","W","W","W","W","W","W","W","W","W","W","W"],
 ["W","P"," "," "," "," "," "," "," "," "," "," "," "," ","W"],
 ["W"," "," "," "," "," "," "," "," "," "," "," "," "," ","W"],
 ["W","X","X","X","W","W","W","W","W","W","W","W","W"," ","W"],
 ["W"," "," "," ","X","X","X","X","X","X","X","X","W"," ","W"],
 ["W","X","X","X","W","W","W","W","W","W","X","*","W"," ","W"],
 ["W"," "," "," ","W"," "," "," "," ","W","W","W","W"," ","W"],
 ["W"," "," "," ","W"," "," "," "," "," "," "," "," "," ","W"],
 ["W"," ","S"," ","W"," "," "," "," "," "," "," "," "," ","W"],
 ["W","W","W","W","W","W","W","W","W","W","W","W","W","W","W"]]


f2_cycle = 1
f2_sp_st = True


f3 = [
 ["W","W","W","W","W","W","W","W","W","W","W","W","W","W","W"],
 ["W","P","X","X","X","X","*","X","X","X","X","X","X","E","W"],
 ["W"," ","X","X","X","h","h","X","X","X","X","X","X"," ","W"],
 ["W"," ","X","X","X","h","X","X","X","X","X","X","X"," ","W"],
 ["W"," ","X","X","X","h","h","h","X","X","X","X","X"," ","W"],
 ["W"," ","X","X","X","X","X","h","X","X","X","X","X"," ","W"],
 ["W"," ","X","X","X","X","X","h","X","X","X","X","X"," ","W"],
 ["W"," "," "," "," ","e"," "," "," "," "," "," "," "," ","W"],
 ["W"," "," "," "," "," "," ","e"," "," "," "," "," "," ","W"],
 ["W","W","W","W","W","W","W","W","W","W","W","W","W","W","W"]]


f3_p_count = 0
star_check = False		
# [counter, s1, s2, s1 backwards flag, s2 backwards flag]
f3_slime_cycles = [0,5,7,0,0,2,2]

# loading backgrounds #
bg = pygame.image.load("sprites/bg.png")
bg_1 = pygame.image.load("sprites/bg_1.png")
bg_2 = pygame.image.load("sprites/bg_2.png")
bg_3 = pygame.image.load("sprites/bg_3.png")
title = [pygame.image.load("sprites/title_screen1.png"), pygame.image.load("sprites/title_screen2.png")]
win_screen = pygame.image.load("sprites/win_bg.png")


def assign_p_sprite(selection):
	global p_sprite_idle, p_sprite_right, p_sprite_left, p_sprite_down, p_sprite_up
	if selection == 0: #knight
		p_sprite_idle = [pygame.image.load("sprites/knight_m_idle_anim_f0.png"), 
		pygame.image.load("sprites/knight_m_idle_anim_f1.png"), 
		pygame.image.load("sprites/knight_m_idle_anim_f2.png"), 
		pygame.image.load("sprites/knight_m_idle_anim_f3.png")]
		p_sprite_down = [pygame.image.load("sprites/knight_m_run_anim_f0.png"), 
		pygame.image.load("sprites/knight_m_run_anim_f1.png"), 
		pygame.image.load("sprites/knight_m_run_anim_f2.png"), 
		pygame.image.load("sprites/knight_m_run_anim_f3.png")]
		p_sprite_up = [pygame.image.load("sprites/knight_m_up_anim_f0.png"), 
		pygame.image.load("sprites/knight_m_up_anim_f1.png"), 
		pygame.image.load("sprites/knight_m_up_anim_f2.png"), 
		pygame.image.load("sprites/knight_m_up_anim_f3.png")]
		p_sprite_left = [pygame.image.load("sprites/knight_m_left_anim_f0.png"), 
		pygame.image.load("sprites/knight_m_left_anim_f1.png"), 
		pygame.image.load("sprites/knight_m_left_anim_f2.png"), 
		pygame.image.load("sprites/knight_m_left_anim_f3.png")]
		p_sprite_right = [pygame.image.load("sprites/knight_m_run_anim_f0.png"), 
		pygame.image.load("sprites/knight_m_run_anim_f1.png"), 
		pygame.image.load("sprites/knight_m_run_anim_f2.png"), 
		pygame.image.load("sprites/knight_m_run_anim_f3.png")]
	if selection == 1: #wizzard
		p_sprite_idle = [pygame.image.load("sprites/wizzard_m_idle_anim_f0.png"), 
		pygame.image.load("sprites/wizzard_m_idle_anim_f1.png"), 
		pygame.image.load("sprites/wizzard_m_idle_anim_f2.png"), 
		pygame.image.load("sprites/wizzard_m_idle_anim_f3.png")]
		p_sprite_down = [pygame.image.load("sprites/wizzart_m_run_anim_f0.png"), 
		pygame.image.load("sprites/wizzart_m_run_anim_f1.png"), 
		pygame.image.load("sprites/wizzart_m_run_anim_f2.png"), 
		pygame.image.load("sprites/wizzart_m_run_anim_f3.png")]
		p_sprite_up = [pygame.image.load("sprites/wizard_m_up_anim_f1.png"), 
		pygame.image.load("sprites/wizard_m_up_anim_f2.png"), 
		pygame.image.load("sprites/wizard_m_up_anim_f3.png"), 
		pygame.image.load("sprites/wizard_m_up_anim_f4.png")]
		p_sprite_left = [pygame.image.load("sprites/wizard_m_left_anim_f1.png"), 
		pygame.image.load("sprites/wizard_m_left_anim_f2.png"), 
		pygame.image.load("sprites/wizard_m_left_anim_f3.png"), 
		pygame.image.load("sprites/wizard_m_left_anim_f4.png")]
		p_sprite_right = [pygame.image.load("sprites/wizzart_m_run_anim_f0.png"), 
		pygame.image.load("sprites/wizzart_m_run_anim_f1.png"), 
		pygame.image.load("sprites/wizzart_m_run_anim_f2.png"), 
		pygame.image.load("sprites/wizzart_m_run_anim_f3.png")]
	if selection == 2: #necro
		p_sprite_idle = [pygame.image.load("sprites/necromancer_idle_re1.png"), 
		pygame.image.load("sprites/necromancer_idle_re2.png"), 
		pygame.image.load("sprites/necromancer_idle_re3.png"), 
		pygame.image.load("sprites/necromancer_idle_re4.png")]
		p_sprite_down = [pygame.image.load("sprites/necromancer_run_re1.png"), 
		pygame.image.load("sprites/necromancer_run_re2.png"), 
		pygame.image.load("sprites/necromancer_run_re3.png"), 
		pygame.image.load("sprites/necromancer_run_re4.png")]
		p_sprite_up = [pygame.image.load("sprites/necromancer_run_up_re1.png"), 
		pygame.image.load("sprites/necromancer_run_up_re2.png"), 
		pygame.image.load("sprites/necromancer_run_up_re3.png"), 
		pygame.image.load("sprites/necromancer_run_up_re4.png")]
		p_sprite_left = [pygame.image.load("sprites/necromancer_run_left_re1.png"), 
		pygame.image.load("sprites/necromancer_run_left_re2.png"), 
		pygame.image.load("sprites/necromancer_run_left_re3.png"), 
		pygame.image.load("sprites/necromancer_run_left_re4.png")]
		p_sprite_right = [pygame.image.load("sprites/necromancer_run_re1.png"), 
		pygame.image.load("sprites/necromancer_run_re2.png"), 
		pygame.image.load("sprites/necromancer_run_re3.png"), 
		pygame.image.load("sprites/necromancer_run_re4.png")]

def draw_frame():
	global p_floor, p_atk, p_x, p_y, p_weapon_state, star_cycle, star_check
	global f0_cursor, f0_cycle_count, f0_mov_count, f0_run_state
	global f1, f1_btn_state, f1_sec_co
	global f2, f2_cycle, f2_sp_st
	global f3_p_count

	if p_floor == 0:
		win.blit(title[0], (0,0))
		p_x = 16
		p_y = 0
		if not f0_cs_state:
			if f0_cursor == 0:
				win.fill(colors["black"])
				win.blit(title[0], (0,0))
				pygame.draw.rect(win, colors["white"], (98, 89, 44, 15), 1)
			else:
				win.fill(colors["black"])
				win.blit(title[0], (0,0))
				pygame.draw.rect(win, colors["white"], (103, 107, 34, 15), 1)

			# knight/demon anim
			if f0_mov_count < 260 and f0_run_state == 0:
				win.blit(p_sprite_right[f0_cycle_count], (f0_mov_count, 125))
				f0_mov_count += 5
			elif f0_mov_count > 0 and f0_run_state == 0:
				f0_run_state = 1
			elif f0_mov_count > -60 and f0_run_state == 1:
				win.blit(p_sprite_left[f0_cycle_count], (f0_mov_count, 125))
				win.blit(demon_left[f0_cycle_count], (f0_mov_count + 30, 120))
				f0_mov_count -= 10

			if f0_cycle_count < 3:
				f0_cycle_count += 1
			else:
				f0_cycle_count = 0
		else:
			win.fill(colors["black"])
			win.blit(title[1], (0,0))
			if f0_cursor == 0:
				win.fill(colors["black"])
				win.blit(title[1], (0,0))
				pygame.draw.rect(win, colors["white"], (73, 96, 20, 26), 1)
				assign_p_sprite(0)
			elif f0_cursor == 1:
				win.fill(colors["black"])
				win.blit(title[1], (0,0))
				pygame.draw.rect(win, colors["white"], (110, 78, 20, 26), 1)
				assign_p_sprite(1)
			else:
				win.fill(colors["black"])
				win.blit(title[1], (0,0))
				pygame.draw.rect(win, colors["white"], (145, 98, 20, 26), 1)
				assign_p_sprite(2)


			win.blit(pygame.transform.scale(p_sprite_idle[f0_cycle_count], (32,56)), (105,95))
			if f0_cycle_count < 3:
				f0_cycle_count += 1
			else:
				f0_cycle_count = 0




	elif p_floor == 1:
		win.blit(bg_1, (0,0))
		
		if f1_btn_state:
			win.blit(f1_spike_down, (12 * 16, 1 * 16))
			win.blit(f1_spike_down, (12 * 16, 2 * 16))
			win.blit(f1_spike_down, (13 * 16, 2 * 16))
			win.blit(f1_side_spikes_down, (14 * 16, 1 * 16))
			win.blit(f1_btn_down, (13 * 16, 7 * 16))

		if f1_sec_co == 4:
			win.blit(pygame.image.load("sprites/f1_wasd.png"), (3*16, 1*16))

		if p_atk == "up":
			win.blit(p_weapon, (p_x + 3, p_y - 2))
			pygame.time.delay(70)
			pygame.display.update()
		elif p_atk == "right":
			win.blit(pygame.transform.rotate(p_weapon, 270), (p_x + 10, p_y + 16))
			pygame.time.delay(70)
			pygame.display.update()
		elif p_atk == "down":
			win.blit(pygame.transform.rotate(p_weapon, 180), (p_x + 3, p_y + 22))
			pygame.time.delay(70)
			pygame.display.update()
		elif p_atk == "left":
			win.blit(pygame.transform.rotate(p_weapon, 90), (p_x - 12, p_y + 16))
			pygame.time.delay(70)
			pygame.display.update()

		if p_left:
			win.blit(p_sprite_left[p_cycle_count], (p_x, p_y))
		elif p_right:
			win.blit(p_sprite_right[p_cycle_count], (p_x, p_y))
		elif p_up:
			win.blit(p_sprite_up[p_cycle_count], (p_x, p_y))
		elif p_down:
			win.blit(p_sprite_down[p_cycle_count], (p_x, p_y))
		else:
			win.blit(p_sprite_idle[p_cycle_count], (p_x, p_y))

		for i in range(0, 10):
			for j in range(0, 15):
				if f1[i][j] == "E" and p_x == j*16 and p_y + 16 == i*16:
					p_floor = 2
					f1_btn_state = False
					p_x = 16
					p_y = 0
					f1[1][12] = "X"
					f1[2][12] = "X"
					f1[2][13] = "X"
				if f1[i][j] == "X" and p_x == j*16 and p_y + 16 == i*16:
					win.blit(pygame.image.load("sprites/knight_m_death.png"), (p_x, p_y))
					pygame.display.update()
					pygame.time.delay(500)
					p_x = 16
					p_y = 0	
				if f1[i][j] == "B" and p_x == j*16 and p_y + 16 == i*16:
					f1[1][12] = " "
					f1[2][12] = " "
					f1[2][13] = " "
					f1_btn_state = True
				if f1[i][j] == "s" and p_x == j*16 and p_y + 16 == i*16:
					if i == 1 and j == 4 and f1_sec_co == 0:
						f1_sec_co += 1
					elif i == 2 and j == 3 and f1_sec_co == 1:
						f1_sec_co += 1
					elif i == 2 and j == 5 and f1_sec_co == 2:
						f1_sec_co += 1
					elif i == 2 and j == 4 and f1_sec_co == 3:
						f1_sec_co += 1

	elif p_floor == 2:
		win.fill(colors["black"])
		win.blit(bg_2, (0,0))

		if f1_sec_co == 4:
			for j in range(4,12):
				f2[4][j] = " "
			f2[5][10] = " "

		if f2_cycle == 10:
			f2_sp_st = not f2_sp_st
			f2_cycle = 1
		f2_cycle += 1
		
		if f2_sp_st == True:
			win.blit(f2_spikes_down, (16,48))
			win.blit(f2_spikes_down, (16,80))
			for i in range(3,6):
				for j in range(1,4):
					if i == 3 or i == 5:
						f2[i][j] = " "

		elif f2_sp_st == False:
			win.blit(f2_spikes_up, (16,48))
			win.blit(f2_spikes_up, (16,80))
			for i in range(3,6):
				for j in range(1,4):
					if i == 3 or i == 5:
						f2[i][j] = "X"



		if p_weapon_state:
			win.blit(f2_sword_anim[7],(32,112))
			win.blit(pygame.image.load("sprites/floor_1.png"), (32, 112))
			win.blit(f2_wood_anim[3],(96,112))
		if star_check:
			win.blit(pygame.image.load("sprites/nothing.png"), (11*16,5*16))
		if p_atk == "up":
			win.blit(p_weapon, (p_x + 3, p_y - 2))
			pygame.time.delay(70)
			pygame.display.update()
		elif p_atk == "right":
			win.blit(pygame.transform.rotate(p_weapon, 270), (p_x + 10, p_y + 16))
			pygame.time.delay(70)
			pygame.display.update()
		elif p_atk == "down":
			win.blit(pygame.transform.rotate(p_weapon, 180), (p_x + 3, p_y + 22))
			pygame.time.delay(70)
			pygame.display.update()
		elif p_atk == "left":
			win.blit(pygame.transform.rotate(p_weapon, 90), (p_x - 12, p_y + 16))
			pygame.time.delay(70)
			pygame.display.update()

		if p_left:
			win.blit(p_sprite_left[p_cycle_count], (p_x, p_y))
		elif p_right:
			win.blit(p_sprite_right[p_cycle_count], (p_x, p_y))
		elif p_up:
			win.blit(p_sprite_up[p_cycle_count], (p_x, p_y))
		elif p_down:
			win.blit(p_sprite_down[p_cycle_count], (p_x, p_y))
		else:
			win.blit(p_sprite_idle[p_cycle_count], (p_x, p_y))

		for i in range(0, 10):
			for j in range(0, 15):
				
				if f2[i][j] == "*":
					if p_x == j*16 and p_y + 16 == i*16:
						p_stars[0] = 1
						star_check = True
					if star_check == False:
						win.blit(star_spr[star_cycle], (176,80))
						if star_cycle < 2:
							star_cycle += 1
						else:
							star_cycle = 0
				
				if f2[i][j] == "E" and p_x == j*16 and p_y + 16 == i*16:
					p_floor = 3
					p_x = 16
					p_y = 0
					star_check = False
				if f2[i][j] == "X" and p_x == j*16 and p_y + 16 == i*16:
					win.blit(pygame.image.load("sprites/knight_m_death.png"), (p_x, p_y))
					pygame.display.update()
					pygame.time.delay(500)
					p_x = 16
					p_y = 0	
				if f2[i][j] == "S" and p_x == j*16 and p_y + 32 == i*16:
					p_weapon_state = True
					f2[i][j] = " "
					win.blit(f2_sword_anim[0],(32,112))
					pygame.display.update()
					win.blit(pygame.image.load("sprites/floor_1.png"), (32, 112))
					win.blit(p_sprite_down[p_cycle_count], (p_x, p_y))
					pygame.display.update()
					pygame.time.delay(150)
					win.blit(f2_sword_anim[1],(32,112))
					pygame.display.update()
					pygame.time.delay(150)
					win.blit(f2_sword_anim[2],(32,112))
					pygame.display.update()
					pygame.time.delay(150)
					win.blit(f2_sword_anim[3],(32,112))
					pygame.display.update()
					pygame.time.delay(150)
					win.blit(f2_sword_anim[4],(32,112))
					pygame.display.update()
					pygame.time.delay(150)
					win.blit(f2_sword_anim[5],(32,112))
					pygame.display.update()
					pygame.time.delay(150)
					win.blit(f2_sword_anim[6],(32,112))
					pygame.display.update()
					pygame.time.delay(150)
					win.blit(f2_sword_anim[7],(32,112))
					pygame.display.update()
					pygame.time.delay(50)

					win.blit(f2_wood_anim[0],(96,112))
					pygame.display.update()
					pygame.time.delay(200)
					win.blit(f2_wood_anim[1],(96,112))
					pygame.display.update()
					pygame.time.delay(200)
					win.blit(f2_wood_anim[2],(96,112))
					pygame.display.update()
					pygame.time.delay(200)
					win.blit(f2_wood_anim[3],(96,112))
					f2[7][6] = "E"

		'''
		s = pygame.Surface((16,16))  # the size of your rect
		s.set_alpha(128)                # alpha level
		s.fill((255,0,0))           # this fills the entire surface
		win.blit(s, (p_x,p_y + 16)) 
		'''
	elif p_floor == 3:
		win.fill(colors["black"])
		win.blit(bg_3, (0,0))
		p_weapon_state = True

		if f3_p_count == 1:
			win.blit(f3_plat, (7*16,6*16))
			f3[6][7] = " "
		elif f3_p_count == 2:
			win.blit(f3_plat, (7*16,6*16))
			win.blit(f3_plat, (7*16,5*16))
			f3[6][7] = " "
			f3[5][7] = " "
		elif f3_p_count == 3:
			win.blit(f3_plat, (7*16,6*16))
			win.blit(f3_plat, (7*16,5*16))
			win.blit(f3_plat, (7*16,4*16))
			f3[6][7] = " "
			f3[5][7] = " "
			f3[4][7] = " "
		elif f3_p_count == 4:
			win.blit(f3_plat, (7*16,6*16))
			win.blit(f3_plat, (7*16,5*16))
			win.blit(f3_plat, (7*16,4*16))
			win.blit(f3_plat, (6*16,4*16))
			f3[6][7] = " "
			f3[5][7] = " "
			f3[4][7] = " "
			f3[4][6] = " "
		elif f3_p_count == 5:
			win.blit(f3_plat, (7*16,6*16))
			win.blit(f3_plat, (7*16,5*16))
			win.blit(f3_plat, (7*16,4*16))
			win.blit(f3_plat, (6*16,4*16))
			win.blit(f3_plat, (5*16,4*16))
			f3[6][7] = " "
			f3[5][7] = " "
			f3[4][7] = " "
			f3[4][6] = " "
			f3[4][5] = " "
		elif f3_p_count == 6:
			win.blit(f3_plat, (7*16,6*16))
			win.blit(f3_plat, (7*16,5*16))
			win.blit(f3_plat, (7*16,4*16))
			win.blit(f3_plat, (6*16,4*16))
			win.blit(f3_plat, (5*16,4*16))
			win.blit(f3_plat, (5*16,3*16))
			f3[6][7] = " "
			f3[5][7] = " "
			f3[4][7] = " "
			f3[4][6] = " "
			f3[4][5] = " "
			f3[3][5] = " "
		elif f3_p_count == 7:
			win.blit(f3_plat, (7*16,6*16))
			win.blit(f3_plat, (7*16,5*16))
			win.blit(f3_plat, (7*16,4*16))
			win.blit(f3_plat, (6*16,4*16))
			win.blit(f3_plat, (5*16,4*16))
			win.blit(f3_plat, (5*16,3*16))
			win.blit(f3_plat, (5*16,2*16))
			f3[6][7] = " "
			f3[5][7] = " "
			f3[4][7] = " "
			f3[4][6] = " "
			f3[4][5] = " "
			f3[3][5] = " "
			f3[2][5] = " "
		elif f3_p_count == 8:
			win.blit(f3_plat, (7*16,6*16))
			win.blit(f3_plat, (7*16,5*16))
			win.blit(f3_plat, (7*16,4*16))
			win.blit(f3_plat, (6*16,4*16))
			win.blit(f3_plat, (5*16,4*16))
			win.blit(f3_plat, (5*16,3*16))
			win.blit(f3_plat, (5*16,2*16))
			win.blit(f3_plat, (6*16,2*16))
			f3[6][7] = " "
			f3[5][7] = " "
			f3[4][7] = " "
			f3[4][6] = " "
			f3[4][5] = " "
			f3[3][5] = " "
			f3[2][5] = " "
			f3[2][6] = " "


		# slime stuff #

		

		if f3_slime_cycles[0] < 5:
			f3_slime_cycles[0] += 1
		else:
			f3_slime_cycles[0] = 0

		if f3_slime_cycles[0] == 5:

			if f3_slime_cycles[5] > 0:
				f3[7][f3_slime_cycles[1]] = " "
				if f3_slime_cycles[3] == 0 and f3_slime_cycles[1] < 8:
					f3_slime_cycles[1] += 1
				elif f3_slime_cycles[3] == 0 and f3_slime_cycles[1] == 8:
					f3_slime_cycles[3] = 1
				elif f3_slime_cycles[3] == 1 and f3_slime_cycles[1] > 5:
					f3_slime_cycles[1] -= 1
				elif f3_slime_cycles[3] == 1 and f3_slime_cycles[1] == 5:
					f3_slime_cycles[3] = 0
				f3[7][f3_slime_cycles[1]] = "e"
			else:
				f3[7][f3_slime_cycles[1]] = " "

			if f3_slime_cycles[6] > 0:
				f3[8][f3_slime_cycles[2]] = " "
				if f3_slime_cycles[4] == 0 and f3_slime_cycles[2] < 8:
					f3_slime_cycles[2] += 1
				elif f3_slime_cycles[4] == 0 and f3_slime_cycles[2] == 8:
					f3_slime_cycles[4] = 1
				elif f3_slime_cycles[4] == 1 and f3_slime_cycles[2] > 5:
					f3_slime_cycles[2] -= 1
				elif f3_slime_cycles[4] == 1 and f3_slime_cycles[2] == 5:
					f3_slime_cycles[4] = 0
				f3[8][f3_slime_cycles[2]] = "e"
			else:
				f3[8][f3_slime_cycles[2]] = " "

		if p_atk == "up":
			win.blit(p_weapon, (p_x + 3, p_y - 2))
			pygame.time.delay(70)
			if f3[int(p_y/16)][int(p_x/16)] == "h":
				f3_p_count += 1
			if f3[int(p_y/16)][int(p_x/16)] == "e" and int(p_y/16) == 7:
				f3_slime_cycles[5] -= 1
			if f3[int(p_y/16)][int(p_x/16)] == "e" and int(p_y/16) == 8:
				f3_slime_cycles[6] -= 1
			pygame.display.update()
		elif p_atk == "right":
			win.blit(pygame.transform.rotate(p_weapon, 270), (p_x + 10, p_y + 16))
			pygame.time.delay(70)
			if f3[int((p_y + 16)/16)][int((p_x+16)/16)] == "h":
				f3_p_count += 1
			if f3[int((p_y + 16)/16)][int((p_x+16)/16)] == "e" and int((p_y + 16)/16) == 7:
				f3_slime_cycles[5] -= 1
			if f3[int((p_y + 16)/16)][int((p_x+16)/16)] == "e" and int((p_y + 16)/16) == 8:
				f3_slime_cycles[6] -= 1
			pygame.display.update()
		elif p_atk == "down":
			win.blit(pygame.transform.rotate(p_weapon, 180), (p_x + 3, p_y + 22))
			pygame.time.delay(70)
			if f3[int((p_y + 32)/16)][int(p_x/16)] == "h":
				f3_p_count += 1
			if f3[int((p_y + 32)/16)][int(p_x/16)] == "e" and int((p_y + 32)/16) == 7:
				f3_slime_cycles[5] -= 1
			if f3[int((p_y + 32)/16)][int(p_x/16)] == "e" and int((p_y + 32)/16) == 8:
				f3_slime_cycles[6] -= 1
			pygame.display.update()
		elif p_atk == "left":
			win.blit(pygame.transform.rotate(p_weapon, 90), (p_x - 12, p_y + 16))
			pygame.time.delay(70)
			if f3[int((p_y + 16)/16)][int((p_x-16)/16)] == "h":
				f3_p_count += 1
			if f3[int((p_y + 16)/16)][int((p_x-16)/16)] == "e" and int((p_y + 16)/16) == 7:
				f3_slime_cycles[5] -= 1
			if f3[int((p_y + 16)/16)][int((p_x-16)/16)] == "e" and int((p_y + 16)/16) == 8:
				f3_slime_cycles[6] -= 1
			pygame.display.update()

		if p_left:
			win.blit(p_sprite_left[p_cycle_count], (p_x, p_y))
		elif p_right:
			win.blit(p_sprite_right[p_cycle_count], (p_x, p_y))
		elif p_up:
			win.blit(p_sprite_up[p_cycle_count], (p_x, p_y))
		elif p_down:
			win.blit(p_sprite_down[p_cycle_count], (p_x, p_y))
		else:
			win.blit(p_sprite_idle[p_cycle_count], (p_x, p_y))

		for i in range(0, 10):
			for j in range(0, 15):
				if f3[i][j] == "*":
					if p_x == j*16 and p_y + 16 == i*16:
						p_stars[1] = 1
						star_check = True
					if star_check == False:
						win.blit(star_spr[star_cycle], (6*16,1*16))
						if star_cycle < 2:
							star_cycle += 1
						else:
							star_cycle = 0
				if f3[i][j] == "E" and p_x == j*16 and p_y + 16 == i*16:
					p_floor = 4
					p_x = 16
					p_y = 0
				if (f3[i][j] == "X" or f3[i][j] == "h" or f3[i][j] == "e") and p_x == j*16 and p_y + 16 == i*16:
					win.blit(pygame.image.load("sprites/knight_m_death.png"), (p_x, p_y))
					pygame.display.update()
					pygame.time.delay(500)
					p_x = 16
					p_y = 0	
				if f3[i][j] == "e":
					win.blit(slime_sprite[0], (j*16, i*16))

				
	elif p_floor == 4:
		win.blit(win_screen, (0,0))

	if p_floor != 0:
		win.blit(star_numbers[0], (0*16,9*16))
		c = 1
		for i in range(0,5):
			if p_stars[i] == 1:
				c += 1
		win.blit(star_numbers[c], (1*16,9*16))

	pygame.display.update()

run = True
while (run):
	pygame.time.delay(110)
	keys = pygame.key.get_pressed()
	if p_floor == 0:
		curr_floor = f0
	elif p_floor == 1:
		curr_floor = f1
	elif p_floor == 2:
		curr_floor = f2
	elif p_floor == 3:
		curr_floor = f3

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	if p_floor == 0:
		if f0_cs_state == False:
			if keys[pygame.K_w]:
				if f0_cursor == 1:
					f0_cursor = 0
			elif keys[pygame.K_s]:
				if f0_cursor == 0:
					f0_cursor = 1
			elif keys[pygame.K_RETURN]:
				if f0_cursor == 0:
					f0_cs_state = True
				else:
					break
			# stage select
			elif keys[pygame.K_1]:
				p_floor = 1
			elif keys[pygame.K_2]:
				p_floor = 2
			elif keys[pygame.K_3]:
				p_floor = 3
		else:
			if keys[pygame.K_a]:
				if f0_cursor == 1:
					f0_cursor = 0
				elif f0_cursor == 2:
					f0_cursor = 1
			elif keys[pygame.K_d]:
				if f0_cursor == 0:
					f0_cursor = 1
				elif f0_cursor == 1:
					f0_cursor = 2
			elif keys[pygame.K_RETURN]:
				if f0_cursor == 0:
					p_char = 0
				elif f0_cursor == 1:
					p_char = 1
				else:
					p_char = 2
				assign_p_sprite(p_char)
				p_floor = 1

	elif p_floor == 1 or p_floor == 2 or p_floor == 3:
		
		if keys[pygame.K_ESCAPE]:
			p_floor = 0
			f0_cs_state = False

		elif keys[pygame.K_a] and curr_floor[int((p_y + 16)/16)][int((p_x-16)/16)] != "W": # left
			p_x -= p_vel
			p_atk = "none"
			if p_left and p_cycle_count < 3:
				p_cycle_count += 1
			elif p_left and p_cycle_count == 3:
				p_cycle_count = 0
			else:
				p_cycle_count = 0
			p_left = True
			p_right = False
			p_down = False
			p_up = False

		elif keys[pygame.K_d] and curr_floor[int((p_y + 16)/16)][int((p_x+16)/16)] != "W": # right
			p_x += p_vel
			p_atk = "none"
			if p_right and p_cycle_count < 3:
				p_cycle_count += 1
			elif p_right and p_cycle_count == 3:
				p_cycle_count = 0
			else:
				p_cycle_count = 0
			p_left = False
			p_right = True
			p_down = False
			p_up = False

		elif keys[pygame.K_w] and curr_floor[int((p_y)/16)][int(p_x/16)] != "W": # up
			p_y -= p_vel
			p_atk = "none"
			if p_up and p_cycle_count < 3:
				p_cycle_count += 1
			elif p_up and p_cycle_count == 3:
				p_cycle_count = 0
			else:
				p_cycle_count = 0
			p_left = False
			p_right = False
			p_down = False
			p_up = True

		elif keys[pygame.K_s] and curr_floor[int((p_y + 32)/16)][int(p_x/16)] != "W": # down
			p_y += p_vel
			p_atk = "none"
			if p_down and p_cycle_count < 3:
				p_cycle_count += 1
			elif p_down and p_cycle_count == 3:
				p_cycle_count = 0
			else:
				p_cycle_count = 0
			p_left = False
			p_right = False
			p_down = True
			p_up = False

		else:
			p_left = False
			p_right = False
			p_up = False
			p_down = False
			p_atk = "none"

			if not p_left and not p_right and not p_up and not p_down and p_cycle_count < 3: 
				p_cycle_count += 1
			else:
				p_cycle_count = 0

		if p_weapon_state == True and p_cycle_count:
			if keys[pygame.K_i] and p_atk == "none":
				p_atk = "up"
			elif keys[pygame.K_l] and p_atk == "none":
				p_atk = "right"
			elif keys[pygame.K_k] and p_atk == "none":
				p_atk = "down"
			elif keys[pygame.K_j] and p_atk == "none":
				p_atk = "left"
	

	draw_frame()

pygame.quit()