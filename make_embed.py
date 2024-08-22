import discord


# 採掘演出のembed (中味はgifのみ)
def subject_embed(subject):
    embed = discord.Embed(title="", description="", color=0x00FF00)
    embed.add_field(name="", value=f"{subject['text']}")
    embed.set_image(url=f"attachment://{subject['img']}.png")
    return embed


# 採掘結果Excellentを雑談チャネルに投稿するときのembed
def hand_embeds(hand_list):
    embeds = []
    for n in range(len(hand_list)):
        print(f"idx:{n}")
        embed = discord.Embed(title="", description="", color=0x00FF00)
        embed.add_field(name=f"{hand_list[n]['nth']}", value=f"{hand_list[n]['text']}", inline=False)
        embed.set_image(url=f"attachment://{hand_list[n]['img']}.png")
        embeds.append(embed)
    return embeds
