
# coding: utf-8

# =============================================================================
# initialization ,scripted by sandbagimon 2018-12/12
# =============================================================================

import tkinter as tk
import hook
import threading
# =============================================================================
# tkinter window
# =============================================================================
window = tk.Tk() 
window.title('Line Emote Downloader')
window.geometry('360x120+120+300') 
address = tk.StringVar()
display_name = tk.StringVar()
download_process = tk.StringVar()
label = tk.Label(window,text = 'Please enter the address!')
label_eg = tk.Label(window,text = 'example: https://store.line.me/stickershop/product/1100/en')
#label_dl = tk.Label(window,textvariable = download_process)
label_text = tk.Label(window,textvariable = display_name)
entry = tk.Entry(window,width=55,textvariable=address)
# =============================================================================
# multithreading and core 
# =============================================================================
def run():
    global address
    global entry
    path = entry.get() # path is the string of address
    if path == '':
        address.set('No address!')

    else:
        hook.set_address(path)

        t1 = threading.Thread(target=hook.core,args=(),name='thread-1')
        t1.setDaemon(True)
        t2 = threading.Thread(target=showname,args=(),name='thread-2')
        t2.setDaemon(True)      
        t1.start()
        t2.start()
    return
def showname():
    while hook.end_flag_out() == False:
        display_name.set('Now Downloading  ' + hook.output_name())
    display_name.set('Download finished!')
button = tk.Button(window,text='Download',command = run)
# =============================================================================
# UI MAPPING
# =============================================================================
label.place(x=10,y=60)
label_eg.place(x=10,y=80)
entry.place(x=10,y=30)
button.place(x=240,y=60)
#label_dl.place (x=10,y=100)
label_text.place(x=50,y=100)
# =============================================================================
# All finished
# =============================================================================
window.mainloop()
window.destroy()
