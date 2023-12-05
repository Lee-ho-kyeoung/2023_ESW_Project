from PIL import Image, ImageDraw
from Joystick import Joystick
from Arm import Arm
from Bullet import Bullet
from Wall import Wall

def main():
    joystick = Joystick()
    backGround_image = Image.open("2023_ESW_Project/image/Stage1.png")  # 게임 배경 이미지
    joystick.disp.image(backGround_image)

    walls = [Wall((0,244), (239, 239), 240, 16), Wall((196, 135), (239, 150), 44, 16)]

    arm_image_path = "2023_ESW_Project/image/Arm.png"  # 총 이미지의 파일 경로
    arm = Arm(arm_image_path)         # Gun 객체 생성

    bullet = None  # 초기에는 총알이 없음을 나타내는 변수

    initial_bullet_count = 5           # 초기 총알 개수 설정
    score = 10                         # 점수 초기화

    while True:
        command = {'up_pressed': False , 'down_pressed': False}
        
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            if arm.angle < 90:           # 90도가 최대
                arm.aim(arm.angle + 5)   # 5도씩 증가시킴

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            if arm.angle > -90:          # -90도가 최대
                arm.aim(arm.angle - 5)   # 5도씩 감소시킴
        
        if not joystick.button_A.value:  # A pressed
            if initial_bullet_count < 0:
                break

            if bullet is None:  # 발사된 총알이 없을 때만 발사 가능
                bullet = Bullet("2023_ESW_Project/image/Bullet.png")  
                bullet.shoot(arm)
                initial_bullet_count -= 1  # 총알이 발사될 때마다 초기 총알 개수 감소
                score -= 1  # 총알이 발사될 때마다 점수 감소

        new_backGround_image = backGround_image.copy()

        arm.draw(new_backGround_image, (-16, 171))  # 팔을 항상 그림

        if bullet is not None:
            bullet.update_bullet(new_backGround_image)
            """
            for wall in walls:
                if wall.check_collision(bullet):  # 벽과 충돌 확인
                    bullet.lifespan -= 1
            """
            if not bullet.active:  # 총알이 없어지면 다음 발사를 위해 변수 초기화
                bullet = None

        # 화면의 일부분만 업데이트
        joystick.disp.image(new_backGround_image) 
        
    # 점수 표시 (예: 콘솔에 출력)
    print("Score:", score)

if __name__ == '__main__':
    main()
