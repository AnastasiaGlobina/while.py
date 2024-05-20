# class Comment:
#     count = 0
#
#
#
#     def __init__(self, text):
#         self.text = text
#
#     def upcount(self):
#         self.count +=1
#
# my_comment = Comment("My comment")
#
# my_comment.upcount()
# print(my_comment.count)
# print(my_comment.__dict__)
#
# my_comment.count = 17
# print(my_comment.count)
# print(Comment.count)
# print(Comment.__dict__)

class Image:

    def __init__(self, resolution,title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, resolution1):
        self.resolution = resolution1

    def title_upper(self):
        self.title = self.title.upper()

image1 = Image("image1", "jpg", "800x600")
print(image1.resolution, image1.title, image1.extension)

# image1.resize("1024x768")
# image1.title_upper()
# print(image1.resolution, image1.title, image1.extension)

image2 = Image("image2", "png", "1024x768")
image2.title_upper()
print(image2.resolution, image2.title, image2.extension)

# image2 = Image("image2", "png", "1024x768")
# print(image2.resolution, image2.title, image2.extension)
# image2.resize("1024x768")
# print(image2.resolution, image2.title, image2.extension)