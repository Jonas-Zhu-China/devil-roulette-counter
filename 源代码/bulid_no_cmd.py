
import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    '缁?.py',
    '--onefile',
    '--windowed',
    '--icon=em.ico',
    '--name=鎭堕瓟杞洏瀛愬脊璁℃暟鍣╪c',
    '--add-data=em.ico;.'
])