class Bullet:
    def __init__(self, x, y, angle):
        self.x = x  # 총알의 초기 x 좌표
        self.y = y  # 총알의 초기 y 좌표
        self.angle = angle  # 총알의 발사 각도
        self.speed = 10  # 총알의 초기 속도
        
    def update(self):
        # 총알의 움직임 업데이트
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))
    
    def collide_with_wall(self, wall):
        # 벽과 충돌처리
        pass
    
    def collide_with_enemy(self, enemy):
        # 적과 충돌처리
        pass