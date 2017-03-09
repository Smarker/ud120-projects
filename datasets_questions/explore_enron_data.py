#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#person who made the most at ENRON:
"""
guy = ""
money = 0
for person in enron_data:
    if isinstance( enron_data[person]["total_payments"], ( int ) ) and person != "TOTAL":
        if enron_data[person]["total_payments"] > money:
            money = enron_data[person]["total_payments"]
            guy = person
print guy
print money
"""

#people with salary and emails that exist
"""
num_salary = 0;
num_email = 0;
for person in enron_data:
    if isinstance( enron_data[person]["salary"], ( int ) ):
        num_salary = num_salary + 1
    if enron_data[person]["email_address"] != "NaN":
        num_email = num_email + 1
print num_salary
print num_email
"""

# % of POIs with NaN as total_payments
num_NaN = 0
num_poi = 0
for person in enron_data:
    if enron_data[person]["poi"]:
        num_poi = num_poi + 1
        if enron_data[person]["total_payments"] == "NaN":
            num_NaN = num_NaN + 1
print num_poi
print float(num_NaN)/float(num_poi)

#number of people with NaN as total payments
num_NaN = 0
for person in enron_data:
    if enron_data[person]["total_payments"] == "NaN":
        num_NaN = num_NaN + 1
print float(num_NaN)

print len(enron_data.keys())

