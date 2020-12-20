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

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/HanPC/Desktop/python workspace/pythonGame/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #가로크기
character_height = character_size[1] # 세로크기
character_x_pos = (screen_width /2) - (character_width /2) #화면 가로의 절반 위치에 해당하는 곳에 위치시킴
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 - 캐릭터 높이


#이동할 좌표
to_x = 0
to_y = 0


#이벤트 루프
running = True# 게임 진행중 확인
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP: #방향키 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y
    
    #가로 경계값 처리
    if character_x_pos <0:
        character_x_pos =0
    elif character_x_pos> screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos <0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0,0)) #배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()#게임화면을 다시 그리기 (필수)


#게임 종료시 pygame종료
pygame.quit()