from fastapi import FastAPI, UploadFile
from Models.models import session, DocumentsORM, Documents_textORM
from datetime import datetime
from os import remove
from cel import doc_analyse

tags_metadata = [
    {
        "name": "Загрузка картинки",
        "description": "Загружаем картинку с текстом. Вносим в базу данных и сохраняем на диск",
    },
    {
        "name": "Удаление картинки",
        'description': 'Удаляем картинку по id из базы данных и на диске'
    },
    {
        "name": "Анализ картинки",
        "description": "Загружаем картинку в pytesseract, обрабатываем, получаем текст и заносим в базу данных"
    },
    {
        'name': 'Получение текста с картинки',
        'description': 'Получаем текс с базы данных'
    }
]
app = FastAPI(
    title='Документы',
    openapi_tags=tags_metadata
)


@app.post('/upload_file/', tags=['Загрузка картинки'])
async def upload_file(file: UploadFile):
    with open(f'Files/{file.filename}', 'wb') as f:
        f.write(file.file.read())
        doc1 = DocumentsORM(psth=file.filename, date=datetime.now())
        session.add(doc1)
        session.flush()
        session.commit()
    return f'file: {file.filename}'


@app.delete('/doc_delete/', tags=["Удаление картинки"])
async def delete_file(file_id: int):
    query = session.get(DocumentsORM, file_id)
    if query is not None:
        name_file = query.psth
        remove(f'Files/{name_file}')
        session.delete(query)
        session.commit()
        return 'Удалено'
    else:
        return f'{file_id} не существует'


@app.post('/doc_analyse/', tags=["Анализ картинки"])
async def analyse(file_id: int):
    doc_analyse.delay(file_id)


@app.get('/get_text/', tags=['Получение текста с картинки'])
async def get_text(doc_text_id: int):
    query = session.get(Documents_textORM, doc_text_id)
    text_doc = query.text
    return text_doc
