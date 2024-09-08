from threading import Thread
from _utils.func import setup_project, run_project

def async_run(project_name: str) -> Thread:
    setup_project(name=project_name)
    project_thread: Thread = Thread(target=run_project,
                                    name=project_name,
                                    args=[project_name],
                                    daemon=True)
    project_thread.start()
    return project_thread