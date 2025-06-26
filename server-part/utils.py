import qrcode as qr
import base64
import re
from io import BytesIO


origin_pattern = re.compile(r'^(?:https?://)?([^/]+)', re.IGNORECASE)


def get_qr_bs64(data: str) -> str:
    """
    Формирование QR кода и передача его в виде base64 строки

    Args:
        data (str): информация, которую необходимо представить в виде QR-кода

    Returns:
        str: строка base64, содержащая байты изображения QR-кода
    """
    buffer = BytesIO()  # буфер для хранения QR
    qr_img = qr.make(data)  # создание QR
    qr_img.save(buffer, format='PNG')  # сохранение QR в буфер
    
    qr_bytes = buffer.getvalue()
    qr_b64 = base64.b64encode(qr_bytes)
    
    return qr_b64.decode('utf-8')

def get_origin(url: str) -> str:
    """
    Получение ресурса с помощью регулярных выражений

    Args:
        url (str): строка ссылки на ресурс

    Returns:
        str: имя ресурса
    """
    ex_str = ''

    match = origin_pattern.match(url)
    if match:
        ex_str = match.group(1)

    return ex_str
    
    