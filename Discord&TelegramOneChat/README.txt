<h1 align="center">Discord & Telegram One Chat</h1>
<h3 align="center">This code was written for its own purposes. I needed to unite two groups of people, from Discord and Telegram, into one community.<h3>

<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/967876932177911878/SmartSelect_20220424-225713_Discord.jpg" alt="From Discord" width="440"></p>

<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/967876932375052408/Screenshot_20220424-212034_Telegram.jpg" alt="From Discord" width="440"></p>

<h1 align="center">Start of work</h1>

1. ### In a terminal or development environment, enter the commands:

- `pip install discord`

- `pip install pyTelegramBotAPI`

- `pip install requests`

And we are waiting for the packages to be installed

2. ### We create bots for Discord and Telegram (If you know how to do it, you can move on to the next step)

#### Create Discord Bot

- We go to the Discord Developer Portal [*klick*](https://discord.com/developers/applications)
- Click on **New Application** and write the name
- In the new window, select the **Bot** section, click on the **Add Bot** button and confirm
- Check the boxes next to all the items in the section **Privileged Gateway Intents**

<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/968180626358419496/2022-04-25_19-03-00.png?width=985&height=424" alt="All Intents" width="440"></p>

- Go to the section **OAuth2** in the item **URL Generator**
- In the **Scopes** field, select **bot**, and in the **Bot Permissions** field that appears, BE sure to set the permissions **Read Messages/View Channels** and **Send Messages**, the rest of the permissions are at your discretion
- By the generated link, we invite the bot to the server

#### Create Telegram Bot

- We enter into a dialogue with the bot `@BotFather`
- If you have never created your Telegram bots, then use the command `/start`
- We use the command `/newbot` and respond to messages

3. ### Additionally, we configure Telegram Bot

- In the dialog with `@BotFather` we use the command `/setprivacy`
- In response to the message, we write the name of the bot that you specified when creating (the name along with `@')
- In response to the message, we write `DISABLE`
- We invite the bot to chat

4. ### Code preparation

- On the Discord Developer Portal website, in the **Bot** section, click the **Reset Token** button, confirm the action, copy the token and paste it into the `DSTOKEN` variable in the source code

<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/968189796126183434/2022-04-25_19-39-58.png" alt="Discord Token" width="440"></p>

- Open a dialog with `@BotFather` and find the message that was sent to you immediately after the bot was created. Take the token from there and paste it into the `TGTOKEN` variable in the source code

<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/968190161328439386/2022-04-25_19-41-18.png" alt="Telegram Token" width="440"></p>

<p align="center">Your code now looks like this 👇</p>
<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/968192232307953706/2022-04-25_19-49-00.png" alt="Your code" width="440"></p>

- In the Discord app settings, open the **Advanced** tab and turn on the switch next to **Developer Mode**
- Copy the ID of your bot (right-click, item **Copy ID**) and paste it into the variable `IDBOTDS`
- Copy the ID of the required channel (right-click, item **Copy ID**) and paste it into the variable `DSCHANNEL`

<p align="center">Now your code looks like this 👇</p>
<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/968195969613189170/2022-04-25_20-04-00.png" alt="Now your code" width="440"></p>

- Running your code as it is now
- In Telegram chat we use the command `/id` and save result
- Stopping the work of the code
- Inserting the chat ID into the `TGGROUP` variable

<p align="center">Ready-made code view 👇</p>
<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/968198119294636062/2022-04-25_20-12-09.png" alt="Ready-made code view" width="440"></p>

5. ### The code is ready and configured, you can use it!