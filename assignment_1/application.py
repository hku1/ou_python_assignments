import planner
import preparation


def generate_planning():
    prep = preparation.Preparation()
    prep.load_courses_done()
    prep.load_courses_offer()
    my_planner = planner.Planner(prep)
    print(my_planner.generate())


generate_planning()
