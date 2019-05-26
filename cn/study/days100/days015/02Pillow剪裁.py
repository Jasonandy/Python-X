from PIL import Image, ImageFilter


def pretty_picture():
    file_image = "koala.jpg"
    image = Image.open(file_image)
    image.filter(ImageFilter.CONTOUR).show()
    # image.format('JPEG')
    # image.size(500, 700)
    # image.mode('RGB')
    # image.show()


def main():
    pretty_picture()


if __name__ == '__main__':
    main()

