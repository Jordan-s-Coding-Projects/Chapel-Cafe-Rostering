import pandas as pd
import datetime
import numpy as np
import os

"""
Person in cafe crew, contains name, skills and availability
"""
class Person:
    def __init__(self, name, row_data, column_headings):
        self.name = name
        self.skills = []
        self.max_shifts_per_sunday = 3
        self.current_allocated_shifts = {1:1, 2:1, 3:3} # Sunday:Shift

        for i in range(0, len(column_headings)):
            if row_data[i] == 'Y':
                self.skills.append(column_headings[i])

    def get_name(self):
        return self.name

    def get_skills(self):
        return self.skills


"""
Current roster state in tree search - contains name allocation at any given instance
"""
class NodeRoster:
    def __init__(self, prev_node, state):
        self.prev_node = prev_node
        self.state = state
        # something capturing current state (existing roster so far, next pending position (sunday, shift, role)

    def advance(self, people):
        # attempt to allocate pending slot, goes through list of people
        # if fulfills: capability, date available, within limit AND not already allocated on current shift
        #       self.allocate(person) to pending state, return all required arguments for new state
        # else, try next person in the list. If reach end of list, BACKTRACE (only needs implementing if availability is very bad)
        pass

    def allocate(self, person):
        # adds given person to current pending slot, updates person's allocated shifts
        pass

    def __hash__(self):
        return hash(self.state)


def main():
    filepath = os.path.join(os.path.dirname(__file__), "constraint_data.xlsx")
    data = pd.read_excel(filepath, sheet_name="capability")
    data = data.set_index("Name")

    # get unavailable days and volume constraints

    # perform tree search

    # state
    year = 2022
    month = 9
    roster_state_0 = init_roster_state(year, month)


    people = generate_people_object_list(data)  # get list of people class


"""
Iteratively instantiate 'person' class and populate a list with them
"""
def generate_people_object_list(data):
    skills = data.columns.tolist()
    people_object_list = []

    for name in data.index.tolist():
        person = Person(name, data.loc[name], skills)
        people_object_list.append(person)
    return people_object_list


def count_sundays(year, month):
    sunday_count = 0
    for i in range(1,31):
        if datetime.date.weekday(datetime.date(year, month, i)) == 6:
            sunday_count += 1
    return sunday_count


def init_roster_state(year, month):
    sundays_count = count_sundays(year, month)
    roster_state = {}
    for i in range(sundays_count):
        day = {}
        for j in range(3):
            day[j] = {"Espresso": 0, "Milk": 0, "Counter": 0, "Food1": 0, "Food2": 0}
        init_roster_state[i] = day
    return roster_state

if __name__ == main():
    main()
