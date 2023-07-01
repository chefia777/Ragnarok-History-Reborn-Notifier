# **Ragnarok Online History Reborn Private Server Scraper**
This repository contains a Python scraper designed to extract URL data from the "Ragnarok Online History Reborn Private Server" game. The scraper's main functionality is to notify the user whenever an item of a shop chosen by him has been sold, both through the console window and Telegram.

## Requirements
To use the scraper, you need to have the following software and dependencies installed:

**Python 3.x**: The scraper is implemented in Python and requires a Python 3.x version to run.

**requests library**: Used for making HTTP requests to fetch data from the server.

**beautifulsoup4 library**: Used for parsing the HTML and extracting the required information.

**concurrent.futures library**: Used for concurrent execution of tasks.

**time library**: Used for time-related functionality.

**json library**: Used for working with JSON data.

Install the required dependencies using the following command:

```pip install -r requirements.txt```

## Usage

Clone the repository to your local machine:

```git clone https://github.com/chefia777/Ragnarok-History-Reborn-Scraper.git```

Navigate to the project directory:

```cd Ragnarok-History-Reborn-Scraper```

Configure the scraper by editing the Notifier.py file. In this file, you can specify the shop url you want to track. Update the Telegram configuration details in the Telegram.py file to enable Telegram notifications.

Run the scraper:

```python scraper.py```

The scraper will start fetching data from the game's server and checking the selected shop URL. If if an item is sold while the Notifier is running, you will be notified through the console window. If Telegram configuration is correctly set up, you will also receive a notification via Telegram.

## License
This repository is licensed under the MIT License. Feel free to modify and distribute it as per the terms of the license.

## Contributing
Contributions to this repository are always welcome. If you find any issues or want to suggest improvements, please open an issue or submit a pull request. We appreciate your contributions!

## Disclaimer
This scraper is intended for personal use and educational purposes only. Use it responsibly and respect the terms and conditions of the "Ragnarok Online History Reborn Private Server" game. The developers of this scraper are not responsible for any misuse or violation of the game's policies.
