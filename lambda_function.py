import numpy as np
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import pyimgur
import boto3
import botocore
import os


def lambda_handler(event, context):
    list_im = []
    list_text = []

    for value in event:
        list_im.append(BytesIO(requests.get(value['url']).content))
        list_text.append(value['text'])

    images = [Image.open(i) for i in list_im]

    s3 = boto3.resource('s3').Bucket('imgurupload')

    try:
        s3.download_file(
            'tmp/Hack-BoldOblique.ttf', '/tmp/font.ttf')
    except botocore.exceptions.ClientError as e:
        print("Error: ", e)

    # use a truetype font
    font = ImageFont.truetype('/tmp/font.ttf', 22)

    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)
    new_horizontal_image = Image.new('RGB', (total_width, max_height))

    new_vertical_image = Image.new('RGB', (max_height, total_width))

    x_offset = 0
    y_offset = 0
    index = 0
    border_color = "black"
    for image in images:
        draw = ImageDraw.Draw(image, "RGBA")
        w, h = draw.textsize(list_text[index].upper(), font)
        # thicker border
        newWidth = (398-w)/2
        newHeight = (350-h)
        newText = list_text[index].upper()
        draw.text((newWidth+1, newHeight-1),
                  newText, font=font, fill=border_color)
        draw.text((newWidth-1, newHeight+1),
                  newText, font=font, fill=border_color)
        draw.text((newWidth+1, newHeight+1),
                  newText, font=font, fill=border_color)
        draw.text((newWidth-1, newHeight-1),
                  newText, font=font, fill=border_color)
        draw.text(((398-w)/2, (350-h)),
                  newText, font=font, fill=(255, 255, 255, 255))

        # new_horizontal_image.paste(image, (x_offset, 0))
        new_vertical_image.paste(image, (0, y_offset))
        x_offset += image.size[0]
        y_offset += image.size[0]
        index += 1

    # new_horizontal_image.save('/tmp/horizontalImage.png',
    #                           format='PNG', subsampling=0, quality=100)
    new_vertical_image.save('/tmp/verticalImage.png',
                            format='PNG', subsampling=0, quality=100)

    LAMBDA_IMGUR_CLIENT_ID = os.environ['IMGUR_CLIENT_ID']

    imgur_object = pyimgur.Imgur(LAMBDA_IMGUR_CLIENT_ID)

    uploaded_image = imgur_object.upload_image(
        "/tmp/verticalImage.png", title="Made with hypemoji.surge.sh")

    # TODO implement
    return {
        'statusCode': 200,
        'body': uploaded_image.link
    }
