from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Aku mau nimbrung**")


@register(outgoing=True, pattern='^.jelek(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Lo jelek☑️**")
    await typew.edit("**Lo jelek✅**")
    sleep(1)
    await typew.edit("**Lo tetep jelek☑️**")
    await typew.edit("**Lo tetep jelek✅**")
    sleep(2)
    await typew.edit("**Lo masih jelek☑️**")
    await typew.edit("**Lo masih jelek✅**")
    sleep(1)
    await typew.edit("**Lo super jelek☑️**")
    await typew.edit("**Lo super jelek✅**")
    sleep(1)
    await typew.edit("**Emang dasarnya lo jelek,Jangan dicakep-cakepin kontol**")


# Create by myself @localheart

CMD_HELP.update({
    "stres":
    "`.stres`\
    \nUsage: alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.rama`\
    \nUsage: coba aja.\
    \n\n`kosong`\
    \nUsage: tunggu update selanjutnya.\
    \n\n`kosong`\
    \nUsage: tunggu update selanjutnya."
})
