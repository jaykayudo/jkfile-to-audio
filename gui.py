import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
from file_to_audio import convert_pdf


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Josho File to Audio Converter")
        self.resizable(False,True)
        self.file = ""
        self.extension_options = ['pdf']
        self.function_options ={
            'pdf': convert_pdf
        }

        self.pack_frame = ttk.Frame(self)
        self.header = ttk.Label(self.pack_frame,text="JK File to Audio Converter",justify='center', anchor="center", font=("Poppins",16))
        self.help_label = ttk.Label(self.pack_frame,text="Choose a file and Convert it to audio (mp3)",
                                    justify='left', anchor="center")
        
        self.extension_string_var = tk.StringVar()
        self.extension_string_var.set(self.extension_options[0])

        self.fileextentionoptionmenu_label = ttk.Label(self.pack_frame,text="Choose a File Extension", justify="center", anchor="center")
        self.fileextentionoptionmenu = ttk.OptionMenu(self.pack_frame,self.extension_string_var,*self.extension_options)
        self.filechooserbutton = ttk.Button(self.pack_frame,command=self.choose_file,text="Choose File")
        self.filechooserlabel = ttk.Label(self.pack_frame,text="No File Chosen")
        self.outputlabel = ttk.Label(self.pack_frame,text="", foreground="green")
        self.errorlabel = ttk.Label(self.pack_frame,text="", foreground="red")
        self.submitbutton = ttk.Button(self.pack_frame,text="Covert",command= self.submit_form)

        self.header.pack(side="top",fill="x",expand=1, pady=(10,10))
        self.help_label.pack(side="top",fill="x",expand=1, pady=(5,10))
        
        self.fileextentionoptionmenu_label.pack(side="top",fill="x", pady=5,anchor="center")
        self.fileextentionoptionmenu.pack(side="top",fill="x", pady=10)
        self.filechooserbutton.pack(side="top",padx=10,pady=10)
        self.filechooserlabel.pack(side="top", pady=10)
        self.submitbutton.pack(side="top", fill="x")
        self.errorlabel.pack(side="top",pady=10)
        self.outputlabel.pack(side="top",pady=10)
        self.pack_frame.pack(side="top",expand=1, padx=(10,10))

    def choose_file(self):
        self.file = filedialog.askopenfilename(filetypes=[('Document Files',("*."+self.extension_string_var.get()))])
        if self.file:
            self.filechooserlabel.config({'text':self.file})
        else:
            self.filechooserlabel.config({'text':'No File Chosen'})
    def submit_form(self):
        self.outputlabel.config({'text':''})
        file = self.file
        file_type = self.extension_string_var.get()
        if not file:
            self.errorlabel.config({'text':'Please Choose a file'})
            return
        else:
            self.errorlabel.config({'text':''})
        self.filechooserbutton.config(state="disabled")
        self.submitbutton.config(state="disabled")

        self.outputlabel.config({'text':'Converting......'})
        path = self.function_options[file_type](file) # Function to Convert to Audio
        self.outputlabel.config({'text':f'Your Audio can be found at: {path}'})
        self.filechooserbutton.config(state="normal")
        self.submitbutton.config(state="normal")

window = Window()
window.mainloop()