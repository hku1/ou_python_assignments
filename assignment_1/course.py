import datetime

def create_course(courseinfo):
    newcourse = Course(courseinfo['code'], courseinfo['naam'],
                       courseinfo['sbu'], courseinfo['startdatum'],
                       courseinfo['einddatum'])
    newcourse.add_required_courses(courseinfo['voorkennisverplicht'])
    newcourse.add_desired_courses(courseinfo['voorkennisgewenst'])
    newcourse.add_exams(courseinfo['tentamens'])
    return newcourse


# functions for lists of courses

def notdone(courses, done):
    """" select courses from list of available courses that not hve bene done"""
    notdone_lst = [course for course in courses if course.code not in done]
    return notdone_lst

def req_prior(courses, done):
    reqprior_lst = [course for course in courses if any(req_course in done for req_course in course.required_courses)]
    return reqprior_lst

def dsrd_prior(courses, done):
    dsrdprior_lst = [course for course in courses if any(dsrd_course in done for dsrd_course in course.desired_courses)]
    return dsrdprior_lst



class Start_and_enddate:
    """ Class for objects with a startdate and an enddate """

    def __init__(self, startdate=None, enddate=None):
        self.startdate = None
        self.enddate = None
        if startdate:
            self.startdate = datetime.date.fromisoformat(startdate)
        if enddate:
            self.enddate = datetime.date.fromisoformat(enddate)

    def __str__(self):
        """ String representation
        no startdate and enddate: returns variable
        otherwise: returns startdate,  enddate """
        if self.nodates():
            return 'variable'
        return str(self.startdate) + ', ' + str(self.enddate)

    def nodates(self):
        """ true when there is no startdate and no enddate """
        return (not self.startdate) and (not self.enddate)

    def quartile(self):
        """ Compute quartile
        startdate in month 9: return 1
        startdate in month 11: return 2
        startdate in month 2: return 3
        startdate in month 4: return 4
        otherwise: return -1
        """
        if self.startdate.month == 9:
            quartile = 1
        elif self.startdate.month == 11:
            quartile = 2
        elif self.startdate.month == 2:
            quartile = 3
        elif self.startdate.month == 4:
            quartile = 4
        else:
            quartile = -1
        return quartile


class Course:
    # TODO: implement and extend with attributes and methods

    def __init__(self, code, title, sbu, startdate, enddate, required_courses=None, desired_courses=None, exams=None):
        # TODO: implement
        self.code: str = code
        self.title: str = title
        self.sbu: int = sbu
        self.startdate: str = startdate
        self.enddate: str = enddate
        self.required_courses: list = required_courses
        self.desired_courses: list = desired_courses
        self.exams: list = exams
        self.dates = Start_and_enddate(startdate, enddate)

    def add_required_courses(self, courses):
        self.required_courses = []
        for course in courses:
            self.required_courses.append(course)
        return self.required_courses

    def add_desired_courses(self, courses):
        self.desired_courses = []
        for course in courses:
            self.desired_courses.append(course)
        return self.desired_courses

    def add_exams(self, exams):
        self.exams = []
        for exam in exams:
            self.exams.append(exam)
        return self.exams

    def get_code(self):
        return self.code
    
    # def __str__(self):
        """ string with:
        - code,
        - title,
        - period,
        - new line
        - codes of required foreknowledge or 'geen verplichte voorkennis'
        - new line
        - codes of desired foreknowledge or 'geen gewenste voorkennis'
        - new line
        """
        # return('code {0), title {1}, ')

        # TODO: implement
