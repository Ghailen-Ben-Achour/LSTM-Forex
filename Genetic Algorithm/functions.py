import pandas as pd
import numpy as np
from numpy import array


def extract_train_data():
    AUD_CAD = pd.read_csv('./pairs/export-AUDCAD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_CHF = pd.read_csv('./pairs/export-AUDCHF-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_JPY = pd.read_csv('./pairs/export-AUDJPY-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_NZD = pd.read_csv('./pairs/export-AUDNZD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_USD = pd.read_csv('./pairs/export-AUDUSD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CAD_CHF = pd.read_csv('./pairs/export-CADCHF-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CAD_JPY = pd.read_csv('./pairs/export-CADJPY-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CHF_JPY = pd.read_csv('./pairs/export-CHFJPY-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_AUD = pd.read_csv('./pairs/export-EURAUD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_CAD = pd.read_csv('./pairs/export-EURCAD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_CHF = pd.read_csv('./pairs/export-EURCHF-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_GBP = pd.read_csv('./pairs/export-EURGBP-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_JPY = pd.read_csv('./pairs/export-EURJPY-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_NZD = pd.read_csv('./pairs/export-EURNZD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_USD = pd.read_csv('./pairs/export-EURUSD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_AUD = pd.read_csv('./pairs/export-GBPAUD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_CAD = pd.read_csv('./pairs/export-GBPCAD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_CHF = pd.read_csv('./pairs/export-GBPCHF-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_JPY = pd.read_csv('./pairs/export-GBPJPY-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_NZD = pd.read_csv('./pairs/export-GBPNZD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_USD = pd.read_csv('./pairs/export-GBPUSD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_CAD = pd.read_csv('./pairs/export-NZDCAD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_CHF = pd.read_csv('./pairs/export-NZDCHF-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_JPY = pd.read_csv('./pairs/export-NZDJPY-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_USD = pd.read_csv('./pairs/export-NZDUSD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_CAD = pd.read_csv('./pairs/export-USDCAD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_CHF = pd.read_csv('./pairs/export-USDCHF-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_JPY = pd.read_csv('./pairs/export-USDJPY-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)

    
    return AUD_CAD,AUD_CHF,AUD_JPY,AUD_NZD,AUD_USD,CAD_CHF,CAD_JPY,CHF_JPY,EUR_AUD,EUR_CAD,EUR_CHF,EUR_GBP,EUR_JPY,EUR_NZD,EUR_USD,GBP_AUD,GBP_CAD,GBP_CHF,GBP_JPY,GBP_NZD,GBP_USD,NZD_CAD,NZD_CHF,NZD_JPY,NZD_USD,USD_CAD,USD_CHF,USD_JPY

def extract_train_datah1():
    AUD_CAD = pd.read_csv('./pairsh1/export-AUDCAD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_CHF = pd.read_csv('./pairsh1/export-AUDCHF-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_JPY = pd.read_csv('./pairsh1/export-AUDJPY-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_NZD = pd.read_csv('./pairsh1/export-AUDNZD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_USD = pd.read_csv('./pairsh1/export-AUDUSD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CAD_CHF = pd.read_csv('./pairsh1/export-CADCHF-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CAD_JPY = pd.read_csv('./pairsh1/export-CADJPY-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CHF_JPY = pd.read_csv('./pairsh1/export-CHFJPY-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_AUD = pd.read_csv('./pairsh1/export-EURAUD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_CAD = pd.read_csv('./pairsh1/export-EURCAD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_CHF = pd.read_csv('./pairsh1/export-EURCHF-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_GBP = pd.read_csv('./pairsh1/export-EURGBP-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_JPY = pd.read_csv('./pairsh1/export-EURJPY-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_NZD = pd.read_csv('./pairsh1/export-EURNZD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_USD = pd.read_csv('./pairsh1/export-EURUSD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_AUD = pd.read_csv('./pairsh1/export-GBPAUD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_CAD = pd.read_csv('./pairsh1/export-GBPCAD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_CHF = pd.read_csv('./pairsh1/export-GBPCHF-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_JPY = pd.read_csv('./pairsh1/export-GBPJPY-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_NZD = pd.read_csv('./pairsh1/export-GBPNZD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_USD = pd.read_csv('./pairsh1/export-GBPUSD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_CAD = pd.read_csv('./pairsh1/export-NZDCAD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_CHF = pd.read_csv('./pairsh1/export-NZDCHF-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_JPY = pd.read_csv('./pairsh1/export-NZDJPY-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_USD = pd.read_csv('./pairsh1/export-NZDUSD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_CAD = pd.read_csv('./pairsh1/export-USDCAD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_CHF = pd.read_csv('./pairsh1/export-USDCHF-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_JPY = pd.read_csv('./pairsh1/export-USDJPY-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)

    
    return AUD_CAD,AUD_CHF,AUD_JPY,AUD_NZD,AUD_USD,CAD_CHF,CAD_JPY,CHF_JPY,EUR_AUD,EUR_CAD,EUR_CHF,EUR_GBP,EUR_JPY,EUR_NZD,EUR_USD,GBP_AUD,GBP_CAD,GBP_CHF,GBP_JPY,GBP_NZD,GBP_USD,NZD_CAD,NZD_CHF,NZD_JPY,NZD_USD,USD_CAD,USD_CHF,USD_JPY

def extract_train_datah2():
    AUD_CAD = pd.read_csv('./pairsh2/export-AUDCAD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_CHF = pd.read_csv('./pairsh2/export-AUDCHF-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_JPY = pd.read_csv('./pairsh2/export-AUDJPY-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_NZD = pd.read_csv('./pairsh2/export-AUDNZD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_USD = pd.read_csv('./pairsh2/export-AUDUSD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CAD_CHF = pd.read_csv('./pairsh2/export-CADCHF-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CAD_JPY = pd.read_csv('./pairsh2/export-CADJPY-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CHF_JPY = pd.read_csv('./pairsh2/export-CHFJPY-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_AUD = pd.read_csv('./pairsh2/export-EURAUD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_CAD = pd.read_csv('./pairsh2/export-EURCAD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_CHF = pd.read_csv('./pairsh2/export-EURCHF-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_GBP = pd.read_csv('./pairsh2/export-EURGBP-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_JPY = pd.read_csv('./pairsh2/export-EURJPY-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_NZD = pd.read_csv('./pairsh2/export-EURNZD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_USD = pd.read_csv('./pairsh2/export-EURUSD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_AUD = pd.read_csv('./pairsh2/export-GBPAUD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_CAD = pd.read_csv('./pairsh2/export-GBPCAD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_CHF = pd.read_csv('./pairsh2/export-GBPCHF-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_JPY = pd.read_csv('./pairsh2/export-GBPJPY-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_NZD = pd.read_csv('./pairsh2/export-GBPNZD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_USD = pd.read_csv('./pairsh2/export-GBPUSD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_CAD = pd.read_csv('./pairsh2/export-NZDCAD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_CHF = pd.read_csv('./pairsh2/export-NZDCHF-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_JPY = pd.read_csv('./pairsh2/export-NZDJPY-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_USD = pd.read_csv('./pairsh2/export-NZDUSD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_CAD = pd.read_csv('./pairsh2/export-USDCAD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_CHF = pd.read_csv('./pairsh2/export-USDCHF-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_JPY = pd.read_csv('./pairsh2/export-USDJPY-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)

    
    return AUD_CAD,AUD_CHF,AUD_JPY,AUD_NZD,AUD_USD,CAD_CHF,CAD_JPY,CHF_JPY,EUR_AUD,EUR_CAD,EUR_CHF,EUR_GBP,EUR_JPY,EUR_NZD,EUR_USD,GBP_AUD,GBP_CAD,GBP_CHF,GBP_JPY,GBP_NZD,GBP_USD,NZD_CAD,NZD_CHF,NZD_JPY,NZD_USD,USD_CAD,USD_CHF,USD_JPY


def extract_val_data():
    AUD_CAD = pd.read_csv('./validation/export-AUDCAD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_CHF = pd.read_csv('./validation/export-AUDCHF-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_JPY = pd.read_csv('./validation/export-AUDJPY-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_NZD = pd.read_csv('./validation/export-AUDNZD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_USD = pd.read_csv('./validation/export-AUDUSD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CAD_CHF = pd.read_csv('./validation/export-CADCHF-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CAD_JPY = pd.read_csv('./validation/export-CADJPY-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CHF_JPY = pd.read_csv('./validation/export-CHFJPY-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_AUD = pd.read_csv('./validation/export-EURAUD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_CAD = pd.read_csv('./validation/export-EURCAD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_CHF = pd.read_csv('./validation/export-EURCHF-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_GBP = pd.read_csv('./validation/export-EURGBP-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_JPY = pd.read_csv('./validation/export-EURJPY-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_NZD = pd.read_csv('./validation/export-EURNZD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_USD = pd.read_csv('./validation/export-EURUSD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_AUD = pd.read_csv('./validation/export-GBPAUD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_CAD = pd.read_csv('./validation/export-GBPCAD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_CHF = pd.read_csv('./validation/export-GBPCHF-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_JPY = pd.read_csv('./validation/export-GBPJPY-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_NZD = pd.read_csv('./validation/export-GBPNZD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_USD = pd.read_csv('./validation/export-GBPUSD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_CAD = pd.read_csv('./validation/export-NZDCAD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_CHF = pd.read_csv('./validation/export-NZDCHF-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_JPY = pd.read_csv('./validation/export-NZDJPY-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_USD = pd.read_csv('./validation/export-NZDUSD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_CAD = pd.read_csv('./validation/export-USDCAD-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_CHF = pd.read_csv('./validation/export-USDCHF-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_JPY = pd.read_csv('./validation/export-USDJPY-Hour4-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    return AUD_CAD,AUD_CHF,AUD_JPY,AUD_NZD,AUD_USD,CAD_CHF,CAD_JPY,CHF_JPY,EUR_AUD,EUR_CAD,EUR_CHF,EUR_GBP,EUR_JPY,EUR_NZD,EUR_USD,GBP_AUD,GBP_CAD,GBP_CHF,GBP_JPY,GBP_NZD,GBP_USD,NZD_CAD,NZD_CHF,NZD_JPY,NZD_USD,USD_CAD,USD_CHF,USD_JPY

def extract_val_datah1():
    AUD_CAD = pd.read_csv('./validationh1/export-AUDCAD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_CHF = pd.read_csv('./validationh1/export-AUDCHF-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_JPY = pd.read_csv('./validationh1/export-AUDJPY-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_NZD = pd.read_csv('./validationh1/export-AUDNZD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_USD = pd.read_csv('./validationh1/export-AUDUSD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CAD_CHF = pd.read_csv('./validationh1/export-CADCHF-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CAD_JPY = pd.read_csv('./validationh1/export-CADJPY-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CHF_JPY = pd.read_csv('./validationh1/export-CHFJPY-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_AUD = pd.read_csv('./validationh1/export-EURAUD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_CAD = pd.read_csv('./validationh1/export-EURCAD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_CHF = pd.read_csv('./validationh1/export-EURCHF-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_GBP = pd.read_csv('./validationh1/export-EURGBP-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_JPY = pd.read_csv('./validationh1/export-EURJPY-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_NZD = pd.read_csv('./validationh1/export-EURNZD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_USD = pd.read_csv('./validationh1/export-EURUSD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_AUD = pd.read_csv('./validationh1/export-GBPAUD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_CAD = pd.read_csv('./validationh1/export-GBPCAD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_CHF = pd.read_csv('./validationh1/export-GBPCHF-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_JPY = pd.read_csv('./validationh1/export-GBPJPY-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_NZD = pd.read_csv('./validationh1/export-GBPNZD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_USD = pd.read_csv('./validationh1/export-GBPUSD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_CAD = pd.read_csv('./validationh1/export-NZDCAD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_CHF = pd.read_csv('./validationh1/export-NZDCHF-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_JPY = pd.read_csv('./validationh1/export-NZDJPY-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_USD = pd.read_csv('./validationh1/export-NZDUSD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_CAD = pd.read_csv('./validationh1/export-USDCAD-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_CHF = pd.read_csv('./validationh1/export-USDCHF-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_JPY = pd.read_csv('./validationh1/export-USDJPY-Hour-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    return AUD_CAD,AUD_CHF,AUD_JPY,AUD_NZD,AUD_USD,CAD_CHF,CAD_JPY,CHF_JPY,EUR_AUD,EUR_CAD,EUR_CHF,EUR_GBP,EUR_JPY,EUR_NZD,EUR_USD,GBP_AUD,GBP_CAD,GBP_CHF,GBP_JPY,GBP_NZD,GBP_USD,NZD_CAD,NZD_CHF,NZD_JPY,NZD_USD,USD_CAD,USD_CHF,USD_JPY

def extract_val_datah2():
    AUD_CAD = pd.read_csv('./validationh2/export-AUDCAD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_CHF = pd.read_csv('./validationh2/export-AUDCHF-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_JPY = pd.read_csv('./validationh2/export-AUDJPY-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_NZD = pd.read_csv('./validationh2/export-AUDNZD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    AUD_USD = pd.read_csv('./validationh2/export-AUDUSD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CAD_CHF = pd.read_csv('./validationh2/export-CADCHF-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CAD_JPY = pd.read_csv('./validationh2/export-CADJPY-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    CHF_JPY = pd.read_csv('./validationh2/export-CHFJPY-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_AUD = pd.read_csv('./validationh2/export-EURAUD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_CAD = pd.read_csv('./validationh2/export-EURCAD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_CHF = pd.read_csv('./validationh2/export-EURCHF-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_GBP = pd.read_csv('./validationh2/export-EURGBP-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_JPY = pd.read_csv('./validationh2/export-EURJPY-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_NZD = pd.read_csv('./validationh2/export-EURNZD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    EUR_USD = pd.read_csv('./validationh2/export-EURUSD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_AUD = pd.read_csv('./validationh2/export-GBPAUD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_CAD = pd.read_csv('./validationh2/export-GBPCAD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_CHF = pd.read_csv('./validationh2/export-GBPCHF-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_JPY = pd.read_csv('./validationh2/export-GBPJPY-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_NZD = pd.read_csv('./validationh2/export-GBPNZD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    GBP_USD = pd.read_csv('./validationh2/export-GBPUSD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_CAD = pd.read_csv('./validationh2/export-NZDCAD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_CHF = pd.read_csv('./validationh2/export-NZDCHF-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_JPY = pd.read_csv('./validationh2/export-NZDJPY-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    NZD_USD = pd.read_csv('./validationh2/export-NZDUSD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_CAD = pd.read_csv('./validationh2/export-USDCAD-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_CHF = pd.read_csv('./validationh2/export-USDCHF-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    USD_JPY = pd.read_csv('./validationh2/export-USDJPY-Hour2-BarChartHist.csv', index_col=0, parse_dates=True,skipinitialspace=True)
    return AUD_CAD,AUD_CHF,AUD_JPY,AUD_NZD,AUD_USD,CAD_CHF,CAD_JPY,CHF_JPY,EUR_AUD,EUR_CAD,EUR_CHF,EUR_GBP,EUR_JPY,EUR_NZD,EUR_USD,GBP_AUD,GBP_CAD,GBP_CHF,GBP_JPY,GBP_NZD,GBP_USD,NZD_CAD,NZD_CHF,NZD_JPY,NZD_USD,USD_CAD,USD_CHF,USD_JPY

def perf(df):
    df_new = pd.DataFrame()    
    df_new['open'] = df['open']
    df_new['close_prec'] = df['close'].shift(1)
    df_new['high'] = df['high'].shift(1)
    df_new['low'] = df['low'].shift(1)
    df_new['close'] = df['close']
    df_new['perf'] = ((df['close']-df_new['close_prec'])*100/df['close']).shift(1)
    df_new = df_new.dropna(axis=0)
    return df_new

#Organising the data
def organising_data(AUD_CAD,AUD_CHF,AUD_JPY,AUD_NZD,AUD_USD,CAD_CHF,CAD_JPY,CHF_JPY,EUR_AUD,EUR_CAD,EUR_CHF,EUR_GBP,EUR_JPY,EUR_NZD,EUR_USD,GBP_AUD,GBP_CAD,GBP_CHF,GBP_JPY,GBP_NZD,GBP_USD,NZD_CAD,NZD_CHF,NZD_JPY,NZD_USD,USD_CAD,USD_CHF,USD_JPY):
    AUD_CAD = perf(AUD_CAD)
    AUD_CHF = perf(AUD_CHF)
    AUD_JPY = perf(AUD_JPY)
    AUD_NZD = perf(AUD_NZD)
    AUD_USD = perf(AUD_USD)
    CAD_CHF = perf(CAD_CHF)
    CAD_JPY = perf(CAD_JPY)
    CHF_JPY = perf(CHF_JPY)
    EUR_AUD = perf(EUR_AUD)
    EUR_CAD = perf(EUR_CAD)
    EUR_CHF = perf(EUR_CHF)
    EUR_GBP = perf(EUR_GBP)
    EUR_JPY = perf(EUR_JPY)
    EUR_NZD = perf(EUR_NZD)
    EUR_USD = perf(EUR_USD)
    GBP_AUD = perf(GBP_AUD)
    GBP_CAD = perf(GBP_CAD)
    GBP_CHF = perf(GBP_CHF)
    GBP_JPY = perf(GBP_JPY)
    GBP_NZD = perf(GBP_NZD)
    GBP_USD = perf(GBP_USD)
    NZD_CAD = perf(NZD_CAD)
    NZD_CHF = perf(NZD_CHF)
    NZD_JPY = perf(NZD_JPY)
    NZD_USD = perf(NZD_USD)
    USD_CAD = perf(USD_CAD)
    USD_CHF = perf(USD_CHF)
    USD_JPY = perf(USD_JPY)
    
    #Calculating Perfs
    data_AUD_CAD=np.array(AUD_CAD['perf'])
    data_AUD_CHF=np.array(AUD_CHF['perf'])
    data_AUD_JPY=np.array(AUD_JPY['perf'])
    data_AUD_NZD=np.array(AUD_NZD['perf'])
    data_AUD_USD=np.array(AUD_USD['perf'])
    data_CAD_CHF=np.array(CAD_CHF['perf'])
    data_CAD_JPY=np.array(CAD_JPY['perf'])
    data_CHF_JPY=np.array(CHF_JPY['perf'])
    data_EUR_AUD=np.array(EUR_AUD['perf'])
    data_EUR_CAD=np.array(EUR_CAD['perf'])
    data_EUR_CHF=np.array(EUR_CHF['perf'])
    data_EUR_GBP=np.array(EUR_GBP['perf'])
    data_EUR_JPY=np.array(EUR_JPY['perf'])
    data_EUR_NZD=np.array(EUR_NZD['perf'])
    data_EUR_USD=np.array(EUR_USD['perf'])
    data_GBP_AUD=np.array(GBP_AUD['perf'])
    data_GBP_CAD=np.array(GBP_CAD['perf'])
    data_GBP_CHF=np.array(GBP_CHF['perf'])
    data_GBP_JPY=np.array(GBP_JPY['perf'])
    data_GBP_NZD=np.array(GBP_NZD['perf'])
    data_GBP_USD=np.array(GBP_USD['perf'])
    data_NZD_CAD=np.array(NZD_CAD['perf'])
    data_NZD_CHF=np.array(NZD_CHF['perf'])
    data_NZD_JPY=np.array(NZD_JPY['perf'])
    data_NZD_USD=np.array(NZD_USD['perf'])
    data_USD_CAD=np.array(USD_CAD['perf'])
    data_USD_CHF=np.array(USD_CHF['perf'])
    data_USD_JPY=np.array(USD_JPY['perf'])

    return data_AUD_CAD,data_AUD_CHF,data_AUD_JPY,data_AUD_NZD,data_AUD_USD,data_CAD_CHF,data_CAD_JPY,data_CHF_JPY,data_EUR_AUD,data_EUR_CAD,data_EUR_CHF,data_EUR_GBP,data_EUR_JPY,data_EUR_NZD,data_EUR_USD,data_GBP_AUD,data_GBP_CAD,data_GBP_CHF,data_GBP_JPY,data_GBP_NZD,data_GBP_USD,data_NZD_CAD,data_NZD_CHF,data_NZD_JPY,data_NZD_USD,data_USD_CAD,data_USD_CHF,data_USD_JPY
# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
    X, y = list(), list()
    for i in range(len(sequence)):
		# find the end of this pattern
            end_ix = i + n_steps
		# check if we are beyond the sequence
            if end_ix > len(sequence)-1:
                break
        
        #gather input and output parts of the pattern
            
            seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
            X.append(seq_x)
            y.append(seq_y)
            
    return array(X), array(y)

def normalize(X_AUD_CAD,X_AUD_CHF,X_AUD_JPY,X_AUD_NZD,X_AUD_USD,X_CAD_CHF,X_CAD_JPY,X_CHF_JPY,X_EUR_AUD,X_EUR_CAD,X_EUR_CHF,X_EUR_GBP,X_EUR_JPY,X_EUR_NZD,X_EUR_USD,X_GBP_AUD,X_GBP_CAD,X_GBP_CHF,X_GBP_JPY,X_GBP_NZD,X_GBP_USD,X_NZD_CAD,X_NZD_CHF,X_NZD_JPY,X_NZD_USD,X_USD_CAD,X_USD_CHF,X_USD_JPY):
    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler = scaler.fit(X_AUD_CAD)
    X_AUD_CAD = scaler.transform(X_AUD_CAD)

    scaler = scaler.fit(X_AUD_CHF)
    X_AUD_CHF = scaler.transform(X_AUD_CHF)

    scaler = scaler.fit(X_AUD_JPY)
    X_AUD_JPY = scaler.transform(X_AUD_JPY)

    scaler = scaler.fit(X_AUD_NZD)
    X_AUD_NZD = scaler.transform(X_AUD_NZD)

    scaler = scaler.fit(X_AUD_USD)
    X_AUD_USD = scaler.transform(X_AUD_USD)

    scaler = scaler.fit(X_CAD_CHF)
    X_CAD_CHF = scaler.transform(X_CAD_CHF)

    scaler = scaler.fit(X_CAD_JPY)
    X_CAD_JPY = scaler.transform(X_CAD_JPY)

    scaler = scaler.fit(X_CHF_JPY)
    X_CHF_JPY = scaler.transform(X_CHF_JPY)

    scaler = scaler.fit(X_EUR_AUD)
    X_EUR_AUD = scaler.transform(X_EUR_AUD)

    scaler = scaler.fit(X_EUR_CAD)
    X_EUR_CAD = scaler.transform(X_EUR_CAD)

    scaler = scaler.fit(X_EUR_CHF)
    X_EUR_CHF = scaler.transform(X_EUR_CHF)

    scaler = scaler.fit(X_EUR_GBP)
    X_EUR_GBP = scaler.transform(X_EUR_GBP)

    scaler = scaler.fit(X_EUR_JPY)
    X_EUR_JPY = scaler.transform(X_EUR_JPY)

    scaler = scaler.fit(X_EUR_NZD)
    X_EUR_NZD = scaler.transform(X_EUR_NZD)

    scaler = scaler.fit(X_EUR_USD)
    X_EUR_USD = scaler.transform(X_EUR_USD)

    scaler = scaler.fit(X_GBP_AUD)
    X_GBP_AUD = scaler.transform(X_GBP_AUD)

    scaler = scaler.fit(X_GBP_CAD)
    X_GBP_CAD = scaler.transform(X_GBP_CAD)

    scaler = scaler.fit(X_GBP_CHF)
    X_GBP_CHF = scaler.transform(X_GBP_CHF)

    scaler = scaler.fit(X_GBP_JPY)
    X_GBP_JPY = scaler.transform(X_GBP_JPY)

    scaler = scaler.fit(X_GBP_NZD)
    X_GBP_NZD = scaler.transform(X_GBP_NZD)

    scaler = scaler.fit(X_GBP_USD)
    X_GBP_USD = scaler.transform(X_GBP_USD)

    scaler = scaler.fit(X_NZD_CAD)
    X_NZD_CAD = scaler.transform(X_NZD_CAD)

    scaler = scaler.fit(X_NZD_CHF)
    X_NZD_CHF = scaler.transform(X_NZD_CHF)

    scaler = scaler.fit(X_NZD_JPY)
    X_NZD_JPY = scaler.transform(X_NZD_JPY)

    scaler = scaler.fit(X_NZD_USD)
    X_NZD_USD = scaler.transform(X_NZD_USD)

    scaler = scaler.fit(X_USD_CAD)
    X_USD_CAD = scaler.transform(X_USD_CAD)

    scaler = scaler.fit(X_USD_CHF)
    X_USD_CHF = scaler.transform(X_USD_CHF)

    scaler = scaler.fit(X_USD_JPY)
    X_USD_JPY = scaler.transform(X_USD_JPY)

    return X_AUD_CAD,X_AUD_CHF,X_AUD_JPY,X_AUD_NZD,X_AUD_USD,X_CAD_CHF,X_CAD_JPY,X_CHF_JPY,X_EUR_AUD,X_EUR_CAD,X_EUR_CHF,X_EUR_GBP,X_EUR_JPY,X_EUR_NZD,X_EUR_USD,X_GBP_AUD,X_GBP_CAD,X_GBP_CHF,X_GBP_JPY,X_GBP_NZD,X_GBP_USD,X_NZD_CAD,X_NZD_CHF,X_NZD_JPY,X_NZD_USD,X_USD_CAD,X_USD_CHF,X_USD_JPY

