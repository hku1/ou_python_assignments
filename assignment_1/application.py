import planner
import preparation


def generate_planning():
    prep = preparation.Preparation(path='C:/Users/harmj/OneDrive/Documenten/OU_python_course/data/assignments/assignment_1')
    prep.load_courses_done()
    prep.load_courses_offer()
    my_planner = planner.Planner(prep)
    print(my_planner.generate())


generate_planning()
