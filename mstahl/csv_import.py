# coding: utf-8
import csv

inputFile = "../probieren.csv"
outputFile = "probieren_mit_id.csv"

csv_file = csv.csv_import(inputFile)

csv.csv_export(outputFile,csv_file)