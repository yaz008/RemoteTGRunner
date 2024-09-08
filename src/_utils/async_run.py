from threading import Thread
from _utils.func import save_document, unpack, setup_project, run_project

def async_run(file_id: str) -> Thread:
    save_document(file_id=file_id)
    project_name: str = unpack()
    setup_project()
    project_thread: Thread = Thread(target=run_project,
                                    name=project_name)
    project_thread.start()
    return project_thread