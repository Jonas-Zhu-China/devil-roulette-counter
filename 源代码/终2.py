
import tkinter as tk
from tkinter import ttk, font

class AmmoCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("高级弹药计数器")
        self.root.geometry("550x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        # 设置默认置顶
        self.topmost_var = tk.BooleanVar(value=True)
        self.root.attributes('-topmost', self.topmost_var.get())
        
        # 创建自定义字体
        self.title_font = font.Font(family="Arial", size=14, weight="bold")
        self.count_font = font.Font(family="Arial", size=18, weight="bold")
        self.button_font = font.Font(family="Arial", size=12, weight="bold")
        self.bullet_font = font.Font(family="Arial", size=11, weight="bold")
        
        # 子弹状态选项
        self.ammo_types = ["实弹", "空弹"]
        self.bullet_states = {}  # 存储子弹状态 {序号: 状态}
        
        # 创建主框架
        self.create_widgets()
        
        # 绑定键盘快捷键
        self.root.bind("<Up>", lambda e: self.update_count(self.live_count, 1))
        self.root.bind("<Down>", lambda e: self.update_count(self.live_count, -1, True))
        self.root.bind("<Right>", lambda e: self.update_count(self.blank_count, 1))
        self.root.bind("<Left>", lambda e: self.update_count(self.blank_count, -1, True))
        self.root.bind("<space>", lambda e: self.reset_all())
        self.root.bind("<Escape>", lambda e: root.destroy())
        
        # 子弹序号快捷键
        self.root.bind("<Control-b>", lambda e: self.bullet_frame.focus_set())
        
        # 初始焦点
        self.root.focus_set()

    def create_widgets(self):
        # 标题栏
        title_frame = tk.Frame(self.root, bg="#3498db", height=40)
        title_frame.pack(fill=tk.X)
        
        tk.Label(
            title_frame, 
            text="高级弹药计数器", 
            font=self.title_font,
            bg="#3498db", 
            fg="white"
        ).pack(pady=10)
        
        # 主内容区
        main_frame = tk.Frame(self.root, bg="#2c3e50", padx=20, pady=15)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # ================= 当前子弹序号区域 =================
        current_frame = tk.LabelFrame(
            main_frame, 
            text="当前子弹序号", 
            font=("Arial", 11, "bold"),
            bg="#2c3e50", 
            fg="#f39c12",
            padx=10,
            pady=10
        )
        current_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.current_bullet = tk.IntVar(value=1)
        
        # 减号按钮
        tk.Button(
            current_frame, 
            text="◄", 
            font=self.button_font,
            width=3,
            bg="#e67e22", 
            fg="white",
            relief=tk.FLAT,
            command=lambda: self.update_current_bullet(-1)
        ).pack(side=tk.LEFT, padx=(10, 5))
        
        # 当前子弹序号显示
        tk.Label(
            current_frame, 
            textvariable=self.current_bullet, 
            font=self.count_font,
            width=5,
            bg="#34495e", 
            fg="#f39c12",
            relief=tk.SUNKEN,
            padx=10,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
        # 加号按钮
        tk.Button(
            current_frame, 
            text="►", 
            font=self.button_font,
            width=3,
            bg="#e67e22", 
            fg="white",
            relief=tk.FLAT,
            command=lambda: self.update_current_bullet(1)
        ).pack(side=tk.LEFT, padx=(5, 10))
        
        # ================= 弹药计数区域 =================
        ammo_frame = tk.Frame(main_frame, bg="#2c3e50")
        ammo_frame.pack(fill=tk.X, pady=(0, 15))
        
        # 实弹计数器
        live_frame = tk.LabelFrame(
            ammo_frame, 
            text="实弹", 
            font=("Arial", 11, "bold"),
            bg="#2c3e50", 
            fg="#e74c3c",
            padx=10,
            pady=10
        )
        live_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        self.live_count = tk.IntVar(value=0)
        
        tk.Button(
            live_frame, 
            text="-", 
            font=self.button_font,
            width=4,
            bg="#e74c3c", 
            fg="white",
            relief=tk.FLAT,
            command=lambda: self.update_count(self.live_count, -1, True)
        ).grid(row=0, column=0, padx=5)
        
        tk.Label(
            live_frame, 
            textvariable=self.live_count, 
            font=self.count_font,
            width=5,
            bg="#34495e", 
            fg="#e74c3c",
            relief=tk.SUNKEN,
            padx=10,
            pady=5
        ).grid(row=0, column=1, padx=5)
        
        tk.Button(
            live_frame, 
            text="+", 
            font=self.button_font,
            width=4,
            bg="#e74c3c", 
            fg="white",
            relief=tk.FLAT,
            command=lambda: self.update_count(self.live_count, 1)
        ).grid(row=0, column=2, padx=5)
        
        # 空弹计数器
        blank_frame = tk.LabelFrame(
            ammo_frame, 
            text="空弹", 
            font=("Arial", 11, "bold"),
            bg="#2c3e50", 
            fg="#3498db",
            padx=10,
            pady=10
        )
        blank_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        self.blank_count = tk.IntVar(value=0)
        
        tk.Button(
            blank_frame, 
            text="-", 
            font=self.button_font,
            width=4,
            bg="#3498db", 
            fg="white",
            relief=tk.FLAT,
            command=lambda: self.update_count(self.blank_count, -1, True)
        ).grid(row=0, column=0, padx=5)
        
        tk.Label(
            blank_frame, 
            textvariable=self.blank_count, 
            font=self.count_font,
            width=5,
            bg="#34495e", 
            fg="#3498db",
            relief=tk.SUNKEN,
            padx=10,
            pady=5
        ).grid(row=0, column=1, padx=5)
        
        tk.Button(
            blank_frame, 
            text="+", 
            font=self.button_font,
            width=4,
            bg="#3498db", 
            fg="white",
            relief=tk.FLAT,
            command=lambda: self.update_count(self.blank_count, 1)
        ).grid(row=0, column=2, padx=5)
        
        # ================= 子弹状态设置区域 =================
        bullet_frame = tk.LabelFrame(
            main_frame, 
            text="子弹状态设置", 
            font=("Arial", 11, "bold"),
            bg="#2c3e50", 
            fg="#9b59b6",
            padx=15,
            pady=15
        )
        bullet_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        self.bullet_frame = bullet_frame  # 保存引用
        
        # 子弹序号控制
        seq_frame = tk.Frame(bullet_frame, bg="#2c3e50")
        seq_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            seq_frame, 
            text="第几发子弹:", 
            font=self.bullet_font,
            bg="#2c3e50", 
            fg="#ecf0f1"
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        self.bullet_num = tk.IntVar(value=1)
        
        tk.Button(
            seq_frame, 
            text="◄", 
            font=self.bullet_font,
            width=2,
            bg="#8e44ad", 
            fg="white",
            relief=tk.FLAT,
            command=lambda: self.update_bullet_num(-1)
        ).pack(side=tk.LEFT)
        
        self.bullet_num_entry = tk.Entry(
            seq_frame, 
            textvariable=self.bullet_num, 
            font=self.bullet_font,
            width=5,
            justify=tk.CENTER,
            bg="#34495e", 
            fg="#ecf0f1",
            relief=tk.SUNKEN,
            borderwidth=1
        )
        self.bullet_num_entry.pack(side=tk.LEFT, padx=5)
        self.bullet_num_entry.bind("<Return>", self.validate_bullet_num)
        
        tk.Button(
            seq_frame, 
            text="►", 
            font=self.bullet_font,
            width=2,
            bg="#8e44ad", 
            fg="white",
            relief=tk.FLAT,
            command=lambda: self.update_bullet_num(1)
        ).pack(side=tk.LEFT)
        
        # 子弹状态控制
        state_frame = tk.Frame(bullet_frame, bg="#2c3e50")
        state_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(
            state_frame, 
            text="子弹类型:", 
            font=self.bullet_font,
            bg="#2c3e50", 
            fg="#ecf0f1"
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        self.bullet_state = tk.StringVar(value="实弹")
        
        tk.Button(
            state_frame, 
            text="◄", 
            font=self.bullet_font,
            width=2,
            bg="#8e44ad", 
            fg="white",
            relief=tk.FLAT,
            command=lambda: self.change_bullet_state(-1)
        ).pack(side=tk.LEFT)
        
        self.state_label = tk.Label(
            state_frame, 
            textvariable=self.bullet_state, 
            font=self.bullet_font,
            width=8,
            bg="#34495e", 
            fg="#9b59b6",
            relief=tk.SUNKEN,
            padx=10,
            pady=3
        )
        self.state_label.pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            state_frame, 
            text="►", 
            font=self.bullet_font,
            width=2,
            bg="#8e44ad", 
            fg="white",
            relief=tk.FLAT,
            command=lambda: self.change_bullet_state(1)
        ).pack(side=tk.LEFT)
        
        # 控制按钮区
        control_frame = tk.Frame(main_frame, bg="#2c3e50", pady=15)
        control_frame.pack(fill=tk.X, pady=(10, 0))
        
        # 置顶复选框
        self.topmost_cb = tk.Checkbutton(
            control_frame,
            text="窗口置顶",
            variable=self.topmost_var,
            command=self.toggle_topmost,
            bg="#2c3e50",
            fg="#ecf0f1",
            selectcolor="#2c3e50",
            activebackground="#2c3e50",
            activeforeground="#ecf0f1",
            font=("Arial", 10)
        )
        self.topmost_cb.pack(side=tk.LEFT, padx=10)
        
        # 重置按钮
        tk.Button(
            control_frame,
            text="全部重置 (空格键)",
            font=("Arial", 10, "bold"),
            bg="#e67e22",
            fg="white",
            relief=tk.FLAT,
            padx=10,
            pady=5,
            command=self.reset_all
        ).pack(side=tk.RIGHT, padx=10)
        
        # 提示标签
        tip_frame = tk.Frame(main_frame, bg="#2c3e50")
        tip_frame.pack(fill=tk.X)
        
        tip_label = tk.Label(
            tip_frame,
            text="提示: ↑/↓ 控制实弹 | ←/→ 控制空弹 | Ctrl+B 焦点到子弹设置 | ESC 退出",
            font=("Arial", 8),
            bg="#2c3e50",
            fg="#bdc3c7"
        )
        tip_label.pack(pady=(5, 0))

    def update_count(self, counter, delta, update_current=False):
        new_value = counter.get() + delta
        if new_value >= 0:  # 防止负数
            counter.set(new_value)
            
            # 如果减少弹药，更新当前子弹序号
            if delta < 0 and update_current:
                self.current_bullet.set(self.current_bullet.get() + 1)

    def update_current_bullet(self, delta):
        new_value = self.current_bullet.get() + delta
        if new_value >= 1:  # 子弹序号不能小于1
            self.current_bullet.set(new_value)

    def update_bullet_num(self, delta):
        new_value = self.bullet_num.get() + delta
        if new_value >= 1:  # 子弹序号不能小于1
            self.bullet_num.set(new_value)
            self.update_bullet_state_display()

    def validate_bullet_num(self, event=None):
        try:
            num = int(self.bullet_num_entry.get())
            if num < 1:
                num = 1
            self.bullet_num.set(num)
            self.update_bullet_state_display()
        except ValueError:
            self.bullet_num.set(1)
        return "break"

    def change_bullet_state(self, direction):
        current_index = self.ammo_types.index(self.bullet_state.get())
        new_index = (current_index + direction) % len(self.ammo_types)
        self.bullet_state.set(self.ammo_types[new_index])
        
        # 更新标签颜色
        if self.bullet_state.get() == "实弹":
            self.state_label.config(fg="#e74c3c")
        else:
            self.state_label.config(fg="#3498db")
        
        # 自动保存状态
        self.save_bullet_state()

    def save_bullet_state(self):
        bullet_num = self.bullet_num.get()
        state = self.bullet_state.get()
        
        # 更新状态字典
        self.bullet_states[bullet_num] = state

    def update_bullet_state_display(self):
        # 检查该序号子弹是否已有设置
        bullet_num = self.bullet_num.get()
        if bullet_num in self.bullet_states:
            self.bullet_state.set(self.bullet_states[bullet_num])
            if self.bullet_state.get() == "实弹":
                self.state_label.config(fg="#e74c3c")
            else:
                self.state_label.config(fg="#3498db")
        else:
            # 默认设置为实弹
            self.bullet_state.set("实弹")
            self.state_label.config(fg="#e74c3c")

    def reset_all(self):
        # 重置计数器
        self.live_count.set(0)
        self.blank_count.set(0)
        
        # 重置当前子弹序号
        self.current_bullet.set(1)
        
        # 重置子弹状态
        self.bullet_states = {}
        self.bullet_num.set(1)
        self.bullet_state.set("实弹")
        self.state_label.config(fg="#e74c3c")

    def toggle_topmost(self):
        self.root.attributes('-topmost', self.topmost_var.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = AmmoCounterApp(root)
    root.mainloop()