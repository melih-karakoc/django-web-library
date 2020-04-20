import io
import json
import cv2
import numpy
import requests
import pytesseract

from PIL import Image


def get_numbers_from_image_text(text):
    isbn_index = text.find('ISBN')
    if isbn_index == -1:
        return None
    isbn_parsed = text[isbn_index+3:]

    isbn = []
    for index, element in enumerate(isbn_parsed, 0):
        if element.isdigit():
            last_isbn_no = index + 17
            isbn.append(isbn_parsed[index:last_isbn_no])
            break
    just_digit = []
    for element in isbn[0]:
        if element.isdigit():
            just_digit.append(element)

    int_digit = (','.join(just_digit)).replace(',', '')
    int_digit = int(int_digit)
    return int_digit


def isbn_number_read(image):
    image_name = image.name
    img = cv2.imdecode(
        numpy.fromstring(image.read(), numpy.uint8),
        cv2.IMREAD_UNCHANGED)

    height, width, _ = img.shape
    # Cutting image
    roi = img

    url_api = "https://api.ocr.space/parse/image"
    _, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
    file_bytes = io.BytesIO(compressedimage)

    try:
        result = requests.post(url_api,
                               files={image_name: file_bytes},
                               data={"apikey": "bf053b551488957",
                                     "language": "tur"}, timeout=59)

        result = result.content.decode()
        result = json.loads(result)

        parsed_results = result.get("ParsedResults")[0]
        text_detected = parsed_results.get("ParsedText")
        print(text_detected)
        isbn = get_numbers_from_image_text(text_detected)
        print(isbn)
        print('------------------------------------------')
    except Exception:
        print('time out')
        isbn = None
    im = Image.open(image)
    # import ipdb; ipdb.set_trace()
    text = pytesseract.image_to_string(im)
    pillow_isbn_result = get_numbers_from_image_text(text)

    print(text)

    if len(str(isbn)) == 13:
        return isbn
    elif len(str(pillow_isbn_result)) == 13:
        return pillow_isbn_result
    elif len(str(isbn)) == 10:
        return isbn
    # elif not isbn or (
    # len(str(isbn)) != 13 and len(str(pillow_isbn_result)) != 13):
    #    return None
    else:
        return None
