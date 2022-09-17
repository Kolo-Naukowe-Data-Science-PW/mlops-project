from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

import utils

WINDOW_HEIGHT = 300
WINDOW_WIDTH = 400


def create_window():
    window = Tk()
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    window.config(bg="white")
    window.resizable(width=False, height=False)
    window.title('Sign Language Digits Recognition')

    canvas = Canvas(width=WINDOW_WIDTH,
                    height=WINDOW_HEIGHT,
                    highlightthickness=0,
                    bg='#fbdcfe')
    canvas.pack()

    return window, canvas


def choose_file(master, model, button):
    filepath = filedialog.askopenfilename(title='Open a file', initialdir='/home')
    show_prediction(master, model, button, filepath)


def create_button(master, model):
    button = Button(master,
                    text='Choose a photo',
                    command=lambda: choose_file(master, model, button))
    button.place(relx=0.5, rely=0.5, anchor=CENTER)

    return button


def show_prediction(master, model, button, file_path):
    button.destroy()

    global img
    img = ImageTk.PhotoImage(Image.open(file_path).resize((150, 150)))

    label_img = Label(master, image=img)
    label_img.place(rely=0.5, relx=0.5, anchor=CENTER)

    prediction = utils.predict(model, file_path)

    label_pred = Label(master, text=f'Prediction: {prediction}')
    label_pred.place(rely=0.85, relx=0.5, anchor=CENTER)

    return label_pred


def main():
    model = utils.load_model('models/model_1.h5')

    window, canvas = create_window()
    button_file = create_button(window, model)

    window.mainloop()


if __name__ == '__main__':
    main()
