import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk

ctk.set_appearance_mode("Dark")  #Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")

class Application(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.grid_rowconfigure((0, 1), weight=1)

        #Create Tabview
        self.tabview = ctk.CTkTabview(self, width = 750)
        self.tabview.grid(row=0, padx=(20,0), pady=(20,0), sticky="nsew")
        self.tabview.add("Threshold Setter")
        self.tabview.add("Discrepancy Finder")

        self.tabview.tab("Threshold Setter").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Threshold Setter").grid_rowconfigure(1, weight=0)
        self.tabview.tab("Threshold Setter").grid_columnconfigure((0, 1), weight=1)

        self.tabview.tab("Discrepancy Finder").grid_columnconfigure((0, 1, 2), weight=0)

        #Add widgets to main screen
        self.reset_button = ctk.CTkButton(self, text="Reset", width=100, height=50)
        self.reset_button.place(x=50, y=400)

        self.video_feed_button = ctk.CTkButton(self, text="Viewfinder", width=200, height=50)
        self.video_feed_button.place(x=300, y=400)

        self.exit_button = ctk.CTkButton(self, text="Exit", width = 100, height = 50)
        self.exit_button.place(x=650, y=400)

        #Add widgets to Threshold Setter Tab
        self.nominal_button = ctk.CTkButton(self.tabview.tab("Threshold Setter"), text="Nominal", width=200, height=100)
        self.nominal_button.grid(row=0, column=0, padx=0, pady=(10,10))

        self.discrepancy_button = ctk.CTkButton(self.tabview.tab("Threshold Setter"), text="Discrepancy", width=200, height=100)
        self.discrepancy_button.grid(row=0, column=1, padx=0, pady=(10,10))

        self.nominal_label = ctk.CTkLabel(self.tabview.tab("Threshold Setter"), font=ctk.CTkFont(size=20, weight="bold"))
        self.nominal_label.grid(row=1, column=0, padx=10, pady=(10,10))

        self.discrepancy_label = ctk.CTkLabel(self.tabview.tab("Threshold Setter"), font=ctk.CTkFont(size=20, weight="bold"))
        self.discrepancy_label.grid(row=1, column=1, padx=10, pady=(10,10))

        #Add widgets to Discrepancy Finder Tab
        self.tabview.tab("Discrepancy Finder").grid_columnconfigure((0, 1, 2), weight=1)
        self.tabview.tab("Discrepancy Finder").grid_rowconfigure(0, weight=1)
        # Add widgets to Settings column
        self.settings_frame = ctk.CTkFrame(self.tabview.tab("Discrepancy Finder"))
        self.settings_frame.grid(row=0, column=0, padx=(10, 0), pady=(20, 0), sticky="nsew")
        self.settings_frame.grid_columnconfigure(0, weight=1)
        self.settings_frame.grid_rowconfigure((0, 1, 2, 3), weight=0)
        self.label_settings_group = ctk.CTkLabel(master=self.settings_frame, text="Settings", font=ctk.CTkFont(size=30, weight="bold"))
        self.label_settings_group.grid(row=0, column=0, columnspan=1, padx=30, pady=10,)
        self.slider_threshold = ctk.CTkSlider(self.settings_frame, from_=0, to=99, number_of_steps=100)
        self.slider_threshold.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
        self.run_button = ctk.CTkButton(self.settings_frame, text="RUN")
        self.run_button.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

        #Add widgets to Run column
        self.runtime_frame = ctk.CTkFrame(self.tabview.tab("Discrepancy Finder"))
        self.runtime_frame.grid(row=0, column=1, padx=(10, 10), pady=(20, 0), sticky="nsew")

        self.label_runtime_group = ctk.CTkLabel(master=self.runtime_frame, text="Run", font=ctk.CTkFont(size=30, weight="bold"))
        self.label_runtime_group.grid(row=0, column=1, columnspan=1, padx=100, pady=10, )

        # Add widgets to Sequence Tab
        self.sequence_frame = ctk.CTkScrollableFrame(self.tabview.tab("Discrepancy Finder"))
        self.sequence_frame.grid(row=0, column=2, padx=(0, 10), pady=(20, 0), sticky="nsew")

        self.label_sequence_group = ctk.CTkLabel(master=self.sequence_frame, text="Sequence", font=ctk.CTkFont(size=30, weight="bold"))
        self.label_sequence_group.pack(padx=30, pady=4)

        options = ["Delay", "Image", "Switch On", "Switch Off"]

        for i in range(15):
            combobox = ctk.CTkComboBox(self.sequence_frame, values=options)
            combobox.pack(padx=(0, 0), pady=(10, 10))
            entry = ctk.CTkEntry(self.sequence_frame, width=7)
            entry.pack(padx=(0, 0), pady=(0, 0))


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x480")
    app = Application(master=root)
    app.mainloop()