from PIL import Image

class Gun:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(self.image_path)

        self.angle = 0  # 총의 초기 각도

    def draw(self, background_image, position):
        # 배경 이미지에 총 이미지 그리기
        background_image.paste(self.rotate_arm(), position, self.rotate_arm())

    def rotate_arm(self):
        # 팔 이미지 회전 및 위치 조정
        rotated_arm = self.image.rotate(self.angle, expand=False, center=(29,29))
        return rotated_arm
        
    def aim(self, angle):
        # 총을 조준하는 동작
        self.angle = angle
    
    def fire(self):
        # 총을 발사하는 동작
        pass

    