import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f'Olha, {event.src_path} foi criado!')

    def on_deleted(self, event):
        print(f'Opa!,Alguem excluiu {event.src_path}!')

    def on_moved(self, event):
        print(f'Alguem moveu o arquivo {event.src_path}!')
        
    def on_modified(self, event):
        print(f'Alguem modificou {event.src_path}!')

    try: 
        while True:
            time.sleep(2)
            print('executando...')
    except KeyboardInterrupt:
        print("interrompido!")
        observer.stop()

event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()