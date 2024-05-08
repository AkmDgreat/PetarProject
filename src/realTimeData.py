from writeMarketData import writeMarketData
from writeSigValue import writeSigValue
from runFunctionsConcurrently import runConcurrently

def realTimeData(stockName):
    runConcurrently(writeMarketData(stockName), writeSigValue(stockName))