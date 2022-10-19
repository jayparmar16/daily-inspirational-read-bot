A telegram bot which sends daily inspiration stories mined from http://www.dailytenminutes.com/p/short-stories.html using BeautifulSoup.

### gettingStories.py
Python script to mine all the links from the site and clean them and therefore store it in CSV file with default value of 0 to show if it has been read or not.

### story.py
Python script to get the story link from CSV file and changing value to 1 for that particular story. 
Using BS4 for that link and mining the story and therefore cleaning it.

### storyNotebook.ipynb
ipynb notebook with all the code for testing purpose

For creating a bot, please refer to [https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot](https://sendpulse.com/knowledge-base/chatbot/telegram/create-telegram-chatbot)
For sending messages, I have used telegram library in Python.
I created a bot named MotivationalBot and the script is ran on Digital Ocean server with the help of Cron.
