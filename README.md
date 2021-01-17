# Forex Prediction
The goal of this project is to extract live market data, use it to train a LSTM model in order to predict the next candlestick mouvement and apply the genetic algorithm to choose which are the best-suited parameters for each model.<br />
## Models
Each model takes as an input the candlestick values, during the past 3 months, of 28 different forex pairs such as EUR/USD, EUR/CAD...<br />
We feed the model from data stored in CSV files using Ctrader.<br />
![Ctrader](https://forexclub.pl/wp-content/uploads/2020/01/ctrader-opinie.jpg)<br />
Two pre-trained models (LSTM_AUD.h5 and LSTM_EUR.h5) are available in the "models" folder.<br />
## Dataset
The Dataset is stored in CSV files:<br />
pairs folder contains the training dataset.<br />
validation folder contains tha validation dataset.<br />
## Genetic Algorithm
We used the genetic algorithm in order to define:
1. Which is the best time step for each model (time step is the time between two consecutive candlesticks which can be in our case 1hour, 2hours or 4hours).
1. Which are the forex pairs to neglect as an input (sometimes there are some inputs that should not be considered. An example for that: the Japanese yen (Jpy) has no influence on the canadian dollar (CAD) in this case we should set JPY to 0).
## Code
in order the run the code:

```bash
python main.py
```
