import math

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2) # 두 점 사이의 거리 반환

class Wall:
    def __init__(self, leftUp, rightDown):
        self.leftUp = leftUp           # 왼쪽 상단 좌표
        self.rightDown = rightDown     # 오른쪽 하단 좌표

    def check_collision(self, bullet):
        bullet_x = bullet.position[0]
        bullet_y = bullet.position[1]  # 총알의 현재 위치 가져오기
        bullet_speed = bullet.speed    # 총알의 속도 가져오기
        bullet_angle = bullet.angle    # 총알의 각도 가져오기

        # 총알의 다음 위치 계산
        angle_rad = math.radians(bullet_angle)
        delta_x = bullet_speed * math.cos(angle_rad)
        delta_y = bullet_speed * math.sin(angle_rad)
        next_bullet_x = bullet_x + delta_x  # 다음 x 좌표
        next_bullet_y = bullet_y - delta_y  # 다음 y 좌표

        points = [] # 전 과 후를 잇는 선 위에 있는 점들의 모임

        if abs(next_bullet_y - bullet_y) < abs(next_bullet_x - bullet_x):       # x 편차가 y 편차보다 크다면
            y_plus = (next_bullet_y - bullet_y) / abs(next_bullet_x - bullet_x) # y 증가량을 x 증가량으로 나눔
            y_point = bullet_y # x좌표를 기준으로 할 것이기 때문에, y점은 실수 값이 나옴

            for x_point in range(min(int(bullet_x), int(next_bullet_x)), max(int(bullet_x), int(next_bullet_x)) + 1):
                points.append((x_point, int(y_point)))
                y_point += y_plus
        else:   # x 편차가 y 편차보다 작다면
            x_plus = (next_bullet_x - bullet_x) / abs(next_bullet_y - bullet_y) # x 증가량을 y 증가량으로 나눔
            x_point = bullet_x # x좌표를 기준으로 할 것이기 때문에, y점은 실수 값이 나옴

            for y_point in range(min(int(bullet_y), int(next_bullet_y)), max(int(bullet_y), int(next_bullet_y)) + 1):
                points.append((int(x_point), y_point))
                x_point += x_plus

        # 벽의 좌표
        wall_left, wall_top = self.leftUp
        wall_right, wall_bottom = self.rightDown

        left_points = []   # 벽의 왼쪽 변의 점들의 모음
        right_points = []  # 벽의 오른쪽 변의 점들의 모음
        top_points = []    # 벽의 위쪽 변의 점들의 모음
        bottom_points = [] # 벽의 아래쪽 변의 점들의 모음

        # 점을 추가
        for side_point in range(wall_top, wall_bottom + 1):
            left_points.append((wall_left, side_point)) # 왼쪽 벽면의 점들을 찍어줌
            right_points.append((wall_right, side_point)) # 오른쪽 벽면의 점들을 찍어줌

        for updown_point in range(wall_left, wall_right + 1):
            top_points.append((updown_point, wall_top))         # 윗쪽 벽면의 점들을 찍어줌
            bottom_points.append((updown_point, wall_bottom))   # 아랫쪽 벽면의 점들을 찍어줌

        for point in points:         # 총알의 예상 이동경로의 모든 점에 대해서
            if point in left_points: # 왼쪽 벽의 점과 이동경로의 점이 겹친다면
                print("왼쪽 벽 충돌")
                bullet.angle = 180 - bullet_angle  # 총알의 이동 방향을 반대로 설정
                return True
            if point in right_points: # 오른쪽 벽의 점과 이동경로의 점이 겹친다면
                print("오른쪽 벽 충돌")  
                bullet.angle = 180 - bullet_angle  # 총알의 이동 방향을 반대로 설정
                return True
            if point in top_points:   # 위쪽 벽의 점과 이동경로의 점이 겹친다면
                print("위쪽 벽 충돌")    
                bullet.angle = -bullet_angle  # 총알의 이동 방향을 반대로 설정합니다.
                return True
            if point in bottom_points: # 아래쪽 벽의 점과 이동경로의 점이 겹친다면
                print("아래쪽 벽 충돌")  
                bullet.angle = -bullet_angle  # 총알의 이동 방향을 반대로 설정
                return True
            
        return False