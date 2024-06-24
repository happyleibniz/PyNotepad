import pyglet, string, gc, sys
from tkinter import messagebox as mb

class NotepadWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pyglet.font.add_file("cambria.ttc")

        # font_name="Cambria",font_size=20,
        self.label = pyglet.text.Label("PyNotepad by happyleibniz", x=266.6666666666666666666666666667, y=self.height - 30)
        self.label_list = []
        self.current_line = 0
        self.col = 0
        self.current_y = 60
        self.label_list.append(pyglet.text.Label("¶",font_name="新宋体",font_size=12.5,x=10, y=self.height - self.current_y))
        self.content = ""
        self.capslock = False
        self.ready = True
        self.control = False
        self.shift = False
        if self.ready:
            pyglet.clock.schedule_interval(self.show, interval=0.5)
        else:
            pass
        self.ready_to_show = True

    def on_draw(self):
        gc.collect()
        self.clear()
        self.label.draw()
        for lb in self.label_list:
            lb.draw()
            lb.text.replace("¶","")
        #self.text_input.draw()

    def show(self,fps):
        if self.ready_to_show:
            self.label_list[self.current_line].text = self.label_list[self.current_line].text.replace("¶","")
            self.ready_to_show = False
        else:
            self.label_list[self.current_line].text += chr(182)
            self.ready_to_show = True
    
    def on_key_press(self, symbol, modifiers):
        # print(chr(symbol))
        self.ready = False
        if symbol == pyglet.window.key.Q:
            pyglet.app.exit()
        elif symbol == pyglet.window.key.ENTER:
            self.label_list[self.current_line].text = self.label_list[self.current_line].text.replace("¶","")
            self.current_y += 15
            self.label_list.append(pyglet.text.Label("",font_name="新宋体",font_size=12.5,x=10, y=self.height-self.current_y))
            self.current_line += 1
            self.col = 0
        elif symbol == pyglet.window.key.LSHIFT or symbol == pyglet.window.key.RSHIFT:
            self.shift = True
        elif symbol == pyglet.window.key.CAPSLOCK:
            self.capslock = not self.capslock
        elif symbol == pyglet.window.key.UP:
            if not self.current_line == 0:
                self.label_list[self.current_line].text = self.label_list[self.current_line].text.replace("¶","")
                self.current_line -= 1
        elif symbol == pyglet.window.key.DOWN:
            self.label_list[self.current_line].text = self.label_list[self.current_line].text.replace("¶","")
            if not self.current_line == len(self.label_list):
                self.current_line += 1
        elif symbol == pyglet.window.key.BACKSPACE:
            if self.col != 0:
                self.col -= 1
            self.label_list[self.current_line].text = self.label_list[self.current_line].text[:-1]
        elif symbol == pyglet.window.key.TAB:
            self.label_list[self.current_line].text += "    "
            self.col += 4
        elif symbol == pyglet.window.key.RCTRL or symbol == pyglet.window.key.LCTRL:
            self.control = True
        else:
            # print(symbol)
            char = chr(symbol)
            
            if char.isprintable():
                if not self.capslock and not self.shift and not self.control:
                    self.label_list[self.current_line].text += char
                elif self.capslock or self.shift:
                    if char in list(string.ascii_lowercase):
                        self.label_list[self.current_line].text += char.upper()
                    elif char in list(string.digits):
                        if char == "0":
                            self.label_list[self.current_line].text += ")"
                        elif char == "1":
                            self.label_list[self.current_line].text += "!"
                        elif char == "2":
                            self.label_list[self.current_line].text += "@"
                        elif char == "3":
                            self.label_list[self.current_line].text += "#"
                        elif char == "4":
                            self.label_list[self.current_line].text += "$"
                        elif char == "5":
                            self.label_list[self.current_line].text += "%"
                        elif char == "6":
                            self.label_list[self.current_line].text += "^"
                        elif char == "7":
                            self.label_list[self.current_line].text += "&"
                        elif char == "8":
                            self.label_list[self.current_line].text += "*"
                        elif char == "9":
                            self.label_list[self.current_line].text += "("
                    elif char in ["-",
                                  "=",
                                  "[",
                                  "]",
                                  ";",
                                  "'",
                                  "\\",
                                  ",",
                                  ".",
                                  "/",
                                  "`"]:
                        if char == "-":
                            self.label_list[self.current_line].text += "_"
                        elif char == "=":
                            self.label_list[self.current_line].text += "+"
                        elif char == "[":
                            self.label_list[self.current_line].text += "{"
                        elif char == "]":
                            self.label_list[self.current_line].text += "}"
                        elif char == ";":
                            self.label_list[self.current_line].text += ":"
                        elif char == "'":
                            self.label_list[self.current_line].text += '"'
                        elif char == "\\":
                            self.label_list[self.current_line].text += "|"
                        elif char == ",":
                            self.label_list[self.current_line].text += "<"
                        elif char == ".":
                            self.label_list[self.current_line].text += ">"
                        elif char == "/":
                            self.label_list[self.current_line].text += "?"
                        elif char == "`":
                            self.label_list[self.current_line].text += "~"
                elif self.control:
                    self.control= False
                    if char == "s":
                        print("save not implimented")
                    elif char == "n":
                        res=mb.askquestion('Clear Notepad?', 'Do you really want to clear the notepad?')
                        if res == 'yes' :
                            self.label = pyglet.text.Label("PyNotepad by happyleibniz", x=266.6666666666666666666666666667, y=self.height - 30)
                            self.label_list = []
                            self.current_line = 0
                            self.col = 0
                            self.current_y = 60
                            self.label_list.append(pyglet.text.Label("¶",font_name="新宋体",font_size=12.5,x=10, y=self.height - self.current_y))
                        else:
                            pass
                    elif char == "q":
                        res=mb.askquestion('Exit Application', 'Do you really want to exit')
                        if res == 'yes' :
                            sys.exit(0)
            self.col += 1
            self.label_list[self.current_line].text = self.label_list[self.current_line].text.replace("¶","")
    def on_key_release(self,symbol, modifier):
        if symbol == pyglet.window.key.LSHIFT or symbol == pyglet.window.key.RSHIFT:
            self.shift = False
        elif symbol == pyglet.window.key.RCTRL or symbol == pyglet.window.key.LCTRL:
            self.control= False
if __name__ == "__main__":
    window = NotepadWindow(width=800, height=600, caption="Advanced Notepad")
    pyglet.app.run()
