import math

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

class Wall:
    def __init__(self, leftUp, rightDown):
        self.leftUp = leftUp  # 왼쪽 상단 좌표
        self.rightDown = rightDown  # 오른쪽 하단 좌표

    def check_collision(self, bullet):
        bullet_x = bullet.position[0]
        bullet_y = bullet.position[1]  # 총알의 현재 위치 가져오기
        bullet_speed = bullet.speed    # 총알의 속도 가져오기
        bullet_angle = bullet.angle    # 총알의 각도 가져오기

        # 총알의 다음 위치 계산
        angle_rad = math.radians(bullet_angle)
        delta_x = bullet_speed * math.cos(angle_rad)
        delta_y = bullet_speed * math.sin(angle_rad)
        next_bullet_x = bullet_x + delta_x
        next_bullet_y = bullet_y - delta_y  # y 값은 반대로 해야 합니다.

        points = [] # 전 과 후를 잇는 선 위에 있는 점들의 모임

        # x 편차가 y 편차보다 크다면
        if abs(next_bullet_y - bullet_y) < abs(next_bullet_x - bullet_x):
            y_plus = (next_bullet_y - bullet_y) / abs(next_bullet_x - bullet_x)
            y_point = bullet_y # x좌표를 기준으로 할 것이기 때문에, y점은 실수 값이 나옴
            for x_point in range(min(int(bullet_x), int(next_bullet_x)), max(int(bullet_x), int(next_bullet_x)) + 1):
                points.append((x_point, int(y_point)))
                y_point += y_plus
        else:
            x_plus = (next_bullet_x - bullet_x) / abs(next_bullet_y - bullet_y)
            x_point = bullet_x # x좌표를 기준으로 할 것이기 때문에, y점은 실수 값이 나옴
            for y_point in range(min(int(bullet_y), int(next_bullet_y)), max(int(bullet_y), int(next_bullet_y)) + 1):
                points.append((int(x_point), y_point))
                x_point += x_plus

        # 벽의 좌표를 가져옵니다.
        wall_left, wall_top = self.leftUp
        wall_right, wall_bottom = self.rightDown

        left_points = []
        right_points = []
        top_points = []
        bottom_points = []

        for side_point in range(wall_top, wall_bottom + 1):
            left_points.append((wall_left, side_point))
            right_points.append((wall_right, side_point))

        for updown_point in range(wall_left, wall_right + 1):
            top_points.append((updown_point, wall_top))
            bottom_points.append((updown_point, wall_bottom))

        for point in points:
            if point in left_points:
                print("양옆 충돌")
                bullet.angle = 180 - bullet_angle  # 총알의 이동 방향을 반대로 설정합니다.
                return True
            if point in right_points:
                print("양옆 충돌")
                bullet.angle = 180 - bullet_angle  # 총알의 이동 방향을 반대로 설정합니다.
                return True
            if point in top_points:
                print("위 아래 충돌")
                bullet.angle = -bullet_angle  # 총알의 이동 방향을 반대로 설정합니다.
                return True
            if point in bottom_points:
                print("위 아래 충돌")
                bullet.angle = -bullet_angle  # 총알의 이동 방향을 반대로 설정합니다.
                return True
            
        return False