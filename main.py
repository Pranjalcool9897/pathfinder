import customtkinter as ctk

root=ctk.CTk()
root.geometry("500x500+200+10")
ctk.set_appearance_mode("dark")
root.title("Path Finder")
root.minsize(200,200)
##========================================FRAMES====================================

F1=ctk.CTkFrame(root,borderwidth=5,bg_color="#547980")
F1.pack(fill="y",side="left")
F2=ctk.CTkFrame(root,borderwidth=5,bg_color="lightgreen",width=1180)
F2.pack(fill="both",side="left")
root.mainloop()