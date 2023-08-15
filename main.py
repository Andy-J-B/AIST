# imports

import modules.stock_indicators as sIclass


stocks = ["SHOP", "BBD-B", "CVE", "FM", "SU"]

# main function
if __name__ == "__main__":
    choice = input("Reset (r) or make (m)?\n\n - ")

    if choice == "m":
        for stock in stocks:
            sI = sIclass.StockIndicator(stock)

            sI.mainDataFunction()
            POCValues = sI.findPOC()
            BB = sI.BollingerBands()

            print(f"The POC is in between {(POCValues[1])} and {(POCValues[0])}")
            print(sI.findRsi())
            print(f"atr value is {sI.ATR()}")
            print(
                f"The top Bollinger Band is {BB[0]}, mid = {BB[1]} and Low is {BB[2]}"
            )

    elif choice == "r":
        for stock in stocks:
            sI = sIclass.StockIndicator(stock)
            sI.deleteFolder()
