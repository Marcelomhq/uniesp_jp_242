import tkinter as tk
from tkinter import ttk
import menu_boxes

class Slip:
    def __init__(self,slip_id,advice):
        self.id = slip_id
        self.advice = advice
    
    def to_dict(self):
        return {"id": self.id, "advice": self.advice}
    
    def __repr__(self):
        return f'ID: {self.id}, Advice: {self.advice}'
    
class CustomMessageBox(tk.Toplevel):
    def __init__(self,title,message,parent=None):
        super().__init__(parent)
        self.title(title)
        self.geometry("300x150")
        self.resizable(False,False)

        icon_image = tk.PhotoImage(file="Logo.png")
        self.iconphoto(False,icon_image)

        self.message_label = ttk.Label(self, text=message, wraplength= "280", anchor="center")
        self.message_label.pack(pady=20)

        self.ok_button = ttk.Button(self, text="Ta Certo!", command=self.close)
        self.ok_button.pack(pady=10)

        self.transient(parent)
        self.grab_set()
        self.wait_window()

    def close(self):
        self.destroy()



        # self.update_idletasks()
        # x = (self.winfo_screenwidth() - self.winfo_width()) // 2
        # y = (self.winfo_screenheight() - self.winfo_height()) // 2
        # self.geometry(f"+{x}+{y}")
    
        self.message_label

if __name__ == "__main__":
    slip = Slip(1, "Test advice")
    # print(slip.to_dict())
    print(slip)
