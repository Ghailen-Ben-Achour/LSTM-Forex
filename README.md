# Forex Prediction
The goal of this project is to extract live market data, use it to train a LSTM model in order to predict the next candlestick mouvement and apply the genetic algorithm in order to choose which are the best-suited parameters for each model.<br />
## Models
Each model takes as an input the candlestick values, during the past 3 months, of 28 different forex pairs such as EUR/USD, EUR/CAD...<br />
We feed the model from data stored in CSV files using Ctrader.<br />
![Ctrader](https://www.google.com/search?q=ctrader&sxsrf=ALeKk00ZuA2MmS72m5P1-6nENBpOT21JDw:1610911371734&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiDnc7A2KPuAhUOwKQKHX_-CCMQ_AUoAXoECBUQAw&biw=1517&bih=730#imgrc=G5sqdVV86r-PLM)
