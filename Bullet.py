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
        background_image.paste(self.image, (position[0] - 1, position[1] - 1), self. image)

    def move(self):
        # 총알을 이동시키는 동작
        angle_rad = math.radians(self.angle)
        delta_x = self.speed * math.cos(angle_rad)
        delta_y = self.speed * math.sin(angle_rad)
        
        # 현재 위치에 변화량을 더하여 새로운 위치 계산
        new_x = self.position[0] + delta_x
        new_y = self.position[1] - delta_y  # y 값은 반대로 해야 합니다.

        # 새로운 위치로 업데이트
        self.position = (int(new_x), int(new_y))

    def shoot(self, arm):
        self.angle = arm.angle  # 총의 각도를 총알의 각도로 설정
        self.position = arm.shootPoint_Position + (0, -3) # 총구 위치로 설정
        self.active = True  # 총알 활성화

    def update_bullet(self, backGround_image):
        if self.active:
            if self.lifespan <= 0:
                self.active = False  # 총알 수명이 다하면 비활성화
            else:
                self.move()  # 총알을 이동시킴
                self.draw(backGround_image, self.position)  # 새로운 위치에 총알 그림
            
    def enemy_collision_check(self, enemys):
        for enemy in enemys:

            # (x1, y1, x2, y2) 형식의 튜플로 변환하여 충돌을 확인합니다
            bullet_position = (
                self.position[0],
                self.position[1],
                self.position[0] + 3,  # 예상 총알 너비 추가
                self.position[1] + 3,  # 예상 총알 높이 추가
            )
            enemy_position = (
                enemy.position[0],
                enemy.position[1],
                enemy.position[0] + 31,  # 예상 적 너비 추가
                enemy.position[1] + 59,  # 예상 적 높이 추가
            )

            collision = self.overlap(bullet_position, enemy_position)
            
            if collision:
                enemy.state = 'die'

    def overlap(self, ego_position, other_position):
        '''
        두개의 사각형(bullet position, enemy position)이 겹치는지 확인하는 함수
        좌표 표현 : [x1, y1, x2, y2]
            
        return :
            True : if overlap
            False : if not overlap
        '''
        return ego_position[0] > other_position[0] and ego_position[1] > other_position[1] \
                and ego_position[2] < other_position[2] and ego_position[3] < other_position[3]