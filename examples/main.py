from PIL import Image, ImageDraw
import face_recognition

class face_detect:
    def __init__(self, face_landmarks_list, image):
        self.face_landmarks_list = face_landmarks_list
        self.image = image

    def active(self, number):
        if number == "1":
            print("Select Draw Line in Image")
            self.draw_line_image()
        elif number == "2":
            print("Select Draw Fun in Image")
            self.draw_fun_image()

    def draw_line_image(self):
        for face_landmarks in self.face_landmarks_list:

            facial_features = [
                'chin',
                'left_eyebrow',
                'right_eyebrow',
                'nose_bridge',
                'nose_tip',
                'left_eye',
                'right_eye',
                'top_lip',
                'bottom_lip'
            ]

            for facial_feature in facial_features:
                print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
            pil_image = Image.fromarray(self.image)
            d = ImageDraw.Draw(pil_image)

            for facial_feature in facial_features:
                d.line(face_landmarks[facial_feature], width=5)
            pil_image.save('sample_image.jpg')
            pil_image.show()

    def draw_fun_image(self):
        for face_landmarks in self.face_landmarks_list:
            pil_image = Image.fromarray(self.image)
            d = ImageDraw.Draw(pil_image, 'RGBA')

            # Make the eyebrows into a nightmare
            d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
            d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
            d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
            d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

            # Gloss the lips
            d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
            d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
            d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
            d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

            # Sparkle the eyes
            d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
            d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

            d.polygon(face_landmarks['chin'], fill=(0, 0, 0, 192))

            # Apply some eyeliner
            d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
            d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

            pil_image.save('sample_image.jpg')
            pil_image.show()

input_image = input()
image = face_recognition.load_image_file(input_image)

face_landmarks_list = face_recognition.face_landmarks(image)

print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

print("Please write number if you want to behave")
print("#if you write 1 : draw line in face_image_file#")
print("#if you write 2 : draw fun image in face_image_file#")
print("#if you write 3 : draw line in face_image_file#")

number = input()
a = face_detect(face_landmarks_list, image)
a.active(number)

print("Save Completed!! named 'sample.jpg'")
    
