import PIL.Image

ASCII_APHABETS = ["@", "#", "&", "%", "T", "+", "*", "-", "!", ",", " "]

def resizeImage(image):
    WIDTH, HEIGHT = image.size
    new_height = 100
    ratio = HEIGHT/WIDTH
    new_width = int(new_height*ratio)
    resized_image = image.resize((new_width,new_height))
    return resized_image

def grayImage(image):
    gray_image = image.convert("L")
    return gray_image

def ASCIIimage(image):
    pixels = image.getdata()
    characters = "".join([ASCII_APHABETS[pixel//25] for pixel in pixels])
    return characters

def main():
    path = input("ENTER LOCATION OF IMAGE:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print("INVAlID LOCATION")

    result = ASCIIimage(grayImage(resizeImage(image)))
    pixel_count = len(result)
    result_final = "\n".join(result[i:(i+100)]for i in range(0,pixel_count,100))
    f=open("aasd.txt","w")
    f.write(result_final)

main()


