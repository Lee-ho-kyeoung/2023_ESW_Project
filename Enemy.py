from PIL import Image
import numpy as np

class Enemy:
    def __init__(self, spawn_position, image_path):
        self.image_path = image_path
        self.image = Image.open(self.image_path)

        self.state = 'alive'
        self.position = np.array([spawn_position[0] - 25, spawn_position[1] - 25, spawn_position[0] + 25, spawn_position[1] + 25])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])

    def draw(self, background_image):
        # 배경 이미지에 총알 이미지 그리기
        background_image.paste(self.image, (self.position[0], self.position[1]), self.image)