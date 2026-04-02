# 🔫 恶魔轮盘子弹计数器 (Devil Roulette Bullet Counter)

> 一个基于 Python + Tkinter 的轮盘赌辅助工具，专为《恶魔轮盘》游戏设计

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📌 项目简介

这是一个用于《恶魔轮盘》(Devil Roulette) 游戏的小工具，主要功能是**记录实弹与空弹的数量**，帮助玩家在作弊模式下更直观地追踪弹匣状态。

游戏原版链接：https://store.steampowered.com/app/2692030/Devil_Roulette/

---

## ✨ 功能特点

- **直观弹药显示**：实弹（红色）/ 空弹（蓝色）分类展示
- **作弊模式计数器**：记录每轮已揭露的子弹类型
- **总弹数统计**：实时显示当前轮次总弹数
- **窗口置顶**：始终保持在游戏窗口前方
- **独立 exe 文件**：无需 Python 环境，双击即用

---

## 🗂️ 文件结构

```
devil-roulette-counter/
├── README.md
├── .gitignore
├── 源代码/
│   ├── 终2.py          # 主程序源码（Python + Tkinter GUI）
│   ├── em.ico          # 程序图标
│   ├── bulid_no_cmd.py # PyInstaller 构建脚本
│   └── 恶魔轮盘子弹计数器nc.spec
└── 恶魔轮盘作弊计数器nc.exe  # 预编译可执行文件（Windows）
```

---

## 🔧 构建方法

如果你有 Python 环境，可以自行重新打包：

```bash
pip install pyinstaller
cd 源代码
python bulid_no_cmd.py
```

打包完成后，主程序输出为 `dist/恶魔轮盘作弊计数器nc.exe`

---

## 🎮 使用说明

1. 下载并运行 `恶魔轮盘作弊计数器nc.exe`
2. 打开《恶魔轮盘》游戏
3. 根据游戏中的子弹揭露情况，点击对应按钮记录
4. 工具会实时统计实弹/空弹数量

---

## 🛠️ 技术栈

| 组件 | 技术 |
|------|------|
| GUI 框架 | Tkinter（Python 内置）|
| 打包工具 | PyInstaller |
| 编程语言 | Python 3.x |

---

## 📝 License

MIT License — 欢迎 Fork、Star 和改进！
