import pygame
from buttons_class import Button
from pills_class import Pill

pygame.init()

pygame.display.set_caption("Storgata simulator")
# const
WHITE = (255, 255, 255)
AUTOCLICK_EVENT = pygame.USEREVENT + 1
WIDTH, HEIGHT = 960, 540
WINDOW = pygame.display.set_mode([WIDTH, HEIGHT])
FONT = pygame.font.SysFont("Comic sans", 25)
running = True

# var
score = 0
click_base = 1
clicks = click_base
base_cost = 50
upg_cost = base_cost
upg_cnt = 0
upg_mult = 1.15
adict_time_base = 5000
adict_time = 0
adict_base = 500
adict_cost = adict_base
adict_pps = 225
adict_pps_max = 500
adict_cnt = 0
od_base = 1000000
od_cost = od_base
od_cnt = 1
buttons = [
    Button(600, 50, 200, 60, f"higher potency ({upg_cost})", (0, 0, 255), (0, 255, 0)),
    Button(
        600, 130, 200, 60, f"unlock adiction ({adict_cost})", (0, 0, 255), (0, 255, 0)
    ),
    Button(600, 210, 200, 60, f"overdose ({od_cost})", (0, 0, 255), (0, 255, 0)),
]
pille = Pill(150, 200)


# loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == AUTOCLICK_EVENT:
            score += clicks * 1
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
                        if "unlock" in btn._text:
                            adict_time = adict_time_base
                            adict_cnt = 0
                            btn._text = f"adiction +1 ({adict_cost}) {adict_cnt}/20"
                        else:
                            if adict_cnt <= 20:
                                score -= adict_cost
                                adict_cnt += 1
                                adict_time = max(
                                    adict_pps_max,
                                    adict_time_base - (adict_cnt * adict_pps),
                                )
                            adict_cost = round(adict_base * (upg_mult**adict_cnt))
                            pygame.time.set_timer(AUTOCLICK_EVENT, adict_time)
                        print(adict_cnt)
                        if adict_cnt == 20:
                            btn._text = f"Maxed Out"
                        else:
                            btn._text = f"adiction +1 ({adict_cost}) {adict_cnt}/20"
                    elif "overdose" in btn._text and score >= od_cost:
                        score, upg_cnt, adict_cnt = 0, 0, 0
                        od_cnt += 1
                        clicks = round(click_base * od_cnt)
                        od_cost = round(od_base * (upg_mult**od_cnt))
                        btn._text = f"overdose + 1 ({od_cost})"
                        print(clicks, od_cnt, click_base)

    WINDOW.fill(WHITE)

    pille.draw_pill(WINDOW)

    if score < od_cost:
        for btn in buttons[0:2]:
            btn.draw(WINDOW)
    else:
        for btn in buttons:
            btn.draw(WINDOW)

    score_txt = FONT.render(f"Pills: {score}", True, (0, 0, 0))
    power_txt = FONT.render(f"Per Click: {clicks}", True, (0, 0, 0))
    adcit_txt = FONT.render(f"adcition: pills per {adict_time}ms", True, (0, 0, 0))
    WINDOW.blit(score_txt, (20, 20))
    WINDOW.blit(power_txt, (20, 50))
    WINDOW.blit(adcit_txt, (20, 80))

    pygame.display.update()
pygame.quit()
