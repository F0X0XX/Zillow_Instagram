from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO


template = Image.open("1.png")


new_image = Image.open("15503_SW_T5_Rd,_Beverly,_WA.jpg")

replacement_area = (113, 190, 980, 730)  


new_image_resized = new_image.resize((replacement_area[2] - replacement_area[0], 
                                      replacement_area[3] - replacement_area[1]))


template.paste(new_image_resized, replacement_area)

def overlay_text_on_image(image, text, y_pos =780, font_size=20):
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", font_size) 
    except IOError:
        font = ImageFont.load_default()  
    text_bbox = draw.textbbox((0, 0), text, font=font)  
    text_width = text_bbox[2] - text_bbox[0] 
    position = (image.width // 2 - text_width // 2, y_pos) 
    text_color = (5, 255, 100)
    draw.text(position, text, fill=text_color, font=font) 


overlay_text_on_image(template, "15503 SW T5 Rd, Beverly, WA 99321", y_pos=780, font_size=50)


template.save("updated_template_with_text.png")

template.show()