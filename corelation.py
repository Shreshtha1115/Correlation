import plotly.express as px
import csv
import numpy as np


def getDataSource(data_path):
    marks_In_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_In_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x": marks_In_percentage, "y": days_present}


def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print("Correlation is:")


def setup():
    data_path = './Student Marks vs Days Present.csv'

    datasource = getDataSource(data_path)
    findCorrelation(datasource)


setup()
