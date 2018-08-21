# coding: utf-8
import mst_csv

inputFile = "../probieren.csv"
outputFile = "probieren_mit_id.csv"

csv_file = mst_csv.csv_import(inputFile)

mst_csv.csv_export(outputFile,csv_file)