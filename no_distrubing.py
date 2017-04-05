from wxpy import *
bot = Bot()
# no_disturbing_str = '嘉嘉呼呼中，有急事给我电话哈，做个好梦[Joyful]\nAlexander is asleep, please call him if there is an emergency, have a nice dream Dear[Joyful]'
# no_disturbing_str = '嘉嘉去运动了，有急事的话给我电话哈，[Joyful]\nAlexander is out for exercise, please call me if there is an emergency, Carpe Diem.[Joyful]'
no_disturbing_str = '工作中，稍后回复，有急事请电话联系^_^\nWorking time, catch you later, ping me if there is an emergency.^_^Carpe Diem.'

@bot.register()
def no_disturbing_reply(msg):
    if isinstance(msg.chat, Group) and not msg.is_at:
        print(msg)
    else:
        # 回复消息内容和类型
        return no_disturbing_str

embed()