import os


def getreportlist(path):
    ignorelist = {"_appcache", "_config", "logs"}
    reportlist = [names for names in os.listdir(
        path) if names not in ignorelist]
    return reportlist
