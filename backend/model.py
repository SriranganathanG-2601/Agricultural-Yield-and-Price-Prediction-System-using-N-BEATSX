import pandas as pd
import numpy as np
from neuralforecast import NeuralForecast
from neuralforecast.models import NBEATSx
from neuralforecast.losses.pytorch import MAE, MSE, MAPE
import os

class PriceForecaster:
    def __init__(self, horizon=30):
        self.horizon = horizon
        self.models = [
            NBEATSx(input_size=2*horizon, h=horizon, max_steps=100, scaler_type='standard')
        ]
        self.nf = NeuralForecast(models=self.models, freq='D')
        self.trained = False

    def preprocess(self, df):
        # NeuralForecast expects columns: unique_id, ds, y
        # We'll combine product and market as unique_id
        df['unique_id'] = df['product'] + '_' + df['market']
        df['ds'] = pd.to_datetime(df['date'])
        df['y'] = df['price']
        return df[['unique_id', 'ds', 'y']]

    def train(self, df):
        print("Preprocessing data...")
        enc_df = self.preprocess(df)
        print("Training NBEATS-X model...")
        self.nf.fit(df=enc_df)
        self.trained = True
        print("Training complete.")

    def predict(self, df=None):
        if not self.trained:
            raise Exception("Model not trained yet.")
        
        # NeuralForecast predict uses the internal dataset if not provided, 
        # but robust usage often implies passing the historical df again or just calling predict()
        # if using the fitted state.
        forecast_df = self.nf.predict()
        return forecast_df

    def evaluate(self, df):
         # Cross validation for metrics
        if not self.trained:
             raise Exception("Model not trained.")
        
        enc_df = self.preprocess(df)
        cv_df = self.nf.cross_validation(df=enc_df, n_windows=1, step_size=self.horizon)
        
        # Calculate metrics
        y_true = cv_df['y']
        y_pred = cv_df['NBEATSx']
        
        rmse = np.sqrt(np.mean((y_true - y_pred)**2))
        mae = np.mean(np.abs(y_true - y_pred))
        mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
        
        return {
            'RMSE': round(rmse, 4),
            'MAE': round(mae, 4),
            'MAPE': round(mape, 4)
        }

    def save(self, path='model_checkpoint'):
        self.nf.save(path=path, overwrite=True)

    def load(self, path='model_checkpoint'):
        self.nf = NeuralForecast.load(path)
        self.trained = True
