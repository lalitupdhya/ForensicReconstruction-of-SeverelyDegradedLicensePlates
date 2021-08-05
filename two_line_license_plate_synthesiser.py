# Download ttf font you want to use
# Install PIL
# This code will  generate  number plates


from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2
import random

# ASCII A to Z are 65 to 90

hel = [75, 25, 15, 130, 120]
beb = [110, 2, 60, 135, 150]


# load the font and size
font = ImageFont.truetype("E:\\license\BebasNeueBold.ttf", 120)


rtc = 33  # number of districts
bias = 10
for r in range(1, rtc+1):
    for k in range(50):  # number of license plates per districts
        if r < 10:
            number_plate_1 = "GV 0" + str(r)
        else:
            number_plate_1 = "GV " + str(r)
        number_plate_2 = (chr(random.randint(65, 90)) +
                          chr(random.randint(65, 90))+" " + str(random.randint(1000, 9999)))
        img = np.zeros((200, 400, 3), np.uint8)
        pil_img = Image.fromarray(img)

        # to generate white background plates comment out the below three statements
        center = (int(0.5 * 400), int(0.5 * 200))
        yellow = (0, 0, 255, 255)
        ImageDraw.floodfill(pil_img, xy=center, value=yellow)

        draw = ImageDraw.Draw(pil_img)

        draw.text((75, 15), number_plate_1, font=font)
        draw.text((40, 105), number_plate_2, font=font)
        cv2_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
        cv2_img = cv2.bitwise_not(cv2_img)

        #cv2.imshow("number_plate", cv2_img)
        cv2.imwrite("E:\\license\\test\\"+number_plate_1.replace(" ", "") +
                    number_plate_2.replace(" ", "")+".png", cv2_img)
        # cv2.waitKey(10)


cv2.destroyAllWindows()
