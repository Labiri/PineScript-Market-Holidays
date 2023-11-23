
## Overview
This Python script is designed to retrieve market holiday data for a variety of global stock exchanges and format them into PineScript arrays. These arrays can then be used within TradingView indicators and strategies to account for non-trading days.

## Features
- Retrieves market holiday data for multiple stock exchanges around the globe.
- Formats the holiday data into PineScript arrays.
- Outputs the arrays to a text file for easy integration into TradingView scripts.

## How It Works
The script uses the `pandas_market_calendars` (https://pandas-market-calendars.readthedocs.io) library to directly obtain the non-trading days (holidays) for each specified exchange. Each set of non-trading days is formatted as a PineScript array and saved to an output file.

## Usage
Ensure you have Python installed on your system.

Install the required libraries using pip:
```bash
pip install pandas pandas_market_calendars
```
Run the script:
```bash
python PineScript_MarketHolidays.py
```
Check the output file `market_holidays_pinescript.txt` for the PineScript arrays.

## Exchange Codes
The script includes a comprehensive list of global stock exchange identifiers. For example:
- `XNYS`: New York Stock Exchange, USA
- `XCBF`: CBOE Futures, USA
- `XTSE`: Toronto Stock Exchange, Canada
- `XJPX`: Tokyo Stock Exchange, Japan
- ... and many more.

## Output Format
Each exchange's non-trading days are outputted as a PineScript array with a naming convention of `<EXCHANGE_CODE>_<COUNTRY_CODE>_nonTradingDays`. For example:
```pinescript
// New York Stock Exchange, US
XNYS_US_nonTradingDays = array.from(
    timestamp("2023-01-01T00:00:00"),
    timestamp("2023-07-04T00:00:00"),
    // ... more dates
)
```
### PineScript Library
In addition to this Python script, a complementary PineScript library will be available for further integration and usage within TradingView scripts on my [TradingView profile](https://www.tradingview.com/u/Protervus/#published-scripts).

## Customization
You can customize the list of exchanges by editing the `exchange_codes` array and the `exchange_descriptions` mapping.

## Contribution
Contributions are welcome! If you'd like to add more features or suggest improvements, please feel free to fork this repository and submit a pull request.

## License
This project is open-source and available under the MIT License.
