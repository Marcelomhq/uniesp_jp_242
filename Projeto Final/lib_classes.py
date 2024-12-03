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
    def __init__(self,title,message,image_path=None,parent=None):
        super().__init__(parent)
        self.title(title)
        
        icon_image = tk.PhotoImage(file="Logo.png")
        self.iconphoto(False,icon_image)       

        content_frame = ttk.Frame(self)
        content_frame.pack(padx=10, pady=(0,10), fill="x")
        
        if image_path:
            icon_image = tk.PhotoImage(file=image_path)
            self.iconphoto(False,icon_image)             
        
        self.message_label = ttk.Label(self, text=message, wraplength= 550, anchor="center")
        self.message_label.pack(pady=(0,10), padx=10,ipadx=0,ipady=0)

        self.ok_button = ttk.Button(self, text="Ta Certo!", command=self.close)
        self.ok_button.pack(pady=10, anchor='center')
        
        self.update_idletasks()
        label_width = self.message_label.winfo_reqwidth()
        label_height = self.message_label.winfo_reqheight()
        button_height = self.ok_button.winfo_reqheight()

        window_width = max(300, label_width + 80)
        window_height = max(150, label_height+button_height+45)

        self.geometry(f"{window_width}x{window_height}")
        self.resizable(False,False)       

        self.center_window()
        
        self.transient(parent)
        self.grab_set()
        self.wait_window()

    def close(self):
        self.destroy()
    
    def center_window(self):
        """Center the window on the screen."""
        self.update_idletasks()
        x = (self.winfo_screenwidth() - self.winfo_width()) // 2
        y = (self.winfo_screenheight() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")    
        
if __name__ == "__main__":
    slip = Slip(1, "Test advice")
    # print(slip.to_dict())
    print(slip)
