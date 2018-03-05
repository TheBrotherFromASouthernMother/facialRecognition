import dlib

from PIL import Image
import face_recognition

known_image = face_recognition.load_image_file("./known/me.jpg")
unknown_image = face_recognition.load_image_file("./known/me2.jpg")


christianencoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([christianencoding], unknown_encoding)


print(results)



# face_locations = face_recognition.face_locations(image)
#
# print("I found {} face(s) in this photograph.".format(len(face_locations)))
#
# for face_location in face_locations:
#
#     # Print the location of each face in this image
#     top, right, bottom, left = face_location
#     print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
#
#     # You can access the actual face itself like this:
#     face_image = image[top:bottom, left:right]
#     pil_image = Image.fromarray(face_image)
#     pil_image.show()
