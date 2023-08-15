# STOCK INDICATOR CLASS

import statistics
import modules.data_module as dm
import yfinance as yf


class StockIndicator(dm.Data):
    def __init__(self, stockSymbol, index="TO"):
        super().__init__(stockSymbol, index)

    # VOLUME INDICATOR

    # PRICE FUNCTIONS

    def priceListify(self):
        priceList = [[], []]

        for value in (self.makeData()).values():
            for keys, values in value.items():
                if keys == "Close":
                    priceList[0].append(values)
                elif keys == "Volume":
                    priceList[1].append(values)

        return priceList

    def dividePrices(self):
        priceList = self.priceListify()
        sumPrices = (max(priceList[0]) - min(priceList[0])) / 24

        return sumPrices

    def matchPrices(self):
        indicatorList = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        ]
        price = (self.priceListify())[0]
        volume = (self.priceListify())[1]
        i = 0
        min_price = min(price)
        sum_prices = self.dividePrices()

        for p in price:
            itemList = []

            if min_price <= price[i] <= (min_price + sum_prices):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[0].append(itemList)
            elif (min_price + sum_prices) <= price[i] <= (min_price + sum_prices * 2):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[1].append(itemList)
            elif (
                (min_price + sum_prices * 2) <= price[i] <= (min_price + sum_prices * 3)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[2].append(itemList)
            elif (
                (min_price + sum_prices * 3) <= price[i] <= (min_price + sum_prices * 4)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[3].append(itemList)
            elif (
                (min_price + sum_prices * 4) <= price[i] <= (min_price + sum_prices * 5)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[4].append(itemList)
            elif (
                (min_price + sum_prices * 5) <= price[i] <= (min_price + sum_prices * 6)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[5].append(itemList)
            elif (
                (min_price + sum_prices * 6) <= price[i] <= (min_price + sum_prices * 7)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[6].append(itemList)
            elif (
                (min_price + sum_prices * 7) <= price[i] <= (min_price + sum_prices * 8)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[7].append(itemList)
            elif (
                (min_price + sum_prices * 8) <= price[i] <= (min_price + sum_prices * 9)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[8].append(itemList)
            elif (
                (min_price + sum_prices * 9)
                <= price[i]
                <= (min_price + sum_prices * 10)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[9].append(itemList)
            elif (
                (min_price + sum_prices * 10)
                <= price[i]
                <= (min_price + sum_prices * 11)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[10].append(itemList)
            elif (
                (min_price + sum_prices * 11)
                <= price[i]
                <= (min_price + sum_prices * 12)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[11].append(itemList)
            elif (
                (min_price + sum_prices * 12)
                <= price[i]
                <= (min_price + sum_prices * 13)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[12].append(itemList)
            elif (
                (min_price + sum_prices * 13)
                <= price[i]
                <= (min_price + sum_prices * 14)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[13].append(itemList)
            elif (
                (min_price + sum_prices * 14)
                <= price[i]
                <= (min_price + sum_prices * 15)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[14].append(itemList)
            elif (
                (min_price + sum_prices * 15)
                <= price[i]
                <= (min_price + sum_prices * 16)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[15].append(itemList)
            elif (
                (min_price + sum_prices * 16)
                <= price[i]
                <= (min_price + sum_prices * 17)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[16].append(itemList)
            elif (
                (min_price + sum_prices * 17)
                <= price[i]
                <= (min_price + sum_prices * 18)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[17].append(itemList)
            elif (
                (min_price + sum_prices * 18)
                <= price[i]
                <= (min_price + sum_prices * 19)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[18].append(itemList)
            elif (
                (min_price + sum_prices * 19)
                <= price[i]
                <= (min_price + sum_prices * 20)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[19].append(itemList)
            elif (
                (min_price + sum_prices * 20)
                <= price[i]
                <= (min_price + sum_prices * 21)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[20].append(itemList)
            elif (
                (min_price + sum_prices * 21)
                <= price[i]
                <= (min_price + sum_prices * 22)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[21].append(itemList)
            elif (
                (min_price + sum_prices * 22)
                <= price[i]
                <= (min_price + sum_prices * 23)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[22].append(itemList)
            elif (
                (min_price + sum_prices * 23)
                <= price[i]
                <= (min_price + sum_prices * 24)
            ):
                itemList.append(price[i])
                itemList.append(volume[i])
                indicatorList[23].append(itemList)

            i += 1

        return indicatorList

    def findBiggestVolume(self):
        indicatorList = self.matchPrices()
        volumeList = []

        for priceList in indicatorList:
            volumeAmount = 0
            for priceVolume in priceList:
                volumeAmount += int(priceVolume[1])

            volumeList.append(volumeAmount)

        biggestVolume = volumeList.index(max(volumeList))

        return biggestVolume

    def findPOC(self):
        POCValues = []

        price = (self.priceListify())[0]
        min_price = min(price)
        sum_prices = self.dividePrices()

        biggestVolume = self.findBiggestVolume()

        up = min_price + sum_prices * (1 + biggestVolume)
        down = min_price + sum_prices * biggestVolume

        POCValues.append(up)
        POCValues.append(down)

        return POCValues

    # ATR INDICATOR

    def HL(self, i):
        data = self.makeData()

        hl = float(data[str(i)]["High"] - data[str(i)]["Low"])
        return hl

    def HC(self, i):
        data = self.makeData()

        hc = float(abs(data[str(i)]["Low"] - data[str(i - 1)]["Close"]))
        return hc

    def LC(self, i):
        data = self.makeData()

        lc = float(abs(data[str(i)]["High"] - data[str(i - 1)]["Close"]))
        return lc

        # List of the highest prices

        # ATR Indicator

    def HighestPrices(self):
        highestNumbers = []

        for i in reversed(range(14)):
            highNumber = []

            i += 1

            highNumber.append(self.HL(i))
            highNumber.append(self.HC(i))
            highNumber.append(self.LC(i))

            highestNumbers.append(max(highNumber))

        return highestNumbers

    def ATR(self):
        atr = sum(self.HighestPrices()) * (1 / 14)

        return atr

    # RSI INDICATOR

    def findRsi(self):
        change = (self.findData())["Close"].diff()
        change.dropna(inplace=True)

        # Create two copies of the Closing price Series
        change_up = change.copy()
        change_down = change.copy()

        change_up[change_up < 0] = 0
        change_down[change_down > 0] = 0

        # Verify that we did not make any mistakes
        change.equals(change_up + change_down)

        # Calculate the rolling average of average up and average down
        avg_up = change_up.rolling(14).mean()
        avg_down = change_down.rolling(14).mean().abs()

        rsi = 100 * avg_up / (avg_up + avg_down)

        removed_rsi = rsi[13:]

        return removed_rsi

    # BOLLINGER BANDS INDICATOR

    # PRICE FUNCTIONS

    def priceListifySMA(self):
        stock = yf.Ticker(self.stockSymbol + self.index).history(
            period="2d", interval="2m"
        )

        dataDict = {}

        for i in range(len(stock)):
            prices = {}
            prices["Open"] = stock["Open"][i]
            prices["Close"] = stock["Close"][i]
            prices["High"] = stock["High"][i]
            prices["Low"] = stock["Low"][i]
            prices["Volume"] = int(stock["Volume"][i])

            dataDict[f"{i}"] = prices

        PLSMA = []

        for value in dataDict.values():
            priceListSMA = []
            for keys, values in value.items():
                if keys == "High":
                    priceListSMA.append(values)
                elif keys == "Low":
                    priceListSMA.append(values)
                elif keys == "Close":
                    priceListSMA.append(values)
            PLSMA.append(priceListSMA)

        return PLSMA

    def typicalPrice(self, h, l, c):
        typicalPrice1 = (h + l + c) / 3

        return typicalPrice1

    # STANDARD DEVIATION

    def standardDeviationChecker(self, TP):
        data = TP
        print(data)
        standardDeviation = statistics.stdev(data)
        mean = statistics.mean(data)
        z = -1.28
        zScore = (z * standardDeviation) + mean

        return standardDeviation

    def simpleMovingAverage(self):
        PLSMA = self.priceListifySMA()
        typicalPriceList = []

        for interval in range(len(PLSMA)):
            typicalPriceNum = self.typicalPrice(
                PLSMA[interval][0], PLSMA[interval][1], PLSMA[interval][2]
            )
            typicalPriceList.append(typicalPriceNum)

        standardDeviation = self.standardDeviationChecker(typicalPriceList[-20:])

        SMA = float(sum(typicalPriceList[-20:])) / float(len(typicalPriceList[-20:]))

        return [SMA, standardDeviation]

    def BollingerBands(self):
        SMA = self.simpleMovingAverage()

        up = SMA[0] + SMA[1]
        down = SMA[0] - SMA[1]

        return [up, SMA[0], down]
