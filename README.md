# 抽卡人生

这是一款用 Python 的 `pygame` 库编写的点击类 rogue-like 模拟经营游戏。

游戏的玩法基本上直接照搬了用 Unity 引擎开发的[同名原作](#关于原作)，并且复现得并不完整。

## 开始游戏（Windows平台）

你需要安装最新版本的 [Python 解释器](https://www.python.org/downloads/)和 [`pygame` 第三方库](https://www.pygame.org/wiki/GettingStarted#Pygame%20Installation)。

安装完成后，只需要打开命令行，输入
```
python main.py
```
即可进入游戏界面。

你可以在游戏过程中随时按 `Esc` 键退出。如果无法退出，可以在命令行界面按 `Ctrl` 加 `C` 键发送键盘中断。

### 调整分辨率

由于当初设计时的失误，本游戏窗口的默认大小是 $960 \times 960$，不符合主流的屏幕分辨率。可以通过命令行传入自定义的分辨率：
```
python main.py 1280*720
```

> [!NOTE]
> * 传入的分辨率必须满足 $16:9$ 的关系
> * 推荐使用 `1280*720` 的分辨率，因为我在整理代码、调整布局时是按照这个分辨率做的

## 项目结构

* `main.py` - 入口点
* `Modules` - 项目主体代码

## 关于本作开发的一些回忆

这是我在大二下学期（2019年）利用课余时间完成的一个 Python 练手项目。

我在 gitee 上面保存了一个[重构前的仓库](https://gitee.com/chiyq2000/draw-card-life)，里面包含一定的早期开发记录。然而，那里面的记录也并不完整，因为最初开发这款游戏时，我对于 `git` 和 GitHub 并不了解。

大约两年后，也就是2021年，我基于自己对 Python 编程以及 UI 设计的进一步理解又开发了一款[背单词软件](https://github.com/wertolf/vocabulary-builder)。不过，当年的我毕竟是业余选手，也许其中所体现出的进步与两年的时间并不相应。而且，即便如此，这件事情也牵涉了我当时做其他事的精力。今天决定把自己过去的作品放在这里，一方面时为了丰富自己的简历，另一方面也是想以一种 historical 和 critical 的 perspective 记录这段过往，并从中总结一些经验与教训。

## 一些经验教训的总结

* 少用全局变量，否则会大大降低代码的可重用性
  * 想要用这个框架开发别的游戏，几乎完全不可能
  * 后来开发的[背单词软件](https://github.com/wertolf/vocabulary-builder)在代码的可重用性和可维护性上有了一定的进步，不过同业界的 UI 开发框架仍然存在巨大的差距
* 良好的设计需要将应用程序 system-dependent 的部分与 system-independent 的部分区分开来，以便于将其移植到其他平台
* 如果要进行面向对象相关的开发，学习有关设计模式的知识很重要
* 将 UI 界面的布局与逻辑分开
  * 在布局时尽量不要用绝对坐标
* 不要把精力都放在写代码和改代码上，维护项目的文档很重要，包括且不限于
  * 给代码写注释
  * 单独编写 markdown 文档
  * 绘制 UML 图记录类的接口与继承关系
* Python 的包相对导入功能不太好用
* 区分 Debug 版本与 Release 版本
  * 在 Release 版本中，移除冗余的输出

总的来说，这不是一个值得研究的项目，因为它的结构中有很多不合理的地方，尤其是与 OOP 以及 UI 布局相关的部分。然而，对于我来说，它具有一定的纪念意义：它证明了大二下学期的我曾经凭一己之力在几个月的时间里折腾出了这么一个东西。

## 关于原作

* [抽卡人生 | 中国独立游戏 | Indienova 独立游戏](https://indienova.com/g/drawcardlife)
* [抽卡人生 Android 版](https://www.taptap.cn/app/35686)
