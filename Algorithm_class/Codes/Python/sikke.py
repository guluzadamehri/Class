import tkinter as tk
from tkinter import messagebox
import itertools

class UltimateCoinSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Peşəkar Saxta Sikkə Dedektoru")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f2f5")
        
        # Header
        tk.Label(root, text="Sikkə Analiz Sistemi", font=("Helvetica", 16, "bold"), bg="#f0f2f5", fg="#1a73e8").pack(pady=15)
        
        # Input Section
        input_frame = tk.Frame(root, bg="#f0f2f5")
        input_frame.pack(pady=5)
        tk.Label(input_frame, text="Sikkə sayı:", font=("Arial", 11), bg="#f0f2f5").pack(side=tk.LEFT, padx=5)
        self.entry_n = tk.Entry(input_frame, width=5, font=("Arial", 11), justify='center')
        self.entry_n.pack(side=tk.LEFT, padx=5)
        self.entry_n.insert(0, "12")
        
        self.btn_start = tk.Button(root, text="SİSTEMİ BAŞLAT", command=self.start_game, 
                                  bg="#1a73e8", fg="white", font=("Arial", 10, "bold"), padx=20)
        self.btn_start.pack(pady=10)
        
        # Display Area
        self.info_box = tk.Label(root, text="Sikkə sayını daxil edib 'Başlat' düyməsinə basın.", 
                                 font=("Courier", 11), bg="white", fg="#333", relief="sunken", 
                                 padx=15, pady=15, width=60, height=8, wraplength=450)
        self.info_box.pack(pady=10)
        
        # Buttons
        self.btns_frame = tk.Frame(root, bg="#f0f2f5")
        self.btns_frame.pack(pady=20)
        
        self.possibilities = []
        self.step = 0

    def start_game(self):
        try:
            n = int(self.entry_n.get())
            if n < 3 or n > 40: # 40-dan çoxu hesablamaq vaxt apara bilər
                messagebox.showwarning("Xəta", "Sikkə sayı 3 ilə 40 arasında olmalıdır.")
                return
            
            # (sikkə_no, status) -> 1: ağır, -1: yüngül
            self.possibilities = []
            for i in range(1, n + 1):
                self.possibilities.append((i, 1))
                self.possibilities.append((i, -1))
            
            self.step = 0
            self.next_move()
        except ValueError:
            messagebox.showerror("Xəta", "Düzgün rəqəm daxil edin.")

    def get_simulated_result(self, coin, status, left, right):
        if coin in left:
            return "left" if status == 1 else "right"
        if coin in right:
            return "right" if status == 1 else "left"
        return "equal"

    def find_best_weighing(self):
        # Qalan bütün sikkələr
        current_coins = sorted(list(set(p[0] for p in self.possibilities)))
        best_move = None
        min_max_size = float('inf')

        # Çəki kombinasiyalarını yoxla (Sadələşdirilmiş Heuristic)
        # n kiçikdirsə bütün kombinasiyaları, böyükdürsə nümunələri yoxlayırıq
        import random
        all_coins = list(range(1, int(self.entry_n.get()) + 1))
        
        for _ in range(300): # 300 təsadüfi kombinasiyadan ən yaxşısını seç
            k = random.randint(1, len(all_coins) // 2)
            shuffled = random.sample(all_coins, 2 * k)
            left = set(shuffled[:k])
            right = set(shuffled[k:])
            
            # Bu çəki ehtimalları necə bölür?
            results = {"left": 0, "right": 0, "equal": 0}
            for p in self.possibilities:
                res = self.get_simulated_result(p[0], p[1], left, right)
                results[res] += 1
            
            max_res = max(results.values())
            if max_res < min_max_size:
                min_max_size = max_res
                best_move = (left, right)
        
        return best_move

    def next_move(self):
        self.step += 1
        
        if len(self.possibilities) == 1:
            self.finish()
            return
        if len(self.possibilities) == 0:
            self.info_box.config(text="ZİDDİYYƏT!\nVerilən məlumatlara uyğun saxta sikkə yoxdur.", fg="red")
            self.clear_btns()
            return

        left, right = self.find_best_weighing()
        self.current_left = left
        self.current_right = right
        
        msg = f"ADDIM №{self.step}\n" + "="*30 + \
              f"\nSOL TƏRƏF: {sorted(list(left))}" + \
              f"\nSAĞ TƏRƏF: {sorted(list(right))}" + \
              f"\n" + "="*30 + "\nTərəzi vəziyyəti?"
        
        self.info_box.config(text=msg, fg="#333")
        self.render_buttons()

    def process(self, result):
        self.possibilities = [p for p in self.possibilities 
                             if self.get_simulated_result(p[0], p[1], self.current_left, self.current_right) == result]
        self.next_move()

    def render_buttons(self):
        self.clear_btns()
        tk.Button(self.btns_frame, text="SOL AŞAĞI", bg="#f44336", fg="white", width=12, command=lambda: self.process("left")).grid(row=0, column=0, padx=5)
        tk.Button(self.btns_frame, text="TARAZLIQ", bg="#9e9e9e", fg="white", width=12, command=lambda: self.process("equal")).grid(row=0, column=1, padx=5)
        tk.Button(self.btns_frame, text="SAĞ AŞAĞI", bg="#4caf50", fg="white", width=12, command=lambda: self.process("right")).grid(row=0, column=2, padx=5)

    def clear_btns(self):
        for w in self.btns_frame.winfo_children(): w.destroy()

    def finish(self):
        coin, status = self.possibilities[0]
        txt = "AĞIR" if status == 1 else "YÜNGÜL"
        self.info_box.config(text=f"NƏTİCƏ TAPILDI!\n\nSAXTA SİKKƏ: №{coin}\nSTATUS: {txt}", fg="#2e7d32")
        self.clear_btns()

if __name__ == "__main__":
    root = tk.Tk()
    app = UltimateCoinSolver(root)
    root.mainloop()
