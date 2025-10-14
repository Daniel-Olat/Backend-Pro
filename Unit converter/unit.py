import tkinter as tk 

class UnitConverter:
  def __init__(self):
    self.window = tk.Tk()
    self.window.title =  "UNIT CONVERTER"
    self.window.geometry = "250x200"
    
    #input Labels
    self.input_label = tk.Label(self.window , text="Enter a value: ")
    self.input_label.grid(column=0 , row=0)
    self.input_entry = tk.Label(self.window)
    self.input_entry.grid(column=1 , row = 0)
    #
    self.from_label = tk.Label(self.window , text="From: ")
    self.from_label.grid(column=0 ,row=1)
    #
    self.base_unit = tk.StringVar(self.window)
    self.base_unit.set("meters")
    #
    self.base_menu = tk.OptionMenu(self.window , self.base_unit , 'meters' , 'feet' , 'kilometers' , 'inches')
    self.base_menu.grid(column=1 , row=1)
    #
    self.to_label = tk.Label(self.window , text="To: ")
    self.to_label.grid(column=0 , row=2)
    #
    self.target_unit = tk.StringVar(self.window)
    self.target_unit.set("feet")
    #
    self.target_menu = tk.OptionMenu(self.window , self.target_unit , 'meters' , 'feet' , 'kilometers' , 'inches')
    self.target_menu.grid(column=1,row=2)
    #
    self.convert_button = tk.Button(self.window , text="Convert" , command=self.convert)
    self.convert_button.grid(column=0 , row=3)
    
    #
    self.ouptut_label = tk.Label(self.window , text="")
    self.ouptut_label.grid(column=0 ,row=4)
    
    self.window.mainloop()
    
  def convert(self):
    #converting the user's value to a float
    input_value = float(self.input_entry.get())
  
    #Convert every entry unit into meters to simplify logic :)
    if self.base_unit.get() == 'feet':
      meter_value = input_value * 0.3048
    elif self.base_unit.get() == 'inches':
      meter_value = input_value * 0.0245
    elif self.base_unit == 'kilometers':
      meter_value = input_value*1000
    else:
      output_value = input_value
      
    #
    if self.target_unit.get() == 'feet':
      output_value = meter_value /0.3048
    elif self.target_unit.get() == 'inches':
      output_value = meter_value / 0.0254
    elif self.target_unit.get() == 'kilometers':
      output_value = meter_value/1000
    else:
      output_value = meter_value
      
      
    #
    self.ouptut_label.config(text = str(output_value) , fg='green')
converter = UnitConverter()