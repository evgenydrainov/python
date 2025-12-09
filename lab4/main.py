from tkinter import Tk, Toplevel, Canvas, Label, Button, BOTH, NW
from tkinter import messagebox
from tkinter import font as tkfont
from tkinter import CENTER
from tkinter import StringVar
from tkinter import LEFT, RIGHT
from tkinter import X, Y
from tkinter import GROOVE
from tkinter import TRUE
from tkinter import PhotoImage
import tkinter.ttk as ttk

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

def center_window(win, width, height):
    win.update_idletasks()
    screen_w = win.winfo_screenwidth()
    screen_h = win.winfo_screenheight()
    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

class CardGeneratorApp:
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']

    SUITS = [
        ('Черви', '♥'),
        ('Бубны', '♦'),
        ('Трефы', '♣'),
        ('Пики', '♠'),
    ]

    SUIT_COLOR = {
        'Черви': '#FF0000',
        'Бубны': '#FF0000',
        'Трефы': '#000000',
        'Пики': '#000000',
    }

    VALUE_SYMBOL = {
        'Валет': 'J',
        'Дама': 'Q',
        'Король': 'K',
        'Туз': 'A',
    }

    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Генератор карт")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        center_window(self.root, 400, 300)

        self.value_var = StringVar()
        self.suit_var = StringVar()

        self.small_font = tkfont.Font(family="Arial", size=24, weight="normal")
        self.big_font = tkfont.Font(family="Arial", size=48, weight="bold")
        self.label_font = tkfont.Font(family="Arial", size=12)

        self._build_ui()

    def _build_ui(self):
        padx = 20
        pady = 12

        lbl_value = Label(self.root, text="Выберите значение карты:", font=self.label_font)
        lbl_value.pack(anchor='w', padx=padx, pady=(20, 4))

        self.cb_value = ttk.Combobox(self.root, values=self.VALUES, textvariable=self.value_var, state="readonly")
        self.cb_value.pack(fill=X, padx=padx)
        self.cb_value.bind("<<ComboboxSelected>>", self._on_selection_change)

        lbl_suit = Label(self.root, text="Выберите масть карты:", font=self.label_font)
        lbl_suit.pack(anchor='w', padx=padx, pady=(14, 4))

        suit_display = [f"{name} ({sym})" for name, sym in self.SUITS]
        self.cb_suit = ttk.Combobox(self.root, values=suit_display, textvariable=self.suit_var, state="readonly")
        self.cb_suit.pack(fill=X, padx=padx)
        self.cb_suit.bind("<<ComboboxSelected>>", self._on_selection_change)

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(expand=True)
        self.show_btn = Button(btn_frame, text="Показать карту", command=self.show_card_modal, width=20)
        self.show_btn.pack(pady=(10, 20))
        self._update_show_button_state()

    def _on_selection_change(self, event=None):
        sv = self.suit_var.get()
        if sv:
            if ' (' in sv:
                name = sv.split(' (')[0]
                self.suit_var.set(name)
        self._update_show_button_state()

    def _update_show_button_state(self):
        if self.value_var.get() and self.suit_var.get():
            self.show_btn.config(state="normal")
        else:
            self.show_btn.config(state="disabled")

    def show_card_modal(self):
        val = self.value_var.get()
        suit = self.suit_var.get()
        if not val or not suit:
            messagebox.showwarning("Warning", "Выберите значение и масть карты.")
            return

        card = Card(value=val, suit=suit)
        self._open_modal(card)
    
    def _open_modal(self, card):
        modal = Toplevel(self.root)
        modal_title = f"Карта: {card.value} {card.suit}"
        modal.title(modal_title)
        modal.geometry("300x450")
        modal.resizable(False, False)
        center_window(modal, 300, 450)

        modal.transient(self.root)
        modal.grab_set()

        canvas = Canvas(modal, width=300, height=380)
        canvas.pack(pady=(10, 0))

        card_w, card_h = 200, 300
        canvas_w, canvas_h = 300, 380
        x0 = (canvas_w - card_w) // 2
        y0 = (canvas_h - card_h) // 2
        x1 = x0 + card_w
        y1 = y0 + card_h

        canvas.create_rectangle(x0, y0, x1, y1, fill="#FFFFFF", outline="#000000", width=2)

        color = self.SUIT_COLOR.get(card.suit, "#000000")
        # use the value as symbol if not in map
        value_symbol = self.VALUE_SYMBOL.get(card.value, card.value)

        suit_symbol = next((sym for name, sym in self.SUITS if name == card.suit), '?')

        small_text = f"{value_symbol}\n{suit_symbol}"
        # up left text
        canvas.create_text(x0 + 30, y0 + 50, anchor="center", text=small_text, font=self.small_font, fill=color)

        # down right text
        canvas.create_text(x1 - 30, y1 - 50, anchor="center", text=small_text, font=self.small_font, fill=color, angle=180)

        # big center text
        canvas.create_text((x0 + x1)//2, (y0 + y1)//2, text=suit_symbol, font=self.big_font, fill=color)

        close_btn = Button(modal, text="Закрыть", width=12, command=lambda: self._close_modal(modal))
        close_btn.pack(pady=(12, 18))

        modal.protocol("WM_DELETE_WINDOW", lambda: self._close_modal(modal))

        modal.wait_window()

    def _close_modal(self, modal_win: Toplevel):
        try:
            modal_win.grab_release()
        except Exception:
            pass
        modal_win.destroy()

def main():
    root = Tk()
    app = CardGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
