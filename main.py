from PIL import Image, ImageDraw
from Joystick import Joystick
import time
from stage1 import stage1
from stage2 import stage2
from Stage3 import stage3

def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height)) # 도화지!
    text_color = (255, 255, 255)  # 텍스트 색상 설정
    draw = ImageDraw.Draw(my_image)

    sequence = 1    # 게임 순서

    total_score = 0 # 총점 초기화

    while True: 
        if(sequence == 0): # 게임 오버
            draw.rectangle((0, 0, 240, 240), fill = '#000000')
            draw.text((93, 115), "Game Over", fill=text_color) # Game over 출력
            joystick.disp.image(my_image)  # 디스플레이에 이미지 업데이트
            return

        if(sequence == 1): # 게임 시작
            draw.text((93, 105), "Gun BBang!", fill=text_color) # Game Start 출력
            draw.text((93, 115), "Game Start", fill=text_color) # Game Start 출력
            joystick.disp.image(my_image)  # 디스플레이에 이미지 업데이트
            time.sleep(3)  # 3초 딜레이
            sequence += 1  # 다음 순서

        elif(sequence == 2): # Stage1
            stage1_score = stage1()
            if(stage1_score == 0): # 반환 점수가 0이면
                sequence = 0       # 게임 오버
            else:
                total_score += stage1_score # 총 점수에 추가
                sequence += 1               # 다음 순서

        elif(sequence == 3): # Stage2
            stage2_score = stage2()
            if(stage2_score == 0): # 반환 점수가 0이면
                sequence = 0       # 게임 오버
            else:
                total_score += stage2_score # 총 점수에 추가
                sequence += 1               # 다음 순서

        elif(sequence == 4): # Stage3
            stage3_score = stage3()
            if(stage3_score == 0): # 반환 점수가 0이면
                sequence = 0       # 게임 오버
            else:
                total_score += stage3_score # 총 점수에 추가
                sequence += 1               # 다음 순서

        elif(sequence == 5): # 게임 클리어
            draw.rectangle((0, 0, 240, 240), fill = '#000000')
            draw.text((93, 115), "Game Clear", fill=text_color) # Game Clear 출력
            draw.text((73, 125), "Total Score: " + str(total_score), fill=text_color) # 총점 출력
            joystick.disp.image(my_image)  # 디스플레이에 이미지 업데이트
            return

if __name__ == '__main__':
    main()