import cryptocompare
import pandas as pd
import pyttsx3
from datetime import datetime

def crypto_analysis_assistant():
    # Text-to-speech setup for Windows (pyttsx3)
    def speak_windows(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    # Function to get cryptocurrency price
    def get_crypto_price(symbol, currency='USD'):
        price = cryptocompare.get_price(symbol, currency=currency)
        return price[symbol][currency]

    # Function to calculate simple moving average for cryptocurrency
    def calculate_crypto_sma(data, window):
        return data.rolling(window=window).mean()

    # Function to calculate exponential moving average for cryptocurrency
    def calculate_crypto_ema(data, window):
        return data.ewm(span=window, adjust=False).mean()

    # List of available cryptocurrency symbols
    crypto_symbols = ['BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'ADA', 'DOT', 'LINK', 'XLM', 'DOGE']

    # User Input
    speak_windows("Welcome to the Cryptocurrency Analysis Assistant. Please select a cryptocurrency from the list.")
    speak_windows(f"Available cryptocurrencies: {', '.join(crypto_symbols)}")
    selected_crypto = input('Select Cryptocurrency: ').upper()

    # Validate user input
    while selected_crypto not in crypto_symbols:
        speak_windows("Invalid cryptocurrency. Please select a valid cryptocurrency from the list.")
        selected_crypto = input('Select Cryptocurrency: ').upper()

    # Fetch Cryptocurrency Data
    crypto_data = cryptocompare.get_historical_price_day(selected_crypto, currency='USD', limit=365)

    # Convert data to DataFrame
    crypto_df = pd.DataFrame(crypto_data)
    crypto_df['time'] = pd.to_datetime(crypto_df['time'], unit='s')
    crypto_df.set_index('time', inplace=True)

    # Display Cryptocurrency Price
    current_price = get_crypto_price(selected_crypto)
    print(f"Current {selected_crypto} Price: ${current_price:.2f}")

    # Display Historical Data
    print('\nHistorical Data:')
    print(crypto_df.tail(10))

    # Technical Indicators
    print("SMA (Simple Moving Average): Averages closing prices over a specified window to smooth price trends.")
    sma_window = int(input('Select SMA Window (e.g., 10): '))
    crypto_df['SMA'] = calculate_crypto_sma(crypto_df['close'], sma_window)
    print('\nTechnical Indicators:')
    print(crypto_df[['close', 'SMA']])

    print("EMA (Exponential Moving Average): Gives more weight to recent prices, reacting faster to price changes.")
    ema_window = int(input('Select EMA Window (e.g., 10): '))
    crypto_df['EMA'] = calculate_crypto_ema(crypto_df['close'], ema_window)
    print(crypto_df[['close', 'EMA']])

    # Ask user if they want a report
    speak_windows("Do you want to generate a report? (yes/no)")
    print("Do you want to generate a report? (yes/no)")
    user_input_report = input().lower()

    if user_input_report == 'yes':
        # Generate HTML report
        report_date = datetime.now().strftime("%Y%m%d")
        report_filename = f"crypto_report_{selected_crypto}_{report_date}.html"

        # Apply styling to the HTML report
        styled_report = crypto_df.style \
            .bar(subset=['close'], color='#d65f5f', vmin=crypto_df['close'].min(), vmax=crypto_df['close'].max()) \
            .background_gradient(subset=['SMA', 'EMA'], cmap='viridis') \
            .set_table_styles([
                {'selector': 'th', 'props': [('background-color', '#2c3e50'), ('color', 'white')]},
                {'selector': 'td', 'props': [('border', '1px solid #dddddd')]},
                {'selector': 'tr:hover', 'props': [('background-color', '#f5f5f5')]}
            ])

        # Save the styled DataFrame to an HTML file
        styled_report.to_html(report_filename, render_links=True, escape=False, classes='table table-striped table-hover')

        speak_windows(f"HTML report generated successfully. Report saved as {report_filename}.")
    else:
        speak_windows("Program closed.")

# Call the function to execute the cryptocurrency analysis assistant
# crypto_analysis_assistant()
