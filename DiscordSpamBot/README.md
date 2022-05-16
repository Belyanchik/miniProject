<h1 align="center">Discord Spam Bot</h1>
<h3 align="center">Sometimes it happens when you communicate in discord, you want to make fun of a friend. It is for these purposes that I developed this code. Its original appearance was used in my other bot`s. Now I have finished it and increased the functional. Have fun!</h3>

##### Navigation:
- [Demonstration](#demo)
- [Start of work](#start)
- [Disclaimer of liability](#disclaimer)

<h1 align="center"><a name="demo"></a>Demonstration</h1>

<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/974940374269304832/2022-05-14_10-44-24.png" alt="Default spam" width="225"></p>

<p align="center">Default spam</p>

<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/974942120399994900/2022-05-14_10-50-13.png" alt="Private message spam" width="225"></p>

<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/974942123986128956/2022-05-14_10-51-27.png" alt="Private message spam" width="225"></p>

<p align="center">Private message spam</p>

<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/974942825097592853/2022-05-14_10-54-21.png" alt="Spam in the selected channel and in private messages" width="225"></p>

<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/974942965388701726/2022-05-14_10-54-49.png" alt="Spam in the selected channel and in private messages" width="225"></p>

<p align="center">Spam in the selected channel and in private messages</p>

<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/974943556475174952/2022-05-14_10-57-15.png" alt="Stop spam" width="225"></p>

<p align="center">Stop spam</p>

> Default number of repetitions is 60, you can set your own number using an optional argument, after `@mention`

<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/974951050098376704/2022-05-14_11-27-05.png" width="225"></p>

<h1 align="center"><a name="start"></a>Start of work</h1>

1. ### In the terminal or development environment, enter the command:

- `pip install discord`

And we are waiting for the packages to be installed

2. ### Creating a discord bot (If you know how to do it, you can move on to the next step)

- We go to the Discord Developer Portal [*klick*](https://discord.com/developers/applications)
- Click on **New Application** and write the name
- In the new window, select the **Bot** section, click on the **Add Bot** button and confirm
- Go to the section **OAuth2** in the item **URL Generator**
- In the **Scopes** field, select **bot**, and in the **Bot Permissions** field that appears, BE sure to set the permissions **Read Messages/View Channels** and **Send Messages**, the rest of the permissions are at your discretion
- By the generated link, we invite the bot to the server

3. ### Code preparation

- On the Discord Developer Portal website, in the **Bot** section, click the **Reset Token** button, confirm the action, copy the token and paste it into the `DSTOKEN` variable in the source code

<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/968189796126183434/2022-04-25_19-39-58.png" alt="Discord Token" width="440"></p>

<p align="center">Your code now looks like this 👇</p>

<p align="center"><img src="https://media.discordapp.net/attachments/967792782297170062/974937460423401472/2022-05-14_10-32-33.png" alt="Your code" width="440"></p>

4. ### The code is ready and configured, you can use it!

<h1 align="center"><a name="disclaimer"></a>Disclaimer of liability</h1>

#### This code was developed solely as a funny joke, do not forget that everyone's humor is different and if it's funny to you, then it may seem offensive to another. Do not forget about the existence of the `!sspam` command, do not force your friends to leave the server or ban you. If the bot was used against you, then you can block it in the user settings. The author does not take responsibility for all actions that will be done by third parties using my open source code!
