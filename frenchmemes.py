# If it doesn't work... Well... Good luck
# Written by: Sgt. Cuddles#0001 (https://github.com/AWildTeddyBear)

import logging, ctypes, random, os, tkinter, time, threading, subprocess, shutil
from playsound import playsound
from PIL import Image, ImageTk

try:
    logging.basicConfig(level = logging.INFO, format = '[+] %(message)s')
except Exception as e:
    logging.exception(f'baguette logger: {e}')

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

try:
    names = [x.decode('utf-8').strip() for x in open(resource_path('names.txt'), 'rb')]
except Exception as e:
    logging.exception(f'baguette names: {e}')

def playSong():
    try:
        playsound(resource_path('honhon.mp3'))
    except Exception as e:
        logging.exception(f'baguette song: {e}')

def choseName():
    return random.choice(names)

def borkBaguette(loops = 10):
    root = tkinter.Tk()
    root.title('HONHONHONHON')

    cv = tkinter.Canvas(root, width=800, height=700)
    cv.pack(fill='both', expand='yes')

    windowWidth = cv.winfo_reqwidth()
    windowHeight = cv.winfo_reqheight()

    positionRight = int((root.winfo_screenwidth() / 2) - (windowWidth / 2))
    positionDown = int((root.winfo_screenheight() / 2) - (windowHeight / 2))

    # print(f'Requested Width: {windowWidth}\tHeight: {windowHeight}')
    # print(f'Real Width: {root.winfo_screenwidth()}\tHeight: {root.winfo_screenheight()}')
    # print(f'Pos - Right: {positionRight}\tDown: {positionDown}')

    root.geometry(f'+{positionRight}+{positionDown}')

    pil_image = Image.open(resource_path('Dunce.png'))
    pil_image_flip = pil_image.transpose(Image.FLIP_LEFT_RIGHT)
    tk_image = ImageTk.PhotoImage(pil_image)
    tk_image_flip = ImageTk.PhotoImage(pil_image_flip)

    first = cv.create_image(10, 10, image=tk_image, anchor='nw')
    second = cv.create_image(10, 10, image=tk_image_flip, anchor='nw')

    for _ in range(loops):
        # print(f'{i} / {loops - 1}')
        cv.itemconfigure(first, state='hidden')
        root.update_idletasks()
        root.update()
        time.sleep(0.2)
        cv.itemconfigure(first, state='normal')
        cv.itemconfigure(second, state='hidden')
        root.update_idletasks()
        root.update()
        time.sleep(0.2)
        cv.itemconfigure(second, state='normal')
        root.update_idletasks()
        root.update()

def sendTheBaguetteArmy(baguettes = 1):
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, resource_path('baguette.png'), 0)
    except Exception as e:
        logging.exception(f'baguette wallpaper: {e}')

    try:
        for _ in range(baguettes):
            chosenName = f'{choseName()}.png'

            while os.path.exists(os.path.realpath(f'{os.getcwd()}./{chosenName}')):
                chosenName = f'{choseName()}.png'

            src = resource_path('baguette.png')
            dst = os.path.join(os.getcwd(), chosenName)
            shutil.copyfile(src, dst)

    except Exception as e:
        logging.exception(f'baguette copy: {e}')

def main():
    logging.info('Injecting baguettes...')
    time.sleep(0.5)
    logging.info('Ç\'est un vrai état gratuit')
    time.sleep(0.2)
    logging.info('Sending the baguette army payload')
    time.sleep(0.1)
    logging.info('HON HON HON HON HON HON')
    time.sleep(0.2)

    t1 = threading.Thread(target = playSong, args = ())
    t2 = threading.Thread(target = borkBaguette, args = (35,))
    t3 = threading.Thread(target = sendTheBaguetteArmy, args = (500,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

main()