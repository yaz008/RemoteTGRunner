from _utils.func import save_document, unpack

def save(file_id: str) -> None:
    save_document(file_id=file_id)
    unpack()