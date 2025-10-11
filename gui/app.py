import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict
from core.acceleration import calcul_acceleration, plus_grand
from core.models import MODELS

class AccelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Loi d'attenuation de l'acceleration selon differents auteurs")
        self.geometry("700x600")
        # palette orange-marron
        self._bg_main = "#FFF3E0"      # très clair
        self._accent = "#D97706"       # orange-marron
        self._heading = "#8B4513"      # marron foncé
        self._winner = "#FFE7C2"       # léger orangé pour highlight
        self.configure(background=self._bg_main)
        self._build_style()
        self._build_ui()

    def _build_style(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except Exception:
            pass
        style.configure("TFrame", background=self._bg_main)
        style.configure("TLabel", background=self._bg_main, foreground=self._heading)
        style.configure("TLabelframe", background=self._bg_main, foreground=self._heading)
        style.configure("TLabelframe.Label", background=self._bg_main, foreground=self._heading)
        style.configure("TButton", background=self._accent, foreground="white")
        style.map("TButton",
                  background=[("active", "#E65C00")],
                  foreground=[("active", "white")])
        # Treeview styling
        style.configure("Treeview",
                        background="white",
                        fieldbackground="white",
                        foreground="black")
        style.configure("Treeview.Heading",
                        background=self._accent,
                        foreground="white",
                        relief="flat")
        style.map("Treeview.Heading",
                  background=[("active", "#E65C00")])

    def _build_ui(self):
        frm = ttk.Frame(self, padding=12)
        frm.pack(fill="both", expand=True)

        input_frame = ttk.LabelFrame(frm, text="Entrées", padding=8)
        input_frame.pack(fill="x", pady=4)

        # Terrain S
        self.s_var = tk.IntVar(value=0)
        ttk.Label(input_frame, text="Nature du terrain:").grid(row=0, column=0, sticky="w")
        rb1 = ttk.Radiobutton(input_frame, text="Rocher (0)", variable=self.s_var, value=0)
        rb2 = ttk.Radiobutton(input_frame, text="Sol (1)", variable=self.s_var, value=1)
        rb1.grid(row=0, column=1, sticky="w", padx=6)
        rb2.grid(row=0, column=2, sticky="w", padx=6)

        # Magnitude M
        ttk.Label(input_frame, text="Magnitude (M):").grid(row=1, column=0, sticky="w", pady=6)
        self.m_entry = ttk.Entry(input_frame, width=12)
        self.m_entry.grid(row=1, column=1, sticky="w")
        self.m_entry.insert(0, "5.0")

        # Distance R
        ttk.Label(input_frame, text="Distance épicentrale (R km):").grid(row=2, column=0, sticky="w", pady=6)
        self.r_entry = ttk.Entry(input_frame, width=12)
        self.r_entry.grid(row=2, column=1, sticky="w")
        self.r_entry.insert(0, "10.0")

        # Bouton calcul
        calc_btn = ttk.Button(input_frame, text="Calculer", command=self.on_calculate)
        calc_btn.grid(row=3, column=0, columnspan=3, pady=8)

        # Résultats (Treeview)
        result_frame = ttk.LabelFrame(frm, text="Résultats", padding=8)
        result_frame.pack(fill="both", expand=True, pady=6)

        columns = ("model", "accel")
        self.tree = ttk.Treeview(result_frame, columns=columns, show="headings", height=8)
        self.tree.heading("model", text="Auteur / Modèle")
        self.tree.heading("accel", text="Accélération (m/s²)")
        self.tree.column("model", width=320)
        self.tree.column("accel", width=180, anchor="e")
        self.tree.pack(fill="both", expand=True, side="left")

        vsb = ttk.Scrollbar(result_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")

        # Info finale simple (sous la table)
        bottom_frame = ttk.Frame(frm, padding=6)
        bottom_frame.pack(fill="x", pady=6)

        # Zone dédiée pour la valeur maximale et les auteurs
        max_frame = ttk.LabelFrame(bottom_frame, text="Accélération maximale", padding=8)
        max_frame.pack(fill="x", expand=True, side="left")

        self.max_value_label = ttk.Label(max_frame, text="Valeur : —", font=("TkDefaultFont", 11, "bold"))
        self.max_value_label.pack(anchor="w", pady=(0,4))

        self.max_authors_label = ttk.Label(max_frame, text="Auteur(s) : —", wraplength=520)
        self.max_authors_label.pack(anchor="w")

        # tag pour winner
        self.tree.tag_configure("winner", background=self._winner)

    def on_calculate(self):
        try:
            S = int(self.s_var.get())
            M = float(self.m_entry.get())
            R = float(self.r_entry.get())
            if R < 0:
                raise ValueError("R doit être >= 0")
            if not (M < 10):
                raise ValueError("Magnitude doit être strictement inférieure à 10")
        except Exception as e:
            messagebox.showerror("Entrée invalide", f"Vérifiez les valeurs : {e}")
            return

        results: Dict[str, float] = {}
        for name, (alpha, beta, gamma, sigma, epsilon, d) in MODELS:
            a = calcul_acceleration(S, M, R, alpha, beta, gamma, sigma, epsilon, d)
            results[name] = a

        # afficher résultats triés
        for i in self.tree.get_children():
            self.tree.delete(i)

        sorted_items = sorted(results.items(), key=lambda x: x[1], reverse=True)
        for name, val in sorted_items:
            self.tree.insert("", "end", values=(name, f"{val:.4f}"), tags=())

        winners, max_val = plus_grand(results)
        # marquer winners
        for iid in self.tree.get_children():
            values = self.tree.item(iid, "values")
            if values[0] in winners:
                self.tree.item(iid, tags=("winner",))

        # mettre à jour la zone maximale
        if max_val is None:
            self.max_value_label.config(text="Valeur : —")
            self.max_authors_label.config(text="Auteur(s) : —")
        else:
            self.max_value_label.config(text=f"Valeur : {max_val:.4f} m/s²")
            self.max_authors_label.config(text=f"Auteur(s) : {', '.join(winners)}")

def main():
    app = AccelApp()
    app.mainloop()

if __name__ == "__main__":
    main()