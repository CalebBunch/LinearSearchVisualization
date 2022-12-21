import pygame
import sys
import pygame_widgets as pw
from pygame_widgets.button import Button
from itertools import count
import tkinter as tk
import time

pygame.init()

win = pygame.display.set_mode((1600, 900))

pygame.display.set_caption("Linear Search")

x = 40

width = 10

heights = [i * 10 for i in range(1, 78)]

GREEN = (0, 255, 0)

DARK_BLUE = (0, 20, 64)

BLACK = (0, 0, 0)


search_button = Button(
    win,
    20,
    20,
    100,
    50,
    text="Search",
    fontSize=50,
    textColour=GREEN,
    margin=20,
    inactiveColour=BLACK,
    pressedColour=BLACK,
    radius=20,
    onRelease=lambda: manage_search(heights),
)


quit_button = Button(
    win,
    1470,
    20,
    100,
    50,
    text="Quit",
    fontSize=50,
    textColour=GREEN,
    margin=20,
    inactiveColour=BLACK,
    pressedColour=BLACK,
    radius=20,
    onRelease=lambda: force_quit(),
)


def urs_input():
    root = tk.Tk()

    root.title("Choose Speed")

    root.geometry("500x300")

    root.eval("tk::PlaceWindow . center")

    root.resizable(False, False)

    root.configure(background="black")

    def input_fast():
        string = entry.get()
        entry.delete(0, "end")
        str_list = string.split(" ")
        if str_list[-1].isdigit():
            target = int(str_list[-1])
            root.destroy()
            time.sleep(0.5)
            linear_search_fast(target)
        else:
            root.destroy()
            urs_input()

    def input_slow():
        string = entry.get()
        entry.delete(0, "end")
        str_list = string.split(" ")
        if str_list[-1].isdigit():
            target = int(str_list[-1])
            root.destroy()
            time.sleep(0.5)
            linear_search_slow(target)
        else:
            root.destroy()
            urs_input()

    entry = tk.Entry(
        root,
        width=40,
        foreground="green",
        background="black",
        insertbackground="green",
    )

    entry.focus_set()

    entry.insert(0, "Enter target num: 1 - 77")

    entry.pack(ipady=3)

    label = tk.Label(
        text="\n\nNow choose the speed for the search algorithm:",
        fg="green",
        bg="black",
        anchor="c",
        font=("Helvetica 14 bold"),
    )
    label.pack()

    button_fast = tk.Button(
        root,
        height=2,
        width=12,
        text="Fast",
        command=lambda: input_fast(),
        font=("Helvetica 16 bold"),
        fg="green",
        bg="black",
        borderwidth=0,
        activebackground="grey",
    )

    button_fast.place(x=20, y=150)

    button_slow = tk.Button(
        root,
        height=2,
        width=12,
        text="Slow",
        command=lambda: input_slow(),
        font=("Helvetica 16 bold"),
        fg=("green"),
        bg="black",
        borderwidth=0,
        activebackground="grey",
    )

    button_slow.place(x=300, y=150)
    tk.mainloop()


def counter(count=count(1)):
    return next(count)


def display_heights(heights):

    for i in range(len(heights)):

        pygame.draw.rect(
            win, DARK_BLUE, (x + 20 * i, (900 - heights[i]), width, heights[i])
        )


def change_color(heights, index1, color):
    for i in range(len(heights)):

        if i == index1:
            pygame.draw.rect(
                win,
                color,
                (x + 20 * index1, (900 - heights[index1]), width, heights[index1]),
            )
            pygame.display.update()


def found(target):
    root = tk.Tk()

    root.title("Found")

    root.geometry("300x75")

    root.eval("tk::PlaceWindow . center")

    root.resizable(False, False)

    root.configure(background="black")

    str_target = str(target)

    label = tk.Label(
        text=f"Found Target:\n\nIt was {str_target}.",
        fg="green",
        bg="black",
        anchor="c",
        font=("Helvetica 14 bold"),
    )
    label.pack()

    tk.mainloop()


def linear_search_fast(target):

    for i in range(len(heights)):
        win.fill((0, 0, 0))

        display_heights(heights)

        change_color(heights, i, GREEN)

        pygame.time.delay(20)

        if heights[i] == target * 10:
            time.sleep(1.0)
            found(target)
            break


def linear_search_slow(target):

    for i in range(len(heights)):
        win.fill((0, 0, 0))

        display_heights(heights)

        change_color(heights, i, GREEN)

        pygame.time.delay(100)

        if heights[i] == target * 10:
            time.sleep(1.0)
            found(target)
            break


def manage_search(heights):

    counter()

    if counter() - 1 == 1:
        urs_input()

    else:
        display_heights(heights)
        urs_input()


def main():
    run = True

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        if keys[pygame.K_q]:
            run = False

        win.fill((0, 0, 0))

        display_heights(heights)

        pw.update(event)

        search_button.listen(event)

        search_button.draw()

        quit_button.listen(event)

        quit_button.draw()

        pygame.display.update()

    pygame.quit()

    sys.exit()


def force_quit():
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
