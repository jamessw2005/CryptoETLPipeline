import requests
import pandas as pd
from datetime import datetime
import os

def run_extraction():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false"
    # url = "https://api.coingecko.com/api/v3/THIS_IS_A_TEST"
    
    headers = {"User-Agent": "ETL-Pipeline-Student-Project"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        parsed_rows = []
        for item in data:
            parsed_rows.append({
                'coin_id': item.get('id'),
                'symbol': str(item.get('symbol')).upper(),
                'coin_name': item.get('name'),
                'current_price': float(item.get('current_price') or 0.0),
                'market_cap': int(item.get('market_cap') or 0),
                'total_volume': int(item.get('total_volume') or 0),
                'price_change_percentage_24h': float(item.get('price_change_percentage_24h') or 0.0),
                'extraction_timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            
        df = pd.DataFrame(parsed_rows)
        
        # Ensure output directory exists
        output_dir = r"C:\ETL_Projects\CryptoPipeline\Staging"
        os.makedirs(output_dir, exist_ok=True)
        
        file_path = os.path.join(output_dir, "crypto_daily_staging.csv")
        df.to_csv(file_path, index=False)
        print(f"Extraction successful. File saved to {file_path}")
    else:
        raise Exception(f"API Failed with status code: {response.status_code}")

if __name__ == "__main__":
    run_extraction()