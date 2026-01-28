import pygame
from buttons_class import Button
from pills_class import Pill

pygame.init()

#const
WHITE = (255,255,255)
AUTOCLICK_EVENT = pygame.USEREVENT + 1
WIDTH,HEIGHT = 960,540
WINDOW = pygame.display.set_mode([WIDTH,HEIGHT])
FONT = pygame.font.SysFont("Comic sans", 25)
running = True

#var
score = 0
clicks = 1
base_cost = 50
upg_cost = base_cost
upg_cnt = 0
upg_mult = 1.15
adict_click = 0
adict_base = 500
adict_cost = adict_base
adict_cnt = 0
od_base = 1000000
od_cost = od_base
buttons = [
    Button(600, 50, 200, 60, f"potency ({upg_cost})", (0,0,255), (0,255,0)),
    Button(600, 130, 200, 60, f"adiction ({adict_cost})", (0,0,255), (0,255,0)),
    Button(600, 210, 200, 60, f"Overdose? ({od_cost})", (0,0,255), (0,255,0))
    
]
pille = Pill(150,200)

pygame.time.set_timer(AUTOCLICK_EVENT, 1000)

#loop
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == AUTOCLICK_EVENT:
            score += (adict_click * 1)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pille.rect.collidepoint(event.pos):
                score += clicks

            
            for btn in buttons:
                if btn._rect.collidepoint(event.pos):
                    if "potency" in btn._text and score >= upg_cost:
                        score -= upg_cost
                        clicks += 1
                        upg_cnt += 1
                        upg_cost = round(base_cost * (upg_mult**upg_cnt))
                        btn._text = f"potency +1 ({upg_cost})"
                    elif "adiction" in btn._text and score >= adict_cost:
                        score -= adict_cost
                        adict_click += clicks
                        adict_cnt += 1
                        adict_cost = round(adict_base * (upg_mult**adict_cnt))
                        btn._text = f"addiction +1 ({adict_cost})"
                    
        
        
        
    
               
    WINDOW.fill(WHITE)
    
    pille.draw_pill(WINDOW)
    
    for btn in buttons: 
        btn.draw(WINDOW)
        
    score_txt = FONT.render(f"Pills: {score}", True, (0, 0, 0))
    power_txt = FONT.render(f"Per Click: {clicks}", True, (0, 0, 0))
    WINDOW.blit(score_txt, (20, 20))
    WINDOW.blit(power_txt, (20, 50))
    
    
            
    pygame.display.update()
pygame.quit()