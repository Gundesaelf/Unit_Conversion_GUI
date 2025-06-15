# |---------------------------------IMPORTS---------------------------------|

import customtkinter as ctk

# |---------------------------------APP_CLASS---------------------------------|

class App(ctk.CTk):
    def __init__(self, master= None, **kwargs):
        super().__init__(master, **kwargs)
        self.title('Unit Conversion GUI')
        self.geometry('480x420')
        self.resizable(False, False)
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')

        tabview = ctk.CTkTabview(
            self,
            border_color='gray',
            border_width= 2
        )
        tabview.grid(row= 0, column= 0, padx=20, pady=20, sticky= 'nsew')
        tabview.columnconfigure(0, weight= 1)
        tabview.columnconfigure(1, weight= 0)
        tabview.columnconfigure(2, weight= 1)
        
        unit_conversion_tab = tabview.add('Unit Conversion')
        
        tabview.set('Unit Conversion')

        self.unit_conversion_ui = UnitConversionUI(unit_conversion_tab)

# |---------------------------------UNIT_CONVERSION---------------------------------|

class UnitConversionUI(ctk.CTkFrame):
    def __init__(self, parent):
        self.conversion_method_option_menu_label = ctk.CTkLabel(
            parent,
            text= 'Select Conversion Method:',
            font= ('Arial', 15),
            text_color= 'white',
            fg_color= 'transparent'
        )

        self.conversion_method_option_menu_label.grid(row= 0, column= 0, pady=(10, 5), padx=(110, 110))

        self.conversion_method_option_menu = ctk.CTkOptionMenu(
            parent,
            values= ['Inches to Centimeters', 'Centimeters to Inches'],
            width= 200,
            height= 30,
            font= ('Arial', 15),
            text_color= 'white',
            fg_color= '#1f1f1f',
            button_color= '#355fad',
            button_hover_color= '#27497c',
            anchor= 'center'
        )

        self.conversion_method_option_menu.grid(row= 1, column= 0, pady=(5, 10), padx=(110, 110))

        self.number_to_convert_label = ctk.CTkLabel(
            parent,
            text= 'Number to Convert:',
            font= ('Arial', 15),
            text_color= 'white',
            fg_color= 'transparent'
        )

        self.number_to_convert_label.grid(row= 2, column= 0, pady=(10, 5), padx=(110, 110))

        self.number_to_convert_entry = ctk.CTkEntry(
            parent,
            width= 100,
            height= 30,
            font= ('Arial', 15),
            text_color= 'white',
            fg_color= '#1f1f1f',
            border_color= 'gray',
            border_width= 2,
            justify= 'center'
        )

        self.number_to_convert_entry.grid(row= 3, column= 0, pady=(5, 10), padx=(110, 110))

        self.calculate_button = ctk.CTkButton(
            parent,
            text= 'Calculate!',
            font= ('Arial', 15, 'bold'),
            text_color= 'white',
            fg_color= '#355fad',
            hover_color= '#27497c',
            border_color= 'gray',
            border_width= 2,
            corner_radius= 25,
            command= lambda: self.calculate_conversion()
        )

        self.calculate_button.grid(row= 4, column= 0, pady=(5, 10), padx=(110, 110))

        self.conversion_result_label = ctk.CTkLabel(
            parent,
            text= 'Conversion Result',
            font= ('Arial', 15, 'underline', 'bold'),
            text_color= 'white',
            fg_color= 'transparent'
        )

        self.conversion_result_label.grid(row= 5, column= 0, pady=(30, 5), padx=(110, 110))

        self.result_label = ctk.CTkLabel(
            parent,
            text='',
            font=('Arial', 15, 'bold'),
            text_color='#5f93f2',
            width=200,
            height=40,
            fg_color='#1f1f1f',
            corner_radius=25,
            anchor='center'
        )

        self.result_label.grid(row= 6, column= 0, pady=(0, 5), padx=(110, 110))

    def calculate_conversion(self):
        conversion_method = self.conversion_method_option_menu.get()
        
        try:
            number_to_convert = float(self.number_to_convert_entry.get())
        except ValueError:
            self.result_label.configure(text='INVALID INPUT', text_color= '#cb5757')
            return

        if conversion_method == 'Inches to Centimeters':
            result = number_to_convert * 2.54
            self.result_label.configure(text=f'{result:.2f} cm', text_color='#5f93f2')
        elif conversion_method == 'Centimeters to Inches':
            result = number_to_convert / 2.54
            self.result_label.configure(text=f'{result:.2f} in', text_color='#5f93f2')
        else:
            self.result_label.configure(text='INVALID METHOD', text_color= '#cb5757')

# |---------------------------------MAIN_LOOP---------------------------------|

if __name__ == '__main__':
    root = App()
    root.mainloop()
    