from PIL import Image, ImageDraw
from Joystick import Joystick
from Gun import Gun

def main():
    joystick = Joystick()
    backGround_image = Image.open("2023_ESW_Project/image/Stage1.png")  # 게임 배경 이미지
    joystick.disp.image(backGround_image)

    gun_image_path = "2023_ESW_Project/image/Gun.png"  # 총 이미지의 파일 경로
    gun = Gun(gun_image_path)  # Gun 객체 생성

    while True:
        command = {'up_pressed': False , 'down_pressed': False}
        
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            if gun.angle < 90:
                gun.aim(gun.angle + 5)  # 예시로 5도씩 증가시킴

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            if gun.angle > -90:
                gun.aim(gun.angle - 5)  # 예시로 5도씩 감소시킴

        new_backGround_image = backGround_image.copy()
        gun.draw(new_backGround_image, (-16, 171))  # 몸 중앙 13, 200 / 팔 중심 축 2,14

        # 화면의 일부분만 업데이트
        joystick.disp.image(new_backGround_image) 
        
if __name__ == '__main__':
    main()