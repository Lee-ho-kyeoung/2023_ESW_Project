from PIL import Image
import numpy as np

class Enemy:
    def __init__(self, spawn_position, image_path):
        self.image = Image.open(image_path) # 적 이미지

        self.state = 'alive' # 적 상태
        self.position = np.array([spawn_position[0], spawn_position[1], spawn_position[0], spawn_position[1]]) # 적 위치 초기화

    def draw(self, background_image):
        # 배경 이미지에 총알 이미지 그리기
        background_image.paste(self.image, (self.position[0], self.position[1]), self.image)