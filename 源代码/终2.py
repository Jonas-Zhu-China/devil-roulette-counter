
import tkinter as tk
from tkinter import ttk, font

class AmmoCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("楂樼骇寮硅嵂璁℃暟鍣?)
        self.root.geometry("550x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        # 璁剧疆榛樿缃《
        self.topmost_var = tk.BooleanVar(value=True)
        self.root.attributes('-topmost', self.topmost_var.get())
        
        # 鍒涘缓鑷畾涔夊瓧浣?
        self.title_font = font.Font(family="Arial", size=14, weight="bold")
        self.count_font = font.Font(family="Arial", size=18, weight="bold")
        self.button_font = font.Font(family="Arial", size=12, weight="bold")
        self.bullet_font = font.Font(family="Arial", size=11, weight="bold")
        
        # 瀛愬脊鐘舵€侀€夐」
        self.ammo_types = ["瀹炲脊", "绌哄脊"]
        self.bullet_states = {}  # 瀛樺偍瀛愬脊鐘舵€?{搴忓彿: 鐘舵€亇
        
        # 鍒涘缓涓绘鏋?
        self.create_widgets()
        
        # 缁戝畾閿洏蹇嵎閿?
        self.root.bind("<Up>", lambda e: self.update_count(self.live_count, 1))
        self.root.bind("<Down>", lambda e: self.update_count(self.live_count, -1, True))
        self.root.bind("<Right>", lambda e: self.update_count(self.blank_count, 1))
        self.root.bind("<Left>", lambda e: self.update_count(self.blank_count, -1, True))
        self.root.bind("<space>", lambda e: self.reset_all())
        self.root.bind("<Escape>", lambda e: root.destroy())
        
        # 瀛愬脊搴忓彿蹇嵎閿?
        self.root.bind("<Control-b>", lambda e: self.bullet_frame.focus_set())
        
        # 鍒濆鐒︾偣
        self.root.focus_set()

    def create_widgets(self):
        # 鏍囬鏍?
        title_frame = tk.Frame(self.root, bg="#3498db", height=40)
        title_frame.pack(fill=tk.X)
        
        tk.Label(
            title_frame, 
            text="楂樼骇寮硅嵂璁℃暟鍣?, 
            font=self.title_font,
            bg="#3498db", 
            fg="white"
        ).pack(pady=10)
        
        # 涓诲唴瀹瑰尯
        main_frame = tk.Frame(self.root, bg="#2c3e50", padx=20, pady=15)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # ================= 褰撳墠瀛愬脊搴忓彿鍖哄煙 =================
        current_frame = tk.LabelFrame(
            main_frame, 
            text="褰撳墠瀛愬脊搴忓彿", 
            font=("Arial", 11, "bold"),
            bg="#2c3e50", 
            fg="#f39c12",
            padx=10,
            pady=10
        )
        current_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.current_bullet = tk.IntVar(value=1)
        
        # 鍑忓彿鎸夐挳
        tk.Button(
            current_frame, 
            text="鈼?, 
            font=self.button_font,
            width=3,
            bg="#e67e22", 
            fg="white",
            relief=tk.FLAT,
            command=lambda: self.update_current_bullet(-1)
        ).pack(side=tk.LEFT, padx=(10, 5))
        
        # 褰撳墠瀛愬脊搴忓彿鏄剧ず
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
        
        # 鍔犲彿鎸夐挳
        tk.Button(
            current_frame, 
            text="鈻?, 
            font=self.button_font,
            width=3,
            bg="#e67e22", 
            fg="white",
            relief=tk.FLAT,
            command=lambda: self.update_current_bullet(1)
        ).pack(side=tk.LEFT, padx=(5, 10))
        
        # ================= 寮硅嵂璁℃暟鍖哄煙 =================
        ammo_frame = tk.Frame(main_frame, bg="#2c3e50")
        ammo_frame.pack(fill=tk.X, pady=(0, 15))
        
        # 瀹炲脊璁℃暟鍣?
        live_frame = tk.LabelFrame(
            ammo_frame, 
            text="瀹炲脊", 
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
        
        # 绌哄脊璁℃暟鍣?
        blank_frame = tk.LabelFrame(
            ammo_frame, 
            text="绌哄脊", 
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
        
        # ================= 瀛愬脊鐘舵€佽缃尯鍩?=================
        bullet_frame = tk.LabelFrame(
            main_frame, 
            text="瀛愬脊鐘舵€佽缃?, 
            font=("Arial", 11, "bold"),
            bg="#2c3e50", 
            fg="#9b59b6",
            padx=15,
            pady=15
        )
        bullet_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        self.bullet_frame = bullet_frame  # 淇濆瓨寮曠敤
        
        # 瀛愬脊搴忓彿鎺у埗
        seq_frame = tk.Frame(bullet_frame, bg="#2c3e50")
        seq_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            seq_frame, 
            text="绗嚑鍙戝瓙寮?", 
            font=self.bullet_font,
            bg="#2c3e50", 
            fg="#ecf0f1"
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        self.bullet_num = tk.IntVar(value=1)
        
        tk.Button(
            seq_frame, 
            text="鈼?, 
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
            text="鈻?, 
            font=self.bullet_font,
            width=2,
            bg="#8e44ad", 
            fg="white",
            relief=tk.FLAT,
            command=lambda: self.update_bullet_num(1)
        ).pack(side=tk.LEFT)
        
        # 瀛愬脊鐘舵€佹帶鍒?
        state_frame = tk.Frame(bullet_frame, bg="#2c3e50")
        state_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(
            state_frame, 
            text="瀛愬脊绫诲瀷:", 
            font=self.bullet_font,
            bg="#2c3e50", 
            fg="#ecf0f1"
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        self.bullet_state = tk.StringVar(value="瀹炲脊")
        
        tk.Button(
            state_frame, 
            text="鈼?, 
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
            text="鈻?, 
            font=self.bullet_font,
            width=2,
            bg="#8e44ad", 
            fg="white",
            relief=tk.FLAT,
            command=lambda: self.change_bullet_state(1)
        ).pack(side=tk.LEFT)
        
        # 鎺у埗鎸夐挳鍖?
        control_frame = tk.Frame(main_frame, bg="#2c3e50", pady=15)
        control_frame.pack(fill=tk.X, pady=(10, 0))
        
        # 缃《澶嶉€夋
        self.topmost_cb = tk.Checkbutton(
            control_frame,
            text="绐楀彛缃《",
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
        
        # 閲嶇疆鎸夐挳
        tk.Button(
            control_frame,
            text="鍏ㄩ儴閲嶇疆 (绌烘牸閿?",
            font=("Arial", 10, "bold"),
            bg="#e67e22",
            fg="white",
            relief=tk.FLAT,
            padx=10,
            pady=5,
            command=self.reset_all
        ).pack(side=tk.RIGHT, padx=10)
        
        # 鎻愮ず鏍囩
        tip_frame = tk.Frame(main_frame, bg="#2c3e50")
        tip_frame.pack(fill=tk.X)
        
        tip_label = tk.Label(
            tip_frame,
            text="鎻愮ず: 鈫?鈫?鎺у埗瀹炲脊 | 鈫?鈫?鎺у埗绌哄脊 | Ctrl+B 鐒︾偣鍒板瓙寮硅缃?| ESC 閫€鍑?,
            font=("Arial", 8),
            bg="#2c3e50",
            fg="#bdc3c7"
        )
        tip_label.pack(pady=(5, 0))

    def update_count(self, counter, delta, update_current=False):
        new_value = counter.get() + delta
        if new_value >= 0:  # 闃叉璐熸暟
            counter.set(new_value)
            
            # 濡傛灉鍑忓皯寮硅嵂锛屾洿鏂板綋鍓嶅瓙寮瑰簭鍙?
            if delta < 0 and update_current:
                self.current_bullet.set(self.current_bullet.get() + 1)

    def update_current_bullet(self, delta):
        new_value = self.current_bullet.get() + delta
        if new_value >= 1:  # 瀛愬脊搴忓彿涓嶈兘灏忎簬1
            self.current_bullet.set(new_value)

    def update_bullet_num(self, delta):
        new_value = self.bullet_num.get() + delta
        if new_value >= 1:  # 瀛愬脊搴忓彿涓嶈兘灏忎簬1
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
        
        # 鏇存柊鏍囩棰滆壊
        if self.bullet_state.get() == "瀹炲脊":
            self.state_label.config(fg="#e74c3c")
        else:
            self.state_label.config(fg="#3498db")
        
        # 鑷姩淇濆瓨鐘舵€?
        self.save_bullet_state()

    def save_bullet_state(self):
        bullet_num = self.bullet_num.get()
        state = self.bullet_state.get()
        
        # 鏇存柊鐘舵€佸瓧鍏?
        self.bullet_states[bullet_num] = state

    def update_bullet_state_display(self):
        # 妫€鏌ヨ搴忓彿瀛愬脊鏄惁宸叉湁璁剧疆
        bullet_num = self.bullet_num.get()
        if bullet_num in self.bullet_states:
            self.bullet_state.set(self.bullet_states[bullet_num])
            if self.bullet_state.get() == "瀹炲脊":
                self.state_label.config(fg="#e74c3c")
            else:
                self.state_label.config(fg="#3498db")
        else:
            # 榛樿璁剧疆涓哄疄寮?
            self.bullet_state.set("瀹炲脊")
            self.state_label.config(fg="#e74c3c")

    def reset_all(self):
        # 閲嶇疆璁℃暟鍣?
        self.live_count.set(0)
        self.blank_count.set(0)
        
        # 閲嶇疆褰撳墠瀛愬脊搴忓彿
        self.current_bullet.set(1)
        
        # 閲嶇疆瀛愬脊鐘舵€?
        self.bullet_states = {}
        self.bullet_num.set(1)
        self.bullet_state.set("瀹炲脊")
        self.state_label.config(fg="#e74c3c")

    def toggle_topmost(self):
        self.root.attributes('-topmost', self.topmost_var.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = AmmoCounterApp(root)
    root.mainloop()