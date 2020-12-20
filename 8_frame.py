import pygame
###################
#기본 초기화 부분(반드시 해야 하는 것들)
pygame.init() #초기화

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))# 화면 크기 설정


#화면 타이틀
pygame.display.set_caption('han game') #게임 이름

#fps
clock = pygame.time.Clock()


#########################################

#1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 폰트 등)

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/HanPC/Desktop/python workspace/pythonGame/background.png")

#이벤트 루프
running = True# 게임 진행중 확인
while running:
    dt = clock.tick(60)# 게임 화면의 초당 프레임수 설정


    #2. 이벤트 처리(키보드, 마우스 등)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #3. 게임 캐릭터 위치 정의

    #4. 충돌 처리

    #5. 화면에 그리기


    pygame.display.update()#게임화면을 다시 그리기 (필수)

#게임 종료시 pygame종료(ms)
pygame.quit()