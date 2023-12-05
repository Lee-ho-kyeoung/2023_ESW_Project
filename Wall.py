import math

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

class Wall:
    def __init__(self, leftUp, rightDown, width, height):
        self.leftUp = leftUp  # 왼쪽 상단 좌표
        self.rightDown = rightDown  # 오른쪽 하단 좌표
        self.width = width  # 벽의 너비
        self.height = height  # 벽의 높이

    def check_collision(self, bullet):
        bullet_x, bullet_y = bullet.position  # 총알의 현재 위치 가져오기
        bullet_speed = bullet.speed  # 총알의 속도 가져오기
        bullet_angle = bullet.angle  # 총알의 각도 가져오기

        # 총알의 다음 위치 계산
        angle_rad = math.radians(bullet_angle)
        delta_x = bullet_speed * math.cos(angle_rad)
        delta_y = bullet_speed * math.sin(angle_rad)
        next_bullet_x = bullet_x + delta_x
        next_bullet_y = bullet_y - delta_y  # y 값은 반대로 해야 합니다.

        # 벽의 좌표를 가져옵니다.
        wall_left, wall_top = self.leftUp
        wall_right, wall_bottom = self.rightDown

        # 총알의 직선과 벽의 변들을 계산합니다.
        bullet_line = Line(bullet_x, bullet_y, next_bullet_x, next_bullet_y)
        wall_lines = [
            Line(wall_left, wall_top, wall_right, wall_top),  # 상단 변
            Line(wall_right, wall_top, wall_right, wall_bottom),  # 우측 변
            Line(wall_left, wall_bottom, wall_right, wall_bottom),  # 하단 변
            Line(wall_left, wall_top, wall_left, wall_bottom)  # 좌측 변
        ]

        intersection_points = []  # 겹치는 지점들을 저장할 리스트

        for line in wall_lines:
            intersection_point = bullet_line.intersect(line)
            if intersection_point:  # 겹치는 지점이 존재하는 경우
                intersection_points.append(intersection_point)  # 겹치는 지점을 추가합니다.
        
        if intersection_points:
            closest_point = min(intersection_points, key=lambda p: distance(p, bullet.position))  # 가장 가까운 지점을 찾습니다.
            if closest_point.x == bullet.position.x:  # 가장 가까운 지점이 세로 선인 경우
                print("양옆 충돌")
                bullet.angle = 180 - bullet_angle  # 총알의 이동 방향을 반대로 설정합니다.
            elif closest_point.y == bullet.position.y:  # 가장 가까운 지점이 가로 선인 경우
                print("위 아래 충돌")
                bullet.angle = -bullet_angle  # 총알의 이동 방향을 반대로 설정합니다.

                return True  # 충돌 발생

        return False  # 충돌 없음
    
"""
        # 충돌 판정을 위해 총알의 직선과 벽의 변들을 비교합니다.
        for line in wall_lines:
            intersection_point = bullet_line.intersect(line)
            if intersection_point: # 겹치는 지점
                # 첫 번째로 겹치는 변이 세로 변인지 가로 변인지 판정합니다.
                if line.is_vertical():
                    # 세로 변과 충돌한 경우 양옆 충돌 판정을 수행합니다.
                    print("양옆 충돌")
                    bullet.angle = 180 - bullet_angle  # 총알의 이동 방향을 반대로 설정합니다.
                if line.is_horizontal():
                    # 가로 변과 충돌한 경우 위아래 충돌 판정을 수행합니다.
                    print("위 아래 충돌")
                    bullet.angle = -bullet_angle  # 총알의 이동 방향을 반대로 설정합니다.
                
                return True  # 충돌 발생

        return False  # 충돌 없음
"""

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def is_vertical(self):
        return self.x1 == self.x2

    def is_horizontal(self):
        return self.y1 == self.y2

    def intersect(self, other_line):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
        x3, y3, x4, y4 = other_line.x1, other_line.y1, other_line.x2, other_line.y2

        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denominator == 0:
            return None

        x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
        y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator

        if x < min(x1, x2) or x > max(x1, x2) or x < min(x3, x4) or x > max(x3, x4):
            return None

        return x, y
