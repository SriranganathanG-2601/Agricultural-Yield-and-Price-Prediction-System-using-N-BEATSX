import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_dummy_data(output_path='data/agri_data.csv'):
    # Setup date range
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2024, 1, 1)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    products = ['Tomato', 'Potato', 'Onion', 'Cabbage']
    markets = ['Market_A', 'Market_B', 'Market_C']
    
    data = []
    
    for product in products:
        for market in markets:
            # Base price
            base_price = np.random.uniform(20, 100)
            
            # Trend component
            trend = np.linspace(0, 20, len(dates))
            
            # Seasonality (yearly)
            seasonality = 10 * np.sin(2 * np.pi * np.arange(len(dates)) / 365)
            
            # Random noise
            noise = np.random.normal(0, 5, len(dates))
            
            prices = base_price + trend + seasonality + noise
            prices = np.maximum(prices, 5) # Ensure no negative prices
            
            for date, price in zip(dates, prices):
                data.append({
                    'date': date,
                    'product': product,
                    'market': market,
                    'price': round(price, 2),
                    'volume': int(np.random.normal(1000, 200))
                })
                
    df = pd.DataFrame(data)
    
    # Ensure data directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    df.to_csv(output_path, index=False)
    print(f"Generated dummy data at {output_path}")

if __name__ == "__main__":
    generate_dummy_data('s:/anti/project/data/agri_data.csv')
