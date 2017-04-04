from wxpy import *
bot = Bot()
carol = ensure_one(bot.search('冰宝'))
tuling = Tuling(api_key='9e416e00b25145b6a1d293aacca77c5f')

# 使用图灵机器人自动与指定好友聊天
@bot.register(carol)
def reply_my_friend(msg):
    tuling.do_reply(msg)
    
embed()
