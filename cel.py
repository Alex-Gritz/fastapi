from celery import Celery
import pytesseract
from PIL import Image

from Models.models import session, DocumentsORM, Documents_textORM
from config import BROKER_URL

celery = Celery('tasks', broker=f'{BROKER_URL}/')


@celery.task
def doc_analyse(file_id: int):
    query = session.get(DocumentsORM, file_id)
    name_file = query.psth
    img = Image.open(f'Files/{name_file}')
    text_doc = pytesseract.image_to_string(img)
    doc_text = Documents_textORM(id_doc=file_id, text=text_doc)
    session.add(doc_text)
    session.flush()
    session.commit()
    return f'{file_id} обработана'
