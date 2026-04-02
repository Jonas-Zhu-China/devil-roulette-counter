
import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    '终2.py',
    '--onefile',
    '--windowed',
    '--icon=em.ico',
    '--name=恶魔轮盘子弹计数器nc',
    '--add-data=em.ico;.'
])