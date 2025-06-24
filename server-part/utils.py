import qrcode as qr
import base64
from io import BytesIO


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
