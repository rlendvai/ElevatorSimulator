from turtle import *
import config
import random
import itertools
import math
import time
import names
import pickle
import arrow
from dateutil import tz



class Appointment():
    def __init__(self, duration):
        self.patient = Patient()
        self.duration = 30

class Patient():
    def __init__(self):
        self.name = names.get_full_name()

class Slot():
    def __init__(self, begin_time, length):
        self.appointment = None
        self.type = "General"
        self.begin_time = begin_time


    def fill(self, appointment):
        #assert self.appointment == None, "Trying to fill already filled slot!"
        if self.appointment == None:
            self.appointment = appointment
            return True
        else:
            sys.exit("You can not fill an already filled slot!")
    def unfill(self):
        self.appointment = None


    def filled_string(self):
        if self.appointment != None:
            return self.appointment.patient.name
        else:
            return "--------------"

    def filled_status(self):
        if self.appointment == None:
            return False
        else:
            return True


class Day():
    def __init__ (self, arrow_day, total_slots, length):
        self.slots = []
        self.begin_time = arrow_day
        for i in range (total_slots):
            self.slots.append(
                Slot(self.begin_time.shift(minutes=(30*i)), length)
                            )

    def show(self):
        print(emphasize("day " + str(self.day_number)))
        for i in range(len(self.slots)):
            if i < 10:
                print(" ", end='')
            print(i, self.slots[i].filled_string())

    def add_appointment (self, slot_no, appointment):
        slot = self.slots[slot_no]
        return slot.fill(appointment)

    def cancel_appointment(self, slot):

        self.slots[slot].unfill()


class Schedule ():
    def __init__(self, num_days = 1, num_slots = 4, duration = 30):
        self.start = arrow.get('2017, 07, 01, 09am', 'YYYY, MM, DD, HHa')
        self.days = []
        self.initialize(num_slots)
        self.duration = duration


    def initialize(self, num_slots):

        for i, day in enumerate(self.days):
            daDay(self.start.shift(days=i), num_slots, 30)

    def show(self):
        for day in self.days:
            day.show()
    def cancel_appointment(self, day, slot):

        self.days[day].cancel_appointment(slot)


def emphasize(string):
    emphasis = "*******"
    string = string.upper()
    new_string = emphasis + " " + string + " " + emphasis
    return new_string

def main():

    FRESH = True

    if FRESH:
        myschedule = Schedule()
    else:
        fh = open("schedule.obj", "rb")
        myschedule = pickle.load(fh)


    myschedule.show()
    #myschedule.cancel_appointment(0,3)
    myschedule.show()


    fh = open("schedule.obj", "wb")
    pickle.dump(myschedule, fh)
    fh.close()


main()
