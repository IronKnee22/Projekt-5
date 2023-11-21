import customtkinter


class LeftFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text="left frame")
        self.label.grid(row=0, column=0, padx=10)

        self.button1 = customtkinter.CTkButton(
            self, text="Akce 1", command=self.button_event)
        self.button1.grid(row=1, column=0, padx=10, pady=10)

        self.button2 = customtkinter.CTkButton(
            self, text="Akce 2", command=self.button_event)
        self.button2.grid(row=2, column=0, padx=10, pady=10)

        self.button3 = customtkinter.CTkButton(
            self, text="Akce 3", command=self.button_event)
        self.button3.grid(row=3, column=0, padx=10, pady=10)

        self.button4 = customtkinter.CTkButton(
            self, text="Akce 4", command=self.button_event)
        self.button4.grid(row=4, column=0, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(self, text=" ")
        self.label2.grid(row=5, column=0, padx=10)

        self.label1 = customtkinter.CTkLabel(self, text=" ")
        self.label1.grid(row=6, column=0, padx=10)

        self.label = customtkinter.CTkLabel(self, text=" ")
        self.label.grid(row=7, column=0, padx=10)

        self.label_switch = customtkinter.CTkLabel(
            self, text="Light/Dark Mode")
        self.label_switch.grid(row=8, column=0, padx=10)

        self.switch = customtkinter.CTkSwitch(self, text="Dark Mode", command=self.switch_event,
                                              onvalue="on", offvalue="off")
        self.switch.grid(row=10, column=0, padx=10)

    def switch_event(self):
        if (self.switch.get() == "on"):
            customtkinter.set_appearance_mode("light")
            self.switch.configure(text="Dark Mode")
        else:
            customtkinter.set_appearance_mode("dark")
            self.switch.configure(text="Light Mode")

    def button_event(self):
        print("Akce")


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # ?první sloupec

        self.label_sval1 = customtkinter.CTkLabel(self, text="sval1")
        self.label_sval1.grid(row=1, column=0, padx=20)

        self.progressbar1 = customtkinter.CTkProgressBar(
            self, orientation="horizontal")
        self.progressbar1.grid(row=2, column=0, padx=20)

        self.entry1 = customtkinter.CTkEntry(self, placeholder_text="entry")
        self.entry1.grid(row=3, column=0, padx=20, pady=10)

        self.label_sval3 = customtkinter.CTkLabel(self, text="sval3")
        self.label_sval3.grid(row=7, column=0, padx=20)

        self.progressbar3 = customtkinter.CTkProgressBar(
            self, orientation="horizontal")
        self.progressbar3.grid(row=8, column=0, padx=20)

        self.entry3 = customtkinter.CTkEntry(self, placeholder_text="entry3")
        self.entry3.grid(row=9, column=0, padx=20, pady=10)

        # ?druhý sloupec
        self.label = customtkinter.CTkLabel(self, text="main frame")
        self.label.grid(row=0, column=1, padx=20)

        self.label_sval5 = customtkinter.CTkLabel(self, text="sval5")
        self.label_sval5.grid(row=4, column=1, padx=20)

        self.progressbar5 = customtkinter.CTkProgressBar(
            self, orientation="horizontal")
        self.progressbar5.grid(row=5, column=1, padx=20)

        self.entry5 = customtkinter.CTkEntry(self, placeholder_text="entry5")
        self.entry5.grid(row=6, column=1, padx=20, pady=10)

        self.button = customtkinter.CTkButton(
            self, text="Spustit", command=self.button_event)
        self.button.grid(row=10, column=1, padx=20, pady=10)

        # ?třetí sloupec
        self.label_sval2 = customtkinter.CTkLabel(self, text="sval2")
        self.label_sval2.grid(row=1, column=2, padx=20)

        self.progressbar2 = customtkinter.CTkProgressBar(
            self, orientation="horizontal")
        self.progressbar2.grid(row=2, column=2, padx=20)

        self.entry2 = customtkinter.CTkEntry(self, placeholder_text="entry2")
        self.entry2.grid(row=3, column=2, padx=20, pady=10)

        self.label_sval4 = customtkinter.CTkLabel(self, text="sval4")
        self.label_sval4.grid(row=7, column=2, padx=20)

        self.progressbar4 = customtkinter.CTkProgressBar(
            self, orientation="horizontal")
        self.progressbar4.grid(row=8, column=2, padx=20)

        self.entry4 = customtkinter.CTkEntry(self, placeholder_text="entry4")
        self.entry4.grid(row=9, column=2, padx=20, pady=10)

    #!funkce
        self.conversion_functions = {
            1: lambda entry_value: int(entry_value) * 2,   # přepočet mm
            2: lambda entry_value: int(entry_value) * 3,  # přepočet mbar
            3: lambda entry_value: int(entry_value) * 4,  # přepočet mV
            4: lambda entry_value: int(entry_value),  # přepočet kroky
        }

    def button_event(self):
        radio_value = radio_var.get()
        entry_values = [self.entry1.get(), self.entry2.get(
        ), self.entry3.get(), self.entry4.get(), self.entry5.get()]
        entry_values = [0 if not value else value for value in entry_values]

        conversion_function = self.conversion_functions.get(radio_value)

        if conversion_function is not None:
            results = [conversion_function(entry) for entry in entry_values]
            print(f"Jednotky {radio_value}")
            for i, result in enumerate(results, start=1):
                print(f"Sval {i} posun o {result}")
        else:
            print(
                "Není definována příslušná konverzní funkce pro tuto hodnotu radio buttonu.")


class RightFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        global radio_var

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self, text="right frame")
        self.label.grid(row=0, column=0, padx=20)

        radio_var = customtkinter.IntVar(value=0)
        self.radiobutton_1 = customtkinter.CTkRadioButton(self, text="mm",
                                                          command=self.radiobutton_event, variable=radio_var, value=1)
        self.radiobutton_1.grid(row=1, column=0, padx=20, pady=10)

        self.radiobutton_2 = customtkinter.CTkRadioButton(self, text="mbar",
                                                          command=self.radiobutton_event, variable=radio_var, value=2)
        self.radiobutton_2.grid(row=2, column=0, padx=20, pady=10)

        self.radiobutton_3 = customtkinter.CTkRadioButton(self, text="mV",
                                                          command=self.radiobutton_event, variable=radio_var, value=3)
        self.radiobutton_3.grid(row=3, column=0, padx=20, pady=10)

        self.radiobutton_3 = customtkinter.CTkRadioButton(self, text="kroky",
                                                          command=self.radiobutton_event, variable=radio_var, value=4)
        self.radiobutton_3.grid(row=4, column=0, padx=20, pady=10)

    def radiobutton_event(self):
        print("radiobutton toggled, current value:", radio_var.get())


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1060x400")
        self.maxsize(1060, 400)
        self.minsize(1060, 400)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.left_frame = LeftFrame(master=self)
        self.left_frame.grid(row=0, column=0, pady=20, sticky="nsew")

        self.main_frame = MainFrame(master=self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.right_frame = RightFrame(master=self)
        self.right_frame.grid(row=0, column=2, pady=20, sticky="nsew")


app = App()
app.mainloop()
