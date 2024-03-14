import pathlib
import json
import course


class Preparation:
    COURSES_DONE_FILE = 'curssengedaan.json'
    COURSES_OFFER_FILE = 'cursusaanbod.json'
    available_courses = []

    def __init__(self, path=None):
        if path:
            self.path = path
        else:
            self.path = pathlib.Path.cwd()
        self.done_codes = set()

    def load_courses_done(self):
        path = self.path / pathlib.Path(self.COURSES_DONE_FILE)
        file_path = pathlib.Path(path)
        with file_path.open('r') as f:
            self.done_codes = set(json.load(f))

    def load_courses_offer(self):
        path = self.path / pathlib.Path(self.COURSES_OFFER_FILE)
        file_path = pathlib.Path(path)
        with file_path.open('r') as f:
            for info in json.load(f):
                self.available_courses.append(course.create_course(info))
