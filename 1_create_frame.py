import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))# 화면 크기 설정


#화면 타이틀
pygame.display.set_caption('han game') #게임 이름


#이벤트 루프
running = True# 게임 진행중 확인
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


#게임 종료시 pygame종료
pygame.quit()