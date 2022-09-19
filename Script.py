class script(object):
    START_TXT = """
𝑯𝒆𝒚 👋 <i>{}</i> 😍

ഞാൻ ഒരു 𝐆𝐑𝐎𝐔𝐏 𝐌𝐀𝐍𝐀𝐆𝐈𝐍𝐆 𝐁𝐎𝐓 ആണ്, എന്നെ നിങ്ങളുടെ ഗ്രൂപ്പിൽ ആഡ് ചെയ്യാൻ നോക്കി സമയം കളയണ്ട, എന്നെ 𝙈𝘼𝙇𝙇𝙐 𝙏𝘼𝙇𝙆𝙄𝙀𝙎 ഗ്രൂപ്പിൽ മാത്രമേ ആഡ് ചെയ്യാൻ കഴിയൂ...!!!"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://github.com/EvamariaTG/EvaMaria  

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    CAPTION_TXT = """
<b>╔═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
♻️ 𝙅𝙊𝙄𝙉 :- @Mallu_Talkies
♻️ 𝙅𝙊𝙄𝙉 :- @MT_Links
♻️ 𝙅𝙊𝙄𝙉 :- @MalluTalkiesGroup
♻️ 𝙅𝙊𝙄𝙉 :- @MB_ChatGrp
╚═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝</b>
"""
    FSUB_TXT = """
 **നിങ്ങൾ ആവിശ്യപ്പെട്ട സിനിമ ലഭിക്കുന്നതായി, നിങ്ങൾ ഞങ്ങളുടെ ****@Mallu_Talkies**** 🎥' ചാനലിൽ ജോയിൻ ചെയ്യണം.

ജോയിൻ ചെയ്ത ശേഷം ' 🔁 REFRESH 🔁 'ബട്ടൺ ക്ലിക്ക് ചെയ്യൂ** 
"""
    SPELL_CHECK_TXT = "<b>{}📃 നിങ്ങൾ ടൈപ്  ചെയ്ത് സ്പെല്ലിങ് ചിലപ്പോൾ തെറ്റായിരിക്കാം  സ്പെല്ലിങ് ഗൂഗിളിൽ നോക്കി ടൈപ്യ്യു ചെയ്യുക ⌨ ◁━━━━◈✙◈━━━━▷ ശരിയായ സ്പെല്ലിങ് അടിച്ചിട്ടും  മൂവി വന്നില്ലെങ്കിൽ  DVD OTT റിലീസ് ആയിട്ടുണ്ടാകില്ല... 🎭 തിയേറ്റർ പ്രിന്റ് കിട്ടില്ല , HD മൂവീസ് മാത്രം..!!!</b>"
    ACTION_RESTRICTED_TXT = """⚠️ ബ്രോ, മറ്റുള്ളവർ റിക്വസ്റ്റ് ചെയിത മൂവിയിൽ കുത്തി നോക്കാതെ ബ്രോന് വേണ്ടത് ബ്രോ റിക്വസ്റ്റ് ചെയ്യുക.

⚠️Bro, Search Your Own File, Don't Click Others Requested Files.
"""

