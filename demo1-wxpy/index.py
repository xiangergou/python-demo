

import os
import math
from wxpy import *
from PIL import Image

def creat_filepath():
  avatar_dir = os.getcwd() + "/wechat/"
  if not os.path.exists(avatar_dir):
    os.mkdir(avatar_dir)
  return avatar_dir

def save_avatar(avatar_dir):
  # 机器人 Bot 对象可被理解为一个 Web 微信客户端。
  bot = Bot()
  # 参数:	update – 是否更新
  # 返回:	聊天对象合集
  # 返回类型:	wxpy.Chats
  friends = bot.friends(update=True)

  # 下载好友头像
  num = 0
  for friend in friends:
    friend.get_avatar(avatar_dir + '/' + str(num) + ".jpg")
    print('好友昵称:%s' % friend.nick_name)
    num = num + 1

def joint_avatar(path):
  # 获取文件夹内头像个数
  length = len(os.listdir(path))

  # 设置画布大小
  image_size = 2560
  # 设置每个头像大小
  each_size = math.ceil(image_size / math.floor(math.sqrt(length)))
  # 计算所需各行列的头像数量
  x_lines = math.ceil(math.sqrt(length))
  y_lines = math.ceil(math.sqrt(length))

  # >> > im = Image.new("RGB", (128, 128), "red")
  # 图像im为128x128大小的黑色图像，因为变量color不赋值的话，图像内容被设置为0，即黑色。
  image = Image.new('RGB', (each_size * x_lines, each_size * y_lines))
  x = 0
  y = 0

  # os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
  # top - - 是你所要遍历的目录的地址, 返回的是一个三元组(root, dirs, files)。
  # root 所指的是当前正在遍历的这个文件夹的本身的地址
  # dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
  # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)

  # topdown - -可选，为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为开启)。如果 topdown 参数为 True，walk 会遍历top文件夹，与top 文件夹中每一个子目录。
  for (root, dirs, files) in os.walk(path):
      for pic_name in files:
          # 增加头像读取不出来的异常处理
              try:
                  with Image.open(path + pic_name) as img:
                      print(path + pic_name, 'path + pic_name')
                      img = img.resize((each_size, each_size))
                      image.paste(img, (x * each_size, y * each_size))
                      x += 1
                      if x == x_lines:
                          x = 0
                          y += 1
              except IOError:
                  print(IOError, pic_name)

  img = image.save(os.getcwd() + "/wechat.png")
  print('微信好友头像拼接完成!')

avatar_dir = creat_filepath()
save_avatar(avatar_dir)
joint_avatar(avatar_dir)
