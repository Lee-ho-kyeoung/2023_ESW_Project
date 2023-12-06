from PIL import Image, ImageDraw
from Joystick import Joystick
from Arm import Arm
from Bullet import Bullet
from Wall import Wall
from Enemy import Enemy
import time

def stage3():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height)) # 도화지
    text_color = (255, 255, 255)  # 텍스트 색상 설정
    draw = ImageDraw.Draw(my_image)

    backGround_image = Image.open("2023_ESW_Project/image/Stage3.png") # 게임 배경 이미지
    joystick.disp.image(backGround_image) # 게임 배경 이미지를 띄움

    walls = []
    walls.append(Wall((0,224), (240, 240)))    # 땅
    walls.append(Wall((0, 135), (81, 150)))    # 좌측 떠있는 가로 벽
    walls.append(Wall((172, 135), (245, 150))) # 우측 떠있는 가로 벽
    walls.append(Wall((172, 169), (188, 208))) # 우측 떠있는 세로 벽
    walls.append(Wall((0, 0), (240, 240)))     # 화면 밖

    enemy_image_path = "2023_ESW_Project/image/Enemy.png"
    enemys_list = []
    enemys_list.append(Enemy((16, 76), enemy_image_path))
    enemys_list.append(Enemy((197, 165), enemy_image_path))

    arm_image_path = "2023_ESW_Project/image/Arm.png"  # 총 이미지의 파일 경로
    arm = Arm(arm_image_path) # 팔 생성

    bullet = None    # 초기에는 총알이 없음을 나타내는 변수

    bullet_count = 5 # 초기 총알 개수 설정
    stage3_score = 0 # 점수 초기화

    while True:
        command = {'up_pressed': False , 'down_pressed': False}
                
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            if arm.angle < 90:           # 90도가 최대
                arm.aim(arm.angle + 2)   # 3도씩 증가시킴

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            if arm.angle > -90:          # -90도가 최대
                arm.aim(arm.angle - 2)   # 3도씩 감소시킴
                
        if not joystick.button_A.value:  # A pressed
            if bullet is None:           # 발사된 총알이 없을 때만 발사 가능
                bullet = Bullet("2023_ESW_Project/image/Bullet.png")  
                bullet.shoot(arm)        # 총알 발사
                bullet_count -= 1        # 총알이 발사될 때마다 초기 총알 개수 감소

        if bullet is None:               # 발사된 총알이 없을 때만 발사 가능
            if bullet_count == 0:        # 총알 다쏘면끝
                return 0                 # 0 반환

        new_backGround_image = backGround_image.copy() # 현재 이미지 넣기

        arm.draw(new_backGround_image)   # 팔을 항상 그림

        if bullet is not None:           # 총알이 발사되고 있으면
            for wall in walls:
                if wall.check_collision(bullet):  # 벽과 충돌 확인
                    bullet.lifespan -= 1          # 총알 수명 1감소

            bullet.enemy_collision_check(enemys_list)  # 벽과의 충돌 체크
            bullet.update_bullet(new_backGround_image) # 총알 상태 업데이트
                    
            if not bullet.active:   # 총알이 없어지면 다음 발사를 위해 변수 초기화
                bullet = None       # 총알이 발사되고 있지 않으면
                if not enemys_list: # 적이 모두 죽었으면 
                    for i in range(bullet_count):
                        stage3_score += 1500 # 남은 총알당 1,500점 추가

                    draw.rectangle((0, 0, 240, 240), fill = '#000000') # 이미지 초기화
                    draw.text((73, 115), "Stage3 Score: " + str(stage3_score), fill=text_color) # 스테이지1 점수 출력
                    joystick.disp.image(my_image)  # 디스플레이에 이미지 업데이트
                    time.sleep(3) # 3초의 딜레이
                    return stage3_score # 스테이지1의 점수 반환

        for enemy in enemys_list:
            if enemy.state != 'die':             # 적이 죽지 않은 상태이면
                enemy.draw(new_backGround_image) # 적을 그림
            else:                                # 적이 죽은 상태이면
                stage3_score += 1000             # 1,000점 추가
                enemys_list.remove(enemy)        # 적을 리스트에서 삭제
        
        bullet_Count_Draw = ImageDraw.Draw(new_backGround_image) # 남은 총알 그리는 도구
        bullet_Count_Draw.text((180, 5), "Bullet: " + str(bullet_count), fill=text_color) # 남은 총알 화면 상단에 출력

        joystick.disp.image(new_backGround_image)  # 화면의 일부분만 업데이트