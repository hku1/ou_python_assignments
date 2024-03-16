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



# TODO: create and implement


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
    required_foreknowledge = []
    desired_foreknowledge = []
    exams = []

    def __init__(self, code, title, startdate=None, enddate=None):
        # TODO: implement
        self.code = code
        self.title = title
        self.dates = Start_and_enddate(startdate, enddate)


    def __str__(self):
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
        # TODO: implement
        # Done
        #string representing the required foreknowledge
        required_foreknowledge = ''
        if not required_foreknowledge:
            required_foreknowledge += "Geen verplicht voorkennis"
        else:
            for code in required_foreknowledge:
                required_foreknowledge += ' , ' + str(code)

        #string representing the desire foreknowledge
        desired_foreknowledge = ''
        if not desired_foreknowledge:
            desired_foreknowledge +="Geen gewenste voorkennis"
        else:
            for code in desired_foreknowledge:
                desired_foreknowledge += ' , ' + str(code)


        return str(self.code + ',' + self.title + ',' + str(self.dates.quartile()) + '\n'
            + ',' + required_foreknowledge + '\n'
            + ',' + desired_foreknowledge + '\n')


    def add_required_courses(self,course):
        """ Function to add required courses """
        self.required_foreknowledge.append(course)

    def add_desired_courses(self,course):
        """ Function to add desired courses """
        self.desired_foreknowledge.append(course)

    def add_exams(self, date):
        """ Function to add exams """
        self.exams.append(date)