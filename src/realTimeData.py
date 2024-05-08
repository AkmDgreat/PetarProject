from writeMarketData import writeMarketData
from writeSigValue import writeSigValue
from runFunctionsConcurrently import runConcurrently
import threading

# def realTimeData(stockName):
#     runConcurrently(writeSigValue(stockName), writeMarketData(stockName))


def realTimeData(stockName):
    # if __name__ == "__main__":
    #     runConcurrently(writeSigValue, writeMarketData, stockName)
    if __name__ == "__main__":
        proc = threading.Thread(target = writeMarketData, args=(stockName))
        proc.start()
        proc2 = threading.Thread(target= writeSigValue, args=(stockName))
        proc2.start()

def realTimeData(stockName):
    t1 = threading.Thread(target=writeMarketData, args=[stockName])
    t2 = threading.Thread(target=writeSigValue, args=[stockName])
    t1.start()
    t2.start()

    t1.join()
    t2.join()

#also try concurent.futures

realTimeData("BHP")