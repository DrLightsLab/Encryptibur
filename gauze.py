import sys
import time
from pylint import lint
from pylint.reporters.text import TextReporter
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class gauze(PatternMatchingEventHandler):
    patterns = ["*.py"]

    def bandage(self, event):
        """
        event.event_type 'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory True | False
        event.src_path path/to/observed/file
        """
        print event.src_path, event.event_type

    def on_modified(self, event):
        print event.src_path
        ARGS = ["-r","n", "--rcfile=rcpylint"]
        filename = event.src_path
        pylint_output = self.Writer()
        lint.Run([filename]+ARGS, reporter=TextReporter(pylint_output), exit=False)
        for l in pylint_output.read():
            print l
        self.bandage(event)

    def on_create(self, event):
        self.bandage(event)

    def on_deleted(self, event):
        self.bandage(event)

    def on_moved(self, event):
        self.bandage(event)

    class Writer(object):
        def __init__(self):
            self.content = []
        def write(self, string):
            self.content.append(string)
        def read(self):
            return self.content


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer = Observer()
    observer.schedule(gauze(), path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
