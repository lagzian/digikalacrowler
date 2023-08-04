# Digikala Website Crawler with Telegram Notification

This GitHub repository contains a Python script that crawls the Digikala website's discount sections to check for specific keywords. When any of the keywords are found, the bot sends a notification message to a Telegram chat.

## How it works

The workflow is scheduled to run every 8 hours using GitHub Actions. The Python script uses the `selenium` library to scrape the Digikala website and `beautifulsoup4` to parse the HTML content. It searches for predefined keywords related to products with discounts.

When the script finds any of the keywords, it sends a message to a Telegram chat using the `python-telegram-bot` library. The Telegram bot token and chat ID are stored as GitHub secrets for security.

## Requirements

- Python 3.x
- `pip` package manager

## Installation and Setup

1. Clone this repository to your local machine:

```bash
git clone https://github.com/lagzian/digikalacrowler.git
cd digikalacrowler

    Install the required Python packages using pip:

bash

pip install -r requirements.txt

    Ensure that you have the Chrome WebDriver installed in the repository root directory. The script uses it for browser automation.

    Set up a Telegram bot by following the instructions in the official Telegram documentation. Obtain the bot token and chat ID.

    Add the bot token and chat ID as secrets to your GitHub repository. Go to Settings > Secrets > New repository secret and add the following secrets:
        TELEGRAM_BOT_TOKEN: The bot token you obtained in step 4.
        TELEGRAM_CHAT_ID: The chat ID to which the bot should send messages.

Usage

The workflow is automatically triggered every 8 hours by GitHub Actions. It will run the Python script to crawl the Digikala website and send a Telegram message if any of the predefined keywords are found.

You can also trigger the workflow manually by going to the Actions tab, selecting the Check Website_telegram workflow, and clicking Run workflow.
Customization

You can customize the keywords list in the Python script (crawler.py) to search for different keywords related to products you are interested in. Modify the list to add or remove keywords according to your preferences.

Additionally, you can adjust the schedule for the workflow by modifying the cron expression in the .github/workflows/main.yml file. The current schedule runs the workflow every 8 hours. Refer to the GitHub Actions documentation for more information on customizing workflows.
License

This project is licensed under the MIT License.

Feel free to contribute to this repository by opening issues or submitting pull requests. Happy coding!

css


Make sure to replace the URLs and other placeholders with actual values, and update the instructions according to your specific setup. This README will give users a clear understanding of your project, how to set it up, and how to use it.
