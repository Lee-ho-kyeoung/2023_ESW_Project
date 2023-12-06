from PIL import Image
import math

class Bullet:
    def __init__(self, image_path):
        self.image = Image.open(image_path) # 총알 이미지

        self.angle = 0         # 총알의 초기 각도
        self.speed = 10        # 총알의 이동 속도
        self.lifespan = 5      # 총알의 수명
        self.position = (0, 0) # 총알의 초기 위치 총알 중심 (1,1)
        self.active = True     # 총알이 활성화되었는지 여부

    def draw(self, background_image, position): # 배경 이미지에 총알 이미지 그리기
        background_image.paste(self.image, (position[0] - 1, position[1] - 1), self. image)

    def move(self): # 총알을 이동시키는 동작
        angle_rad = math.radians(self.angle) # 라디안으로 변경
        delta_x = self.speed * math.cos(angle_rad) # x좌표 변화량
        delta_y = self.speed * math.sin(angle_rad) # y좌표 변화량
        
        # 현재 위치에 변화량을 더하여 새로운 위치 계산
        new_x = self.position[0] + delta_x  # 다음 x좌표
        new_y = self.position[1] - delta_y  # 다음 y좌표 (y 값은 반대로 해야함)

        self.position = (int(new_x), int(new_y))  # 새로운 위치로 갱신

    def shoot(self, arm):      # 총알을 발사
        self.angle = arm.angle # 총의 각도를 총알의 각도로 설정
        self.position = arm.shootPoint_Position + (0, -3) # 총구 위치로 설정
        self.active = True     # 총알 활성화

    def update_bullet(self, backGround_image):
        if self.active:              # 총알 상태
            if self.lifespan <= 0:   # 총알 수명이 0보다 작으면
                self.active = False  # 총알 비활성화
            else:                    # 총알 수명이 0이 아니면
                self.move()          # 총알을 이동시킴
                self.draw(backGround_image, self.position) # 새로운 위치에 총알 그림
            
    def enemy_collision_check(self, enemys):
        for enemy in enemys:
            bullet_position = (self.position[0], self.position[1], self.position[0] + 1, self.position[1]) # 총알 판정 범위
            enemy_position = (enemy.position[0], enemy.position[1], enemy.position[0] + 31, enemy.position[1] + 59) # 적 판정 범위

            collision = self.overlap(bullet_position, enemy_position) # 충돌 확인
            
            if collision: # 총알과 충돌시 적을 죽은 상태로 변경
                enemy.state = 'die'

    def overlap(self, ego_position, other_position):
        return ego_position[0] > other_position[0] and ego_position[1] > other_position[1] \
                and ego_position[2] < other_position[2] and ego_position[3] < other_position[3] # 겹치면 True, 안겹치면 False