# Discord-bot
Discord bot using python

A discord bot called 'Encourage bot' will perform the following in discord when added to a discord server.

- On coming across any word from ["sad","depressed","unhappy","angry","miserable","depressing","suffocating"] the bot is triggered into responding with a random encouragement.</br>
- $inspire - Will display a random quote from the zenquote.com API.</br>
- $new [ quote ] - Will add a new quote to the list of encouragements.</br>
- $del [index] - Deletes an encouragement at the given index.</br>
- $list -  Lists all the encouragements from the list of encouragements.</br>
- $responding false - Stops the bot from responding.</br>
- $responding true - Starts the bot and allows it to respond when it comes across the words from the list.</br></br>

**Flask webserver** service is used to keep the bot running in the background.</br>
UptimeRobot.com is used to ping the http address of the bot code every 5 mins.</br>
[Refer to discord developer documentation for more details]
