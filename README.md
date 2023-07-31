# Currency Exchange Program in Python

## Overview

This is a simple currency exchange program implemented in Python. The program allows users to convert an amount of money from one currency to another using real-time exchange rates.

## Features

- User-friendly command-line interface.
- Supports conversion between multiple currencies.
- Utilizes a public API to fetch real-time exchange rates.
- Displays the converted amount with the corresponding currency symbol.
- NEW: identify when the currency don't exist

## How to Use

1. Clone this repository to your local machine.
2. Install the required packages (if not already installed) using the following command:
   ```
   pip install requests
   ```
3. Run the program using the following command:
   ```
   python exchange.py
   ```
4. Follow the on-screen instructions to enter the input currency, output currency, and the amount you want to convert.
5. The program will fetch the latest exchange rate and display the converted amount.

## Dependencies

This program requires the `requests` library to fetch data from the exchange rate API. You can install it using the following command:
```
pip install requests
```

## API Used

The program uses the "exchangerate-api.com" API to get real-time exchange rates for various currencies. The API is free to use and provides accurate and up-to-date exchange rates.

## Note

Please note that the exchange rate API used in this program may have rate limits or usage restrictions. It is recommended to review the API documentation for usage limitations and consider implementing caching mechanisms for frequent use.

Feel free to explore and modify the program to suit your needs. Enjoy exchanging currencies with Python!
