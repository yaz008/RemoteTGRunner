from threading import Thread
from _utils.func import save_document, unpack, setup_project, run_project

def async_run(file_id: str, file_name: str) -> Thread:
    save_document(file_id=file_id)
    unpack()
    project_name: str = file_name.rsplit(sep='.', maxsplit=1)[0]
    setup_project(name=project_name)
    project_thread: Thread = Thread(target=run_project,
                                    name=project_name,
                                    args=[project_name])
    project_thread.start()
    return project_thread