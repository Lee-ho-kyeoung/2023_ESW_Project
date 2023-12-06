from PIL import Image
import numpy as np
import math

class Arm:
    def __init__(self, image_path):
        self.image = Image.open(image_path)  # 팔 이미지

        self.position = np.array([-16, 171]) # 팔의 위치 (59x59 이미지)
        self.angle = 0                       # 팔의 초기 각도
        self.rotated_arm = self.rotate_arm() # 초기 회전된 이미지 생성
        self.radius = 20                     # 반지름 (팔과 총구의 거리가 20)
        self.center = (self.position[0] + 29, self.position[1] + 29)  # 원의 중심
        self.shootPoint_Position = (self.center[0] + self.radius, self.center[1]) # 총구 위치

    def draw(self, background_image): # 배경 이미지에 회전된 이미지 그리기
        # 새로운 회전된 이미지 생성 (팔이 변경되었을 때만)
        new_rotated_arm = self.rotate_arm()
        if new_rotated_arm:
            self.rotated_arm = new_rotated_arm # 회전된 팔의 이미지로 갱신
        
        background_image.paste(self.rotated_arm, (self.position[0], self.position[1]), self.rotated_arm)

    def rotate_arm(self):
        # 팔 이미지 회전 및 위치 조정
        rotated_arm = self.image.rotate(self.angle, expand=False, center=(29, 29)) # 팔의 이미지를 회전
        return rotated_arm

    def aim(self, angle):
        self.angle = angle # 팔의 각도 조정

        # 각도에 따른 총구의 위치를 계산 (원 위를 따라 이동)
        angle_rad = math.radians(self.angle) # 라디안으로 변경
        x = self.center[0] + self.radius * math.cos(angle_rad)
        y = self.center[1] - self.radius * math.sin(angle_rad)

        self.shootPoint_Position = (round(x), round(y)) # 총구의 위치 갱신