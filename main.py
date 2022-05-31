import pandas as pd
import datetime as dt

def combinePDH():
    parts = pd.read_csv(r'C:\Users\Isabella\Documents\Projects\DDMRP Simulator\Files\Part.csv')
    dh = pd.read_csv(r'C:\Users\Isabella\Documents\Projects\DDMRP Simulator\Files\Demand History.csv')

    parts['ItemLoc'] = parts['PartNumber'] + "-" + parts['Location']
    dh['ItemLoc'] = dh['PartNumber'] + "-" + dh['Location']

    parts.to_csv(r'C:\Users\Isabella\Documents\Projects\DDMRP Simulator\test.csv')

combinePDH()
