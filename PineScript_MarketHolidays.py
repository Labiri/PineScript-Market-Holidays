import pandas_market_calendars as mcal
import pandas as pd
from datetime import datetime

# Function to format non-trading days for PineScript array
def format_for_pinescript(non_trading_days, exchange_code, country_code):
    print(f"Formatting non-trading days for PineScript.")
    formatted_dates = [f'timestamp("{day.strftime("%Y-%m-%d")}T00:00:00")' for day in sorted(non_trading_days)]
    pine_script_array = f'int[] {exchange_code}_{country_code}_nonTradingDays = array.from(\n     ' + ',\n     '.join(formatted_dates) + '\n )'
    return pine_script_array

def get_market_holidays_formatted(exchange, start_date, end_date, exchange_code, country_code):
    try:
        calendar = mcal.get_calendar(exchange)
        schedule = calendar.schedule(start_date=start_date, end_date=end_date)
        all_weekdays = pd.date_range(start=schedule.index.min(), end=schedule.index.max(), freq='B')
        holidays = all_weekdays.difference(schedule.index)
        return format_for_pinescript(holidays, exchange_code, country_code)
    except Exception as e:
        return f"// Error encountered for {exchange_descriptions[exchange_code][1]}, {country_code}: {e}"


# Define the date range
start_date = '2015-09-01'   # for current time use:  datetime.now().strftime('%Y-%m-%d')
end_date = '2025-12-31'

# Initialize a string to accumulate the formatted arrays
formatted_arrays = ""

# List of exchange codes
exchange_codes = [
    # 'XNYS',  # New York Stock Exchange, USA
    # 'CMES',  # Chicago Mercantile Exchange, USA
    # 'IEPA',  # ICE US, USA
    'XCBF',  # CBOE Futures, USA
    'XTSE',  # Toronto Stock Exchange, Canada
    'BVMF',  # BMF Bovespa, Brazil
    'XLON',  # London Stock Exchange, England
    'XAMS',  # Euronext Amsterdam, Netherlands
    'XBRU',  # Euronext Brussels, Belgium
    'XLIS',  # Euronext Lisbon, Portugal
    'XPAR',  # Euronext Paris, France
    'XFRA',  # Frankfurt Stock Exchange, Germany
    'XSWX',  # SIX Swiss Exchange, Switzerland
    'XTKS',  # Tokyo Stock Exchange, Japan
    'XASX',  # Australialian Securities Exchange, Australia
    'XMAD',  # Bolsa de Madrid, Spain
    'XMIL',  # Borsa Italiana, Italy
    'XNZE',  # New Zealand Exchange, New Zealand
    'XWBO',  # Wiener Borse, Austria
    'XHKG',  # Hong Kong Stock Exchange, Hong Kong
    'XCSE',  # Copenhagen Stock Exchange, Denmark
    'XHEL',  # Helsinki Stock Exchange, Finland
    'XSTO',  # Stockholm Stock Exchange, Sweden
    'XOSL',  # Oslo Stock Exchange, Norway
    'XDUB',  # Irish Stock Exchange, Ireland
    'XBOM',  # Bombay Stock Exchange, India
    'XSES',  # Singapore Exchange, Singapore
    'XSHG',  # Shanghai Stock Exchange, China
    'XKRX',  # Korea Exchange, South Korea
    'XICE',  # Iceland Stock Exchange, Iceland
    'XWAR',  # Poland Stock Exchange, Poland
    #'XSGO',  # Santiago Stock Exchange, Chile (returning an error from lib)
    'XBOG',  # Colombia Securities Exchange, Colombia
    'XMEX',  # Mexican Stock Exchange, Mexico
    'XLIM',  # Lima Stock Exchange, Peru
    'XPRA',  # Prague Stock Exchange, Czech Republic
    'XBUD',  # Budapest Stock Exchange, Hungary
    'ASEX',  # Athens Stock Exchange, Greece
    'XIST',  # Istanbul Stock Exchange, Turkey
    'XJSE',  # Johannesburg Stock Exchange, South Africa
    'XKLS',  # Malaysia Stock Exchange, Malaysia
    'XMOS',  # Moscow Exchange, Russia
    'XPHS',  # Philippine Stock Exchange, Philippines
    'XBKK',  # Stock Exchange of Thailand, Thailand
    'XIDX',  # Indonesia Stock Exchange, Indonesia
    'XTAI',  # Taiwan Stock Exchange Corp., Taiwan
    'XBUE',  # Buenos Aires Stock Exchange, Argentina
    'XKAR',  # Pakistan Stock Exchange, Pakistan
    'XETR',  # Xetra, Germany
    #'XTAE',  # Tel Aviv Stock Exchange, Israel (returning an error from lib)
    'AIXK',  # Astana International Exchange, Kazakhstan
    'XBSE',  # Bucharest Stock Exchange, Romania
    'XSAU',  # Saudi Stock Exchange, Saudi Arabia
]

# Mapping of exchange codes to their countries in ISO 3166-1 alpha-2 format and full names
exchange_descriptions = {
    # 'XNYS': ('US', 'New York Stock Exchange'),
    # 'CMES': ('US', 'Chicago Mercantile Exchange'),
    # 'IEPA': ('US', 'ICE US'),
    'XCBF': ('US', 'CBOE Futures'),
    'XTSE': ('CA', 'Toronto Stock Exchange'),
    'BVMF': ('BR', 'BM&F Bovespa'),
    'XLON': ('GB', 'London Stock Exchange'),
    'XAMS': ('NL', 'Euronext Amsterdam'),
    'XBRU': ('BE', 'Euronext Brussels'),
    'XLIS': ('PT', 'Euronext Lisbon'),
    'XPAR': ('FR', 'Euronext Paris'),
    'XFRA': ('DE', 'Frankfurt Stock Exchange'),
    'XSWX': ('CH', 'SIX Swiss Exchange'),
    'XTKS': ('JP', 'Tokyo Stock Exchange'),
    'XASX': ('AU', 'Australian Securities Exchange'),
    'XMAD': ('ES', 'Bolsa de Madrid'),
    'XMIL': ('IT', 'Borsa Italiana'),
    'XNZE': ('NZ', 'New Zealand Exchange'),
    'XWBO': ('AT', 'Wiener Borse'),
    'XHKG': ('HK', 'Hong Kong Stock Exchange'),
    'XCSE': ('DK', 'Copenhagen Stock Exchange'),
    'XHEL': ('FI', 'Helsinki Stock Exchange'),
    'XSTO': ('SE', 'Stockholm Stock Exchange'),
    'XOSL': ('NO', 'Oslo Stock Exchange'),
    'XDUB': ('IE', 'Irish Stock Exchange'),
    'XBOM': ('IN', 'Bombay Stock Exchange'),
    'XSES': ('SG', 'Singapore Exchange'),
    'XSHG': ('CN', 'Shanghai Stock Exchange'),
    'XKRX': ('KR', 'Korea Exchange'),
    'XICE': ('IS', 'Iceland Stock Exchange'),
    'XWAR': ('PL', 'Warsaw Stock Exchange'),
    #'XSGO': ('CL', 'Santiago Stock Exchange'),  (returning an error from lib)
    'XBOG': ('CO', 'Colombia Securities Exchange'),
    'XMEX': ('MX', 'Mexican Stock Exchange'),
    'XLIM': ('PE', 'Lima Stock Exchange'),
    'XPRA': ('CZ', 'Prague Stock Exchange'),
    'XBUD': ('HU', 'Budapest Stock Exchange'),
    'ASEX': ('GR', 'Athens Stock Exchange'),
    'XIST': ('TR', 'Istanbul Stock Exchange'),
    'XJSE': ('ZA', 'Johannesburg Stock Exchange'),
    'XKLS': ('MY', 'Malaysia Stock Exchange'),
    'XMOS': ('RU', 'Moscow Exchange'),
    'XPHS': ('PH', 'Philippine Stock Exchange'),
    'XBKK': ('TH', 'Stock Exchange of Thailand'),
    'XIDX': ('ID', 'Indonesia Stock Exchange'),
    'XTAI': ('TW', 'Taiwan Stock Exchange Corp.'),
    'XBUE': ('AR', 'Buenos Aires Stock Exchange'),
    'XKAR': ('PK', 'Pakistan Stock Exchange'),
    'XETR': ('DE', 'Xetra'),
    #'XTAE': ('IL', 'Tel Aviv Stock Exchange'), (returning an error from lib)
    'AIXK': ('KZ', 'Astana International Exchange'),
    'XBSE': ('RO', 'Bucharest Stock Exchange'),
    'XSAU': ('SA', 'Saudi Stock Exchange'),
    # Add more exchanges as needed
}

# Loop through each exchange and get the market holidays formatted for PineScript
for exchange_code in exchange_codes:
    country_code, exchange_name = exchange_descriptions[exchange_code]
    result = get_market_holidays_formatted(exchange_code, start_date, end_date, exchange_code, country_code)
    if result.startswith("// Error"):
        formatted_arrays += result + "\n\n"
    else:
        formatted_arrays += f"// {exchange_name}, {country_code}\n{result}\n\n"


# Output the result to a text file
output_file_path = "market_holidays_pinescript.txt"
with open(output_file_path, "w") as file:
    file.write(formatted_arrays)

print(f"Output saved to {output_file_path}")