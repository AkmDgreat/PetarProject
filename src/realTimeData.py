from writeMarketData import writeMarketData
from writeSigValue import writeSigValue
import multiprocessing

def realTimeData(stockName):
    if __name__ == "__main__":
        t1 = multiprocessing.Process(target=writeMarketData, args=[stockName])
        t2 = multiprocessing.Process(target=writeSigValue, args=[stockName])
        t1.start()
        t2.start()
        t1.join()
        t2.join()


realTimeData("BHP")
