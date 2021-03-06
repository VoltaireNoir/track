#!/usr/bin/env python3
import time
from datetime import datetime, timedelta
import pathlib, pickle

DATE_FORMAT = "%d-%m-%Y"
P = pathlib.Path(__file__).with_name(".tdata")

class activity:

    state = False
    start_time = None

    def __init__(self,name:str,log={}):
        self.name = name
        self.log = log

    def start(self):
        if self.state is False:
            self.state = True
            self.start_time = datetime.now()

    def stop(self):
        if self.state:
            self.state = False
            key = todays_date()
            delta = datetime.now() - self.start_time

            if key in self.log: self.log[key] += delta.seconds
            else: self.log[key] = delta.seconds

    def alog(self):
        if self.state is True:
            key = todays_date()
            offset = self.log[key] if key in self.log else 0
            return timeconv(offset + (datetime.now() - self.start_time).seconds)


class activities(list):

    ACTIVE = activity("")

    def __repr__(self):
        return f"Act[{', '.join(self.get_all_names())}]"

    def __str__(self):
        return self.__repr__()

    def add(self, name:str, log={}):
        if not self.exists(name): self.append(activity(name,log)); return True

    def delete(self, name:str):
        if self.exists(name): self.remove(self.get(name)); return True

    def flush(self):
        for _ in range(len(self)): self.pop(0)
        self.ACTIVE = activity("")

    def clean_log(self,name:str,date=None,today=False):
        act = self.get(name)
        if today and act:
            key = todays_date()
            if key in act.log: del act.log[key]; return True
        elif date and act:
            if date in act.log: del act.log[date]; return True
        elif act:
            act.log = {}; return True

    def clean_all_logs(self):
        for act in self:
            act.log = {}

    def exists(self, name:str):
        for activity in self:
            if name.lower() == activity.name.lower():
                return True
        return False

    def get_all_names(self) -> list:
        names = []
        for act in self:
            names.append(act.name.capitalize())
        return names

    def get(self,name:str):
        for act in self:
            if act.name.lower() == name.lower():
                return act

    def get_log(self,name:str,raw=False,recent=False):
        if self.exists(name):
            log = self.get(name).log

            if raw:
                return log

            if log == {}: return "Empty"
            loglist = [f"{key}: {timeconv(value)}" for key,value in log.items()]
            loglist.reverse()
            string = "\n".join(loglist[:3]) if recent and len(loglist) > 3 else "\n".join(loglist)
            return string

    def get_logs(self,raw=False):
        string = ""
        for act in self:
            string += act.name.capitalize() + "\n"
            string += self.get_log(act.name) + "\n\n"
        return string

    def todays_log(self,name:str):
        key = todays_date(); act = self.get(name)
        if act:
            log = str(timedelta(seconds=act.log[key])) if key in act.log else "Empty"
            return log

    def active_log(self):
        if self.ACTIVE.state:
            log = self.ACTIVE.alog()
            return log

    def activate(self, name=None):
        if name is None and not self.ACTIVE.state and self.ACTIVE.name != "":
            self.ACTIVE.start()
            return True
        elif name is not None and self.exists(name) and not self.ACTIVE.state:
            self.ACTIVE = self.get(name)
            self.ACTIVE.start()
            return True

    def deactivate(self):
        if self.ACTIVE.state:
            self.ACTIVE.stop()
            return True

    def select(self,name:str):
        if self.exists(name): self.ACTIVE = self.get(name); return True

    def map(self,name,index):
        if index >= len(self): return False
        if self.exists(name):
            self.insert(index,self.pop(self.index(self.get(name))))
            return True

def timeconv(seconds:int):
        formatted = str(timedelta(seconds=seconds))
        return formatted

def todays_date():
    todayob = datetime.now()
    formatted = todayob.strftime(DATE_FORMAT)
    return formatted

def save(activities):
    data = {}
    with P.open("wb") as f:
        for act in activities:
            data[act.name] = act.log

        pickle.dump((data,activities.ACTIVE),f)

def load():
    data = activities()
    try:
        with P.open("rb") as f:
            x = pickle.load(f)
    except (FileExistsError, FileNotFoundError, pickle.UnpicklingError): return data

    if x is None:
        return data

    if len(x) == 2:
        rawdata, active = x
        data.ACTIVE = active
        for name, log in rawdata.items():
            data.add(name,log)

    return data

def export_csv(activities,filename="activity_log.csv"):
    try:
        with open(filename,"w") as f:
            for act in activities:
                log = ";".join([f"{date}:{time}" for date, time in act.log.items()])
                f.write(f"{act.name};{log}\n")
    except:
        return False
    return True

if __name__ == "__main__":
    pass
