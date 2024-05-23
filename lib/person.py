#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]


class Person:
    approved_jobs = ["Sales", "ITC", "HR", "Marketing"]

    def __init__(self, name, job):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name.title()

        if job not in self.approved_jobs:
            print("Job must be in list of approved jobs.")
        else:
            self.job = job
