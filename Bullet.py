from PIL import Image
import math

class Bullet:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(self.image_path)

        self.angle = 0  # 총알의 초기 각도
        self.speed = 10  # 총알의 이동 속도
        self.lifespan = 5  # 총알의 수명
        self.position = (0, 0)  # 총알의 초기 위치 총알 중심 (1,1)
        self.active = True  # 총알이 활성화되었는지 여부

    def draw(self, background_image, position):
        # 배경 이미지에 총알 이미지 그리기
        background_image.paste(self.image, position, self.image)

    def move(self):
        # 총알을 이동시키는 동작
        angle_rad = math.radians(self.angle)
        delta_x = self.speed * math.cos(angle_rad)
        delta_y = self.speed * math.sin(angle_rad)
        
        # 현재 위치에 변화량을 더하여 새로운 위치 계산
        new_x = self.position[0] + delta_x
        new_y = self.position[1] - delta_y  # y 값은 반대로 해야 합니다.
        
        # 화면 경계에 도달했는지 확인하여 충돌 처리
        if new_x <= 0 or new_x >= 239:
            self.angle = 180 - self.angle  # 수평 방향 반사 처리
            self.lifespan -= 1
        
        if new_y <= 0 or new_y >= 239:
            self.angle = -self.angle  # 수직 방향 반사 처리
            self.lifespan -= 1

        # 새로운 위치로 업데이트
        self.position = (int(new_x), int(new_y))

    def shoot(self, arm):
        self.angle = arm.angle  # 총의 각도를 총알의 각도로 설정
        self.position = arm.shootPoint_Position # 총구 위치로 설정
        self.active = True  # 총알 활성화

    def update_bullet(self, backGround_image):
        if self.active:
            self.move()  # 총알을 이동시킴
            self.draw(backGround_image, self.position)  # 새로운 위치에 총알 그림
            if self.lifespan <= 0:
                self.active = False  # 총알 수명이 다하면 비활성화