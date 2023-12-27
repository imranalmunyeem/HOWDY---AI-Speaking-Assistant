import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import pyttsx3

def stock_analysis_app():
    # Text-to-speech setup for Windows (pyttsx3)
    def speak_windows(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    # Function to get stock price
    def get_stock_price(ticker):
        return yf.Ticker(ticker).history(period='1d').iloc[-1].Close

    # Function to calculate simple moving average
    def calculate_sma(data, window):
        return data.rolling(window=window).mean()

    # Function to calculate exponential moving average
    def calculate_ema(data, window):
        return data.ewm(span=window, adjust=False).mean()

    # Function to calculate relative strength index (RSI)
    def calculate_rsi(data, window):
        delta = data.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=window).mean()
        avg_loss = loss.rolling(window=window).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    # Function to analyze sentiment
    def analyze_sentiment(ticker):
        return 0.2  # Placeholder, replace with your sentiment analysis logic

    # Function to recommend investment
    def recommend_investment(rsi, sentiment_score):
        if rsi < 30 and sentiment_score > 0:
            return "Buy"
        elif rsi > 70 and sentiment_score < 0:
            return "Sell"
        else:
            return "Hold"

    # Function to suggest investment amount
    def suggest_investment_amount(current_price, risk_percentage):
        return current_price * risk_percentage / 100

    # Function to calculate win and loss probability
    def calculate_win_loss_probability(sentiment_score):
        win_probability = max(0, min(1, (sentiment_score + 1) / 2))
        loss_probability = 1 - win_probability
        return win_probability, loss_probability

    # Function to calculate Sharpe ratio
    def calculate_sharpe_ratio(data, risk_free_rate=0.02):
        returns = data.pct_change().dropna()
        excess_returns = returns - risk_free_rate
        sharpe_ratio = (excess_returns.mean() / excess_returns.std()) * np.sqrt(252)
        return sharpe_ratio

    # Function to calculate Sortino ratio
    def calculate_sortino_ratio(data, risk_free_rate=0.02):
        returns = data.pct_change().dropna()
        downside_returns = returns[returns < 0]
        sortino_ratio = (returns.mean() - risk_free_rate) / downside_returns.std()
        return sortino_ratio

    # Function to calculate Maximum Drawdown
    def calculate_max_drawdown(data):
        cum_returns = (1 + data.pct_change()).cumprod()
        peak = cum_returns.expanding(min_periods=1).max()
        drawdown = (cum_returns - peak) / peak
        max_drawdown = drawdown.min()
        return max_drawdown

    # Function to suggest investment based on financial condition
    def suggest_investment_based_on_financial_condition(financial_condition):
        if financial_condition == "Excellent":
            return "Based on your excellent financial condition, we suggest investing in well-established companies with a low-risk profile."
        elif financial_condition == "Moderate":
            return "Based on your moderate financial condition, consider a diversified portfolio with a mix of growth and value stocks."
        elif financial_condition == "Poor":
            return "Considering your financial condition, focus on risk management and consider conservative investment strategies."

    # List of available stock tickers
    stock_tickers = ['AAPL', 'META', 'GOOGL', 'MSFT', 'X', 'IBM', 'AMZN', 'TSLA', 'GOOGL', 'NFLX', 'BABA', 'JNJ', 'PG', 'JPM', 'GS', 'DIS', 'CSCO', 'GE']

    # User Input
    speak_windows("Sure. Launching the Stock Analysis App. Please select a stock ticker from the list.")
    speak_windows(f"Available tickers: {', '.join(stock_tickers)}")
    selected_ticker = input('Select Stock Ticker: ').upper()

    # Validate user input
    while selected_ticker not in stock_tickers:
        speak_windows("Invalid ticker. Please select a valid ticker from the list.")
        selected_ticker = input('Select Stock Ticker: ').upper()

    # Historical Data
    historical_data = yf.Ticker(selected_ticker).history(period='5y')

    # Display Stock Price
    current_price = get_stock_price(selected_ticker)
    print(f"Current Stock Price ({selected_ticker}): ${current_price}")

    # Display Data Duration
    print(f"Data Duration: {historical_data.index[0].strftime('%Y-%m-%d')} to {historical_data.index[-1].strftime('%Y-%m-%d')}")

    # Display Historical Data
    print('\nHistorical Data:')
    print(historical_data.tail(10))

    # Technical Indicators
    print("SMA (Simple Moving Average): Averages closing prices over a specified window to smooth price trends.")
    sma_window = int(input('Select SMA Window (e.g., 10): '))
    historical_data['SMA'] = calculate_sma(historical_data['Close'], sma_window)
    print('\nTechnical Indicators:')
    print(historical_data[['Close', 'SMA']])

    print("EMA (Exponential Moving Average): Gives more weight to recent prices, reacting faster to price changes.")
    ema_window = int(input('Select EMA Window (e.g., 10): '))
    historical_data['EMA'] = calculate_ema(historical_data['Close'], ema_window)
    print(historical_data[['Close', 'EMA']])

    print("RSI (Relative Strength Index): Measures the speed and change of price movements, indicating overbought or oversold conditions.")
    rsi_window = int(input('Select RSI Window (e.g., 14): '))
    historical_data['RSI'] = calculate_rsi(historical_data['Close'], rsi_window)
    print(historical_data['RSI'])

    # Sentiment Analysis
    sentiment_score = analyze_sentiment(selected_ticker)
    print(f"\nAverage Sentiment Score for {selected_ticker}: {sentiment_score:.2f}")

    # Investment Recommendations
    investment_recommendation = recommend_investment(historical_data['RSI'].iloc[-1], sentiment_score)
    print(f"Recommendation: {investment_recommendation}")

    # Suggested Investment Amount
    risk_percentage = float(input('Select Risk Percentage (e.g., 5): '))
    investment_amount = suggest_investment_amount(current_price, risk_percentage)
    print(f"Suggested Investment Amount: ${investment_amount:.2f}")

    # Win and Loss Probability
    win_probability, loss_probability = calculate_win_loss_probability(sentiment_score)
    print(f"\nWin Probability: {win_probability:.2%}")
    print(f"Loss Probability: {loss_probability:.2%}")

    # Performance Metrics
    sharpe_ratio = calculate_sharpe_ratio(historical_data['Close'])
    sortino_ratio = calculate_sortino_ratio(historical_data['Close'])
    max_drawdown = calculate_max_drawdown(historical_data['Close'])
    print(f"\nPerformance Metrics:")
    print(f"Sharpe Ratio: {sharpe_ratio:.4f}")
    print(f"Sortino Ratio: {sortino_ratio:.4f}")
    print(f"Maximum Drawdown: {max_drawdown:.2%}")

    # Financial Condition Input
    financial_condition = input('Select Your Financial Condition (e.g., Excellent, Moderate, Poor): ')

    # Suggest Investment Based on Financial Condition
    investment_suggestion = suggest_investment_based_on_financial_condition(financial_condition)
    print(f"Investment Suggestion: {investment_suggestion}")

    # Ask user if they want a report
    speak_windows("Do you want to generate a report? (yes/no)")
    print("Do you want to generate a report? (yes/no)")
    user_input_report = input().lower()

    if user_input_report == 'yes':
        # Generate HTML report
        report_date = datetime.now().strftime("%Y%m%d")
        report_filename = f"financial_report_{selected_ticker}_{report_date}.html"

        # Create a DataFrame for the report
        report_data = pd.DataFrame({
            'Date': historical_data.index,
            'Close': historical_data['Close'],
            'SMA': historical_data['SMA'],
            'EMA': historical_data['EMA'],
            'RSI': historical_data['RSI'],
        })

        # Apply styling to the HTML report
        styled_report = report_data.style \
            .bar(subset=['RSI'], color='#d65f5f', vmin=0, vmax=100) \
            .background_gradient(subset=['Close', 'SMA', 'EMA'], cmap='viridis') \
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

# Call the function to execute the stock analysis app
# stock_analysis_app()
