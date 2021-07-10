# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


# function named save_csv() that uses the csv library to save the qualifying data as a file

def save_csv(output_path, qualifying_loans):
   header= ("Lender", "Max_Loan_Amount", "Max_Loan_to_Value", "Max_Debt_to_Income", "Credit_Score", "Interest_Rate")
   output_path =Path("data/qualifing_loan.csv")
   with open(output_path, "w", newline='') as csvfile:
      csvwriter = csv.writer(csvfile, delimiter = "|")
      csvwriter.writerow(header)
      for item in qualifying_loans:
        csvwriter.writerow(item)
   return



    