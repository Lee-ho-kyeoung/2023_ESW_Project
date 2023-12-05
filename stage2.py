from PIL import Image, ImageDraw
from Joystick import Joystick
from Arm import Arm
from Bullet import Bullet
from Wall import Wall
from Enemy import Enemy
import time

def stage2():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height)) # 도화지!
    text_color = (255, 255, 255)  # 텍스트 색상 설정
    draw = ImageDraw.Draw(my_image)

    backGround_image = Image.open("2023_ESW_Project/image/Stage2.png")  # 게임 배경 이미지
    joystick.disp.image(backGround_image)

    walls = []
    walls.append(Wall((111,120), (127, 223)))  # 세로 벽
    walls.append(Wall((128, 120), (191, 133))) # 가로 벽
    walls.append(Wall((0,224), (240, 240)))    # 땅
    walls.append(Wall((0, 0), (240, 240)))     # 화면 밖

    enemy_image_path = "2023_ESW_Project/image/Enemy.png"
    enemys_list = []
    enemys_list.append(Enemy((160, 190), enemy_image_path))

    arm_image_path = "2023_ESW_Project/image/Arm.png"  # 총 이미지의 파일 경로
    arm = Arm(arm_image_path) # 팔 생성

    bullet = None  # 초기에는 총알이 없음을 나타내는 변수

    bullet_count = 5           # 초기 총알 개수 설정
    stage2_score = 0                  # 점수 초기화

    while True:
        command = {'up_pressed': False , 'down_pressed': False}
                
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            if arm.angle < 90:           # 90도가 최대
                arm.aim(arm.angle + 3)   # 3도씩 증가시킴

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            if arm.angle > -90:          # -90도가 최대
                arm.aim(arm.angle - 3)   # 3도씩 감소시킴
                
        if not joystick.button_A.value:  # A pressed
            if bullet_count < 0:         # 총알 다쏘면끝
                return 0
                

            if bullet is None:  # 발사된 총알이 없을 때만 발사 가능
                bullet = Bullet("2023_ESW_Project/image/Bullet.png")  
                bullet.shoot(arm)
                bullet_count -= 1  # 총알이 발사될 때마다 초기 총알 개수 감소

        new_backGround_image = backGround_image.copy()

        arm.draw(new_backGround_image)  # 팔을 항상 그림

        if bullet is not None:
            for wall in walls:
                if wall.check_collision(bullet):  # 벽과 충돌 확인
                    bullet.lifespan -= 1

            bullet.enemy_collision_check(enemys_list)
            bullet.update_bullet(new_backGround_image)
                    
            if not bullet.active:  # 총알이 없어지면 다음 발사를 위해 변수 초기화
                bullet = None
                if not enemys_list: 
                    for i in range(bullet_count):
                        stage2_score += 1500
                        
                    print("Stage2 Score:", stage2_score)
                    draw.rectangle((0, 0, 240, 240), fill = '#000000') # 이미지 초기화
                    draw.text((73, 115), "Stage2 Score: " + str(stage2_score), fill=text_color)
                    joystick.disp.image(my_image)  # 디스플레이에 이미지 업데이트
                    time.sleep(3)
                    return stage2_score

        for enemy in enemys_list:
            if enemy.state != 'die':
                enemy.draw(new_backGround_image)
            else:
                stage2_score += 1000
                enemys_list.remove(enemy)

        # 화면의 일부분만 업데이트
        joystick.disp.image(new_backGround_image) 