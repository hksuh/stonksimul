import sys
import sqlite3
import yfinance as yf

def main():
    dbfilename='yfinance.db'

    for arg in sys.argv[1:]:
        with sqlite3.connect('yfinance.db') as connection:
            yfobj = yf.Ticker(ticker)
            stockdf = yfobj.history(period="max")
            stockdf.to_sql(ticker,connection,if_exists='replace')
            print(ticker+" saved in "+dbfilename)

if __name__ == '__main__':
    main()
