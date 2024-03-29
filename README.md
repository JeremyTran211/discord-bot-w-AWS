# Waste Management Discord Bot

## Project Overview
The Waste Management Discord Bot is an innovative tool designed to streamline interactions within waste management systems. Hosted on Replit and integrated with Amazon RDS using MySQL, it allows Discord users to interact with the bot using specific commands, facilitating quick access to waste management operations and information.

## Features
- **Command Interaction**: Engage with the bot through commands like `!GetCategory category1` to obtain data related to waste management.
- **MySQL Database Integration**: Utilizes Amazon RDS for a robust and scalable backend storage solution.
- **Automated Responses**: Instantly replies to user inquiries with detailed information about various waste management categories.

## Commands
Here are some of the commands you can use with the bot:
- `!GetCategory [categoryName]`: Fetches and displays information about the specified waste management category.
- `!FindService <service provider> <location>`: Retrieves information about the specified service provider in the given location. 
- `!GetRecord <Service> <Generator>`: Gets the average cost between the specified generator and service providers.
- `!RegulatoryBody <Body Name>`: Checks a regulatory body for regulations and retrieves information.
- `!AddWaste <Category> <description> <amount> <item> <item_desc> <amount_item> <generator>`: Adds waste to a specified category or item with the given amount and generator.
- `!AddSchedule "<Title>" "<Description>" "<AccountID>"`: Creates a new collection schedule with a title, description, and account ID.
- `!UpdateService <Service Provider> <Column> <Info>`: Updates information for a specified service provider.
- `!UpdateProcess <Process name> <Column> "<Description>"`: Updates information for a specified process.
- `!DeleteProvider <Table> <Name>`: Deletes a specified provider.
- `!DeleteTech <Technology Name>`: Deletes a specified waste technology and sets processes that utilize the tech to NULL.
- `!UpdateLog <Log_ID> <Column> "<new description>"`: Updates anything in the logs, which automatically updates the time of the log.
- `!GetQuarterSummary`: Retrieves a quarterly summary of waste management data.
- `!GetAvg <generator> <Waste Category>`: Retrieves the average waste produced by a specified generator within a focus category.
- `!FindCommon <Waste Type>`: Finds the most common waste type or waste management site.

## Installation
To set up and run the bot, follow these steps. Make sure you have Node.js and npm installed.

```bash
# Clone the repository
git clone <repository-url>

# Navigate to the bot directory
cd waste-management-discord-bot

# Install dependencies
npm install

# Run the bot
node bot.js
