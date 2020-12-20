import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))# 화면 크기 설정


#화면 타이틀
pygame.display.set_caption('han game') #게임 이름

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/HanPC/Desktop/python workspace/pythonGame/background.png")


#이벤트 루프
running = True# 게임 진행중 확인
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #screen.fill((0, 0, 255)) #단색으로 색 채우기
    screen.blit(background, (0,0)) #배경 그리기

    pygame.display.update()#게임화면을 다시 그리기 (필수)


#게임 종료시 pygame종료
pygame.quit()