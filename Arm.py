from PIL import Image
import numpy as np
import math

class Arm:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(self.image_path)
        self.angle = 0  # 팔의 초기 각도
        self.rotated_arm = self.rotate_arm()  # 초기 회전된 이미지 생성
        self.shootPoint_Position = (28, 195)
        self.center = (8, 195)  # 원의 중심
        self.radius = 20  # 반지름 (지름이 40이므로)

    def draw(self, background_image, position):
        # 새로운 회전된 이미지 생성 (팔이 변경되었을 때만)
        new_rotated_arm = self.rotate_arm()
        if new_rotated_arm:
            self.rotated_arm = new_rotated_arm
        
        # 배경 이미지에 회전된 이미지 그리기
        background_image.paste(self.rotated_arm, position, self.rotated_arm)

    def rotate_arm(self):
        # 팔 이미지 회전 및 위치 조정
        rotated_arm = self.image.rotate(self.angle, expand=False, center=(29, 29))
        return rotated_arm

    def aim(self, angle):
        self.angle = angle # 팔의 각도 조정

        # 각도에 따른 총구의 위치를 계산 (원 위를 따라 이동)
        angle_rad = math.radians(self.angle)
        x = self.center[0] + self.radius * math.cos(angle_rad)
        y = self.center[1] - self.radius * math.sin(angle_rad)

        self.shootPoint_Position = (int(x), int(y)) # 총구의 위치 갱신