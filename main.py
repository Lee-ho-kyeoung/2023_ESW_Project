from PIL import Image, ImageDraw
from Joystick import Joystick
import time
from stage1 import stage1
from stage2 import stage2

def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height)) # 도화지!
    text_color = (255, 255, 255)  # 텍스트 색상 설정
    text_position = (93, 115)    # 텍스트 위치 설정
    draw = ImageDraw.Draw(my_image)

    sequence = 1 # 게임 순서

    total_score = 0 # 총점 초기화

    while True: 
        if(sequence == 0): # 게임 오버
            draw.rectangle((0, 0, 240, 240), fill = '#000000')
            draw.text(text_position, "Game Over", fill=text_color)
            joystick.disp.image(my_image)  # 디스플레이에 이미지 업데이트

        if(sequence == 1): # 게임 시작
            draw.text(text_position, "Game Start", fill=text_color)
            joystick.disp.image(my_image)  # 디스플레이에 이미지 업데이트
            time.sleep(3)
            sequence += 1

        elif(sequence == 2): # Stage1
            total_score += stage1()

            if(total_score == 0):
                sequence = 0
            sequence = 3

        elif(sequence == 3): # Stage2
            total_score += stage2()

            if(total_score == 0):
                sequence = 0
            sequence += 1

        elif(sequence == 4): # 게임 클리어
            draw.rectangle((0, 0, 240, 240), fill = '#000000')
            draw.text(text_position, "Game Clear", fill=text_color)
            draw.text((73, 125), "Total Score: " + str(total_score), fill=text_color) # 총점 출력
            joystick.disp.image(my_image)  # 디스플레이에 이미지 업데이트
            return

if __name__ == '__main__':
    main()