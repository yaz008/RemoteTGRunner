from _utils.func import save_document, unpack, setup_project

def save(file_id: str, project_name: str) -> None:
    save_document(file_id=file_id)
    unpack()
    setup_project(name=project_name)