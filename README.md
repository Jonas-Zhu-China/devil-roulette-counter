# 🔫 恶魔轮盘子弹计数器 (Devil Roulette Bullet Counter)

> 一个基于 Python + Tkinter 的轮盘赌辅助工具，专为《恶魔轮盘》游戏设计

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📌 项目简介

这是一个用于《恶魔轮盘》(Devil Roulette) 游戏的小工具。

**郑重声明：本工具不是外挂，也不是作弊程序。**

游戏机制是这样的：每局游戏开始前，系统会向玩家展示本轮弹匣里有哪些子弹（几发实弹、几发空弹），但游戏开始后，子弹的顺序会被打乱，玩家需要靠记忆来追踪。子弹数量越多，记忆难度就越大。

本工具的作用就是**帮玩家记录每一轮已经击发过什么子弹、还剩什么子弹**，让玩家不用费脑子记，可以专心享受游戏策略本身的乐趣。

游戏原版链接：https://store.steampowered.com/app/2692030/Devil_Roulette/

---

## ✨ 功能特点

- **直观弹药显示**：实弹（红色）/ 空弹（蓝色）分类展示
- **弹匣状态追踪**：实时记录已击发的子弹，显示剩余弹种
- **总弹数统计**：显示当前轮次总弹数
- **窗口置顶**：始终保持在游戏窗口前方，不遮挡操作
- **独立 exe 文件**：无需 Python 环境，双击即用

---

## 🗂️ 文件结构

```
devil-roulette-counter/
├── README.md
├── .gitignore
├── 恶魔轮盘作弊计数器nc.exe  # 预编译可执行文件（Windows，开箱即用）
└── 源代码/
    ├── 终2.py          # 主程序源码（Python + Tkinter GUI）
    ├── em.ico          # 程序图标
    ├── bulid_no_cmd.py # PyInstaller 构建脚本
    └── 恶魔轮盘计数器nc.spec  # PyInstaller 打包配置
```

---

## 🔧 构建方法

如果你有 Python 环境，可以自行重新打包：

```bash
# 安装依赖
pip install pyinstaller

# 运行打包脚本
cd 源代码
python bulid_no_cmd.py
```

打包完成后，主程序输出为 `dist/恶魔轮盘作弊计数器nc.exe`

---

## 🎮 使用说明

1. 下载并运行 `恶魔轮盘作弊计数器nc.exe`
2. 打开《恶魔轮盘》游戏
3. 游戏开始前，记下弹匣里有哪些子弹
4. 游戏中每开一枪，就在计数器上点击对应的子弹类型
5. 工具会实时统计已击发的子弹和剩余弹种

---

## 🛠️ 技术栈

| 组件 | 技术 |
|------|------|
| GUI 框架 | Tkinter（Python 内置）|
| 打包工具 | PyInstaller |
| 编程语言 | Python 3.x |

---

## 💛 赞赏支持

如果你觉得这个工具对你有帮助，欢迎扫码打赏，您的支持是我继续维护的动力！

<img src="https://raw.githubusercontent.com/Jonas-Zhu-China/devil-roulette-counter/main/%E8%B5%9E%E8%B5%8F%E7%A0%81/bece2c0c8e74ed5c4ceb88d1819a1bfe.jpg" width="280" alt="微信赞赏码" /> <img src="https://raw.githubusercontent.com/Jonas-Zhu-China/devil-roulette-counter/main/%E8%B5%9E%E8%B5%8F%E7%A0%81/caa22a5535d130cd98683065921a44df.jpg" width="280" alt="支付宝赞赏码" />

---

## 📝 License

MIT License — 欢迎 Fork、Star 和改进！
