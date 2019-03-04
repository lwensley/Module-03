{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#PyBank\n",
    "\n",
    "Your task is to create a Python script that analyzes the records to calculate each of the following:\n",
    "\n",
    "- The total number of months included in the dataset.\n",
    "- The net total amount of \"Profit/Losses\" over the entire period\n",
    "- The average of the changes in \"Profit/Losses\" over the entire period\n",
    "- The greatest increase in profits (date and amount) over the entire period\n",
    "- The greatest decrease in losses (date and amount) over the entire period\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import code\n",
    "import os\n",
    "import csv\n",
    "\n",
    "#define path\n",
    "PyBank_csv_path = os.path.join(\".\", \"budget_data.csv\")\n",
    "\n",
    "# Open and read csv\n",
    "with open(PyBank_csv_path, newline=\"\") as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "    \n",
    "    # Read the header row first skip this part if there is no header \n",
    "    csv_header = next(csvreader)\n",
    "    print(f\"CSV Header = {csv_header}\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
