# Copyright (C) 2019 The Raphielscape Company LLC.; Licensed under the Raphielscape Public License, Version 1.d (the "License"); you may not use this file except in compliance with the License.; Modified by @PrajjuS

""" bot module for other small commands. """

import io
import sys
from os import execl
from random import choice
from time import sleep

from bot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from bot.events import register
from bot.utils import time_formatter


@register(outgoing=True, pattern="^.random")
async def randomise(items):
    """ For .random command, get a random item from the list of items. """
    itemo = (items.text[8:]).split(" ")
    if len(itemo) < 2:
        await items.edit(
            "`2 or more items are required! Check .help random for more info.`"
        )
        return
    rand = choice(itemo)
    await items.edit(
        "**Query: **\n`" + items.text[8:] + "`\n**Output: **\n`" + rand + "`"
    )


@register(outgoing=True, pattern="^.sleep ([0-9]+)$")
async def sleepybot(time):
    """ For .sleep command, let the bot snooze for a few second. """
    counter = int(time.pattern_match.group(1))
    await time.edit("`Going For Sleep`")
    if BOTLOG:
        str_counter = time_formatter(counter)
        await time.client.send_message(
            BOTLOG_CHATID,
            f"You put the bot to sleep for {str_counter}.",
        )
    sleep(counter)
    await time.edit("`OK, I'm awake now.`")


@register(outgoing=True, pattern="^.shutdown$")
async def killbot(shut):
    """For .shutdown command, shut the bot down."""
    await shut.edit("`Shutting The Power Off`")
    if BOTLOG:
        await shut.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n" "Bot shut down")
    await bot.disconnect()


@register(outgoing=True, pattern="^.restart$")
async def killdabot(reboot):
    await reboot.edit("`Restarting`")
    if BOTLOG:
        await reboot.client.send_message(BOTLOG_CHATID, "#RESTART \n" "Bot Restarted")
    await bot.disconnect()
    # Spin a new instance of bot
    execl(sys.executable, sys.executable, *sys.argv)
    # Shut the existing one down
    exit()


@register(outgoing=True, pattern="^.readme$")
async def reedme(event):
    await event.edit(
        "Here's something for you to read:\n"
        "\n[Cosmic UB's' README.md file](https://github.com/SkyLab-Devs/Cosmicbot/blob/demon/README.md)"
)


@register(outgoing=True, pattern="^.guide$")
async def guidee(event):
    await event.edit(
        "*Guide on Deploying Cosmicbot*\n"
        "•[Reading Guide](https://frost2k5.github.io/ProjectFizilion)\n"
        "•[Yt Guide](https://youtu.be/tJzmrTq09tA)\n"
)


# Copyright (c) Gegham Zakaryan | 2019
@register(outgoing=True, pattern="^.repeat (.*)")
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(" ", 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.edit(replyText)


@register(outgoing=True, pattern="^.repo$")
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.edit(
        "[Click here](https://github.com/SkyLab-Devs/Cosmicbot) to open Cosmic UB's GitHub Repo."
    )

@register(outgoing=True, pattern="^.deploy$")
async def repo_is_here(wannasee):
    """ For .deploy command, just returns the heroku deploying URL. """
    await wannasee.edit(
        "[Click here](https://heroku.com/deploy?template=https://github.com/SkyLab-Devs/Cosmicbot/tree/starfire) to deploy Cosmic bot on Heroku."
    )

@register(outgoing=True, pattern="^.support$")
async def grup(sapot):
    await sapot.edit("**Channel:** @Cosmicbot\n**Support Group:** @CosmicbotChat")
    
@register(outgoing=True, pattern="^.raw$")
async def raw(rawtext):
    the_real_message = None
    reply_to_id = None
    if rawtext.reply_to_msg_id:
        previous_message = await rawtext.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = rawtext.reply_to_msg_id
    else:
        the_real_message = rawtext.stringify()
        reply_to_id = rawtext.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await rawtext.edit("`Check the bot log for the decoded message data !!`")
        await rawtext.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="`Here's the decoded message data !!`",
        )


CMD_HELP.update(
    {
        "misc": ".random <item1> <item2> ... <itemN>"
"\nUsage: Get a random item from the list of items.\n\n"
".sleep <seconds>"
"\nUsage: hibernate your bot.\n\n"
".shutdown"
"\nUsage: Shutdowns Your Bot.\n\n"
".repo"
"\nUsage: If you are curious what makes the bot work, this is what you need.\n\n"
".readme"
"\nUsage: Provide links to setup the bot and it's modules\nAnd .support for support group\n\n"
".guide"
"\nUsage: Provides Full guide to setup Cosmic bot.\n\n"
".repeat <no.> <text>"
"\nUsage: Repeats the text for a number of times. Don't confuse this with spam tho.\n\n"
".restart"
"\nUsage: Restarts the bot !!\n\n"
".raw"
"\nUsage: Get detailed JSON-like formatted data about replied message."
".deploy"
"\nUsage: Get link to deploy Cosmic bot on Heroku."
     }
)