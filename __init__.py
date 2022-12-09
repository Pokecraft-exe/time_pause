import time as t

'''time_pause to pause the time'''
__version__ = "0.1"

class time_p():
    def __init__(self, debug=0):
        '''Init the class'''
        self.paused = 0
        self.debug = debug
        self.time = t.time()
        self.pause_start = 0.0
        self.unpaused_time = t.time()
        self.lastcalled = t.time()
        self.__float__()
    def __PRIVATE__copyvalue__(self, value_to_copy):
        '''Private funtion to copy values'''
        return value_to_copy
    def __copy__(self):
        '''Used to return a copy f the class. not reference'''
        return self.__PRIVATE__copyvalue__(self)
    def __PRIVATE__debug__(self, value):
        '''Private function to print value if debug is set to 1'''
        if self.debug:
            print(value)
    def __float__(self):
        '''Returns a float'''
        last = self.__PRIVATE__copyvalue__(self.lastcalled)
        self.lastcalled = t.time()
        self.__PRIVATE__debug__(f"   paused: {self.paused}, time: {self.time}, unpaused_time: {self.unpaused_time}, lastcalled: {self.lastcalled}, last: {last}, {self.lastcalled-last}, pause_start  {self.pause_start}, {self.lastcalled-self.pause_start}")
        self.unpaused_time+= 0 if self.paused else (self.lastcalled-self.pause_start if self.pause_start>last and self.pause_start==self.lastcalled else self.lastcalled-last)
        return self.unpaused_time
    def __str__(self):
        '''Returns a string'''
        return str(self.__float__())
    def pause(self):
        '''Pauses and unpauses the time'''
        if not self.paused:
            self.paused = 1
            self.pause_start = t.time()
        else:
            self.paused = 0
            self.pause_start = 0
    def delay(self, ms):
        '''delay in ms. used like sleep()'''
        t.sleep(ms/1000)
		

if __name__ == '__main__':
    import tkinter as tk
    time_pause = time_p()
    before_p = time_pause.__float__()
    before = t.time()
    def __PRIVATE__TESTING__PAUSE__():
        time_pause.pause()
        
    root = tk.Tk()
    root.resizable(0,0)
    root.title("Library test: time_pause")
    b1 = tk.Button(root, text="pause", command=__PRIVATE__TESTING__PAUSE__)
    label1 = tk.Label(root, text=f'creating time class: value: {time_pause} time.time(): {t.time()}')
    label2 = tk.Label(root, text=f"Current time_p(): {time_pause}")
    label3 = tk.Label(root, text=f"Current time.time(): {t.time()}")
    label4 = tk.Label(root, text=f'the elapsed time with time_paused() is {time_pause.__float__()-before_p}')
    label5 = tk.Label(root, text=f'the elapsed time with time.time() is {t.time()-before}')
    def __PRIVATE__TESTING__ACTUALISE__():
        label2.config(text=f"Current time_p(): {time_pause}")
        label3.config(text=f"Current time.time(): {t.time()}")
        label4.config(text=f'the elapsed time with time_paused() is {time_pause.__float__()-before_p}')
        label5.config(text=f'the elapsed time with time.time() is {t.time()-before}')
        root.after(50, __PRIVATE__TESTING__ACTUALISE__)

    label1.pack(anchor='w')
    label2.pack(anchor='w')
    label3.pack(anchor='w')
    label4.pack(anchor='w')
    label5.pack(anchor='w')
    b1.pack(fill='x')
    print(help(time_p))
    root.after(50, __PRIVATE__TESTING__ACTUALISE__)
    root.mainloop()
