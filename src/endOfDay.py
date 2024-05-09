import pandas as pd
import CONSTANTS

# reads the csv, skips the required num of rows, writes the csv
def endOfDay(stockName):
    filePath = f"csv/{stockName} DATA.csv"
    df = pd.read_csv(filePath, skiprows=CONSTANTS.ONE_DAY)
    df.to_csv(filePath, index=False)