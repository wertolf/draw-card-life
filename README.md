# 抽卡人生

这是一款用 Python 的 pygame 库编写的点击类 rogue-like 模拟经营游戏，是我在初学 Python 时的一部练手作品。

游戏的玩法基本上直接照搬了用 Unity 引擎开发的[同名原作](#关于原作)，没有太多新意。

## 开始游戏（Windows平台）

你需要安装最新版本的[ Python 解释器](https://www.python.org/downloads/)和[ pygame 第三方库](https://www.pygame.org/wiki/GettingStarted#Pygame%20Installation)。

安装完成后，只需要打开命令行，输入
```
python main.py
```
即可进入游戏界面。

你可以在游戏过程中随时按`Esc`键退出。

### 调整分辨率

由于当初设计时的失误，本游戏窗口的默认大小是 $960 \times 960$，不符合主流的屏幕分辨率。一个临时的解决方案是，在命令行传入自定义的分辨率：
```
python main.py 1280*720
```

> [!NOTE]
> * 传入的分辨率必须满足 $16:9$ 的关系
> * 即使通过这种方式更改分辨率，各组件的位置关系也可能出现重叠的情况

## 项目结构

待填充

## 关于原作

* [抽卡人生 | 中国独立游戏 | Indienova 独立游戏](https://indienova.com/g/drawcardlife)
* [抽卡人生 Android 版](https://www.taptap.cn/app/35686)
