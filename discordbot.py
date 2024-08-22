# import asyncio
import os
import random

import discord
from discord import app_commands

# made for this prj
import config
# import consts.const as const
import consts.sysmsg as sysmsg
import make_embed
import util

# init
os.chdir(config.CWD)
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client=client)


# Bot起動時に呼び出される関数
@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")


# TODO:ゲーム開始スラッシュコマンド
@tree.command(name="zirchoco", description="ジルコン版キャット＆チョコレート　ゲームスタート！")
async def mining_zircon(interaction: discord.Interaction):
    if not config.RUNNING_FLAG:
        await interaction.response.send_message(content=sysmsg.NOT_RUNNING)
        return
    # TODO: お題ガチャ {"text":"", "img":"filename"} 形式で返す
    subject = util.choose_subject()
    # TODO: お題を投稿する
    img_subject = discord.File(
        fp=f"{config.CWD}/assets/{subject['img']}.png",
        filename=f"{subject['img']}.png"
    )
    sub_embed = make_embed.subject_embed(subject)
    await interaction.response.defer(thinking=True, ephemeral=False)
    await interaction.followup.send(embed=sub_embed, file=img_subject, ephemeral=False)

    # お題解決に使用する手札を１～３枚で決める
    hand_num = 2#random.randint(1,3)
    # TODO: hand_num枚数だけ手札をガチャする [{"nth":n, "text":"", "img":None}] 形式で返す
    hand_list = util.choose_hand(hand_num)
    # TODO: 手札を投稿する
    imgs_hand = []
    for n in range(hand_num):
        print(f"nth:{n}")
        imgs_hand.append(
            discord.File(
                fp=f"{config.CWD}/assets/{hand_list[n]['img']}.png",
                filename=f"{hand_list[n]['img']}.png"
            )
        )
    print(f"length:{len(imgs_hand)}")
    hand_embeds = make_embed.hand_embeds(hand_list)
    await interaction.followup.send(embeds=hand_embeds, files=imgs_hand, ephemeral=False)


### 以下は運営コマンド


# TODO:ゲーム稼働停止コマンド, 権限はサーバー側で運営チャンネルのみに設定
@tree.command(name="stopzcc", description="ジルチョコSTOP")
async def stop_game(interaction: discord.Interaction):
    config.RUNNING_FLAG = False
    await interaction.response.send_message(content="STOP", ephemeral=True)
    return


# TODO:ゲーム稼働再開コマンド, 権限はサーバー側で運営チャンネルのみに設定
@tree.command(name="startzcc", description="ジルチョコSTART")
async def start_game(interaction: discord.Interaction):
    config.RUNNING_FLAG = True
    await interaction.response.send_message(content="START", ephemeral=True)
    return


# Bot起動
client.run(config.DISCORD_TOKEN)
