from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messageboximport mysql.connector
import cv2


class Train:
    def _init_(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)


if __name__ == "_main _":
    root = Tk()
    obj = Train(root)
    root.mainloop()
