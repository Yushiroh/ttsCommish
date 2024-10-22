import os
os.system("export DISPLAY=:0")

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)



barCode = [
    "4800344001413",
    "014285002789",
    "4800496818082",
    "4807788561848",
    "4806504712175",
    "4800361015110"
]

categoryList = [
    "Bread",
    "Condiments",
    "Condiments",
    "Medicine",
    "Canned Goods",
    "Dairy"
]


productList = [
    "Pinoy Tasty (450g)",
    "UFC Banana Catsup (100g)",
    "Silver Swan Soy Sauce (350mL)",
    "Biogesic 500mg (10 tablets)",
    "Mega Mama Hot & Spicy Tuna (155g)",
    "Nestle Fresh Mlik (1000 mL)",
]

priceList = [
    "40.5 PHP",
    "PHP PHP",
    "19.25 PHP",
    "47.50 PHP",
    "33 PHP",
    "105.25 PHP",
]


ingridientList = [
    "Wheat Flour (with Vit. A and Iron),\n Purified Water, Washed Sugar, Pure Vegetable Shortening\n (contains Palm Oil and/or Coconut Oil), Baker's Yeast,\n Iodized Salt, Dough Improver and Calcium Propionate.",
    "Water, Sugar, Banana, Modified Starch\n as Stabilizer, Iodized Salt, Spices, Vinegar, Sodium Benzoate\n as Preservative, Artificial Colors and Artificial\n Flavor added.",
    "Water, Blend of Hydrolyzed and Naturally\n Fermented Soybean, Wheat, Iodized Salt, Caramel, and Spices.\n Contains Preservatives: Monosodium Glutamate (MSG),\n Sodium Benzoate as preservative, Monosodium Glutamate\n (flavor enhancer) and Sodium Guanylate as flavor enhancers, and Yeast Extract.",
    "INSTRUCTIONS Liver Warning. This product contains paracetamol. Severe liver\n damage may occur if: an adult or child 12 years old and above takes more than\n 4g of paracetamol in 24 hours, which is the maximum daily amount; taken with\n other medicines containing paracetamol (or acetaminophen); an adult has 3 or\n more alcoholic drinks everyday while using this product. Do not use with any\n other medicine containing paracetamol (prescription or nonprescription). Ask a\n doctor before use if the patient has kidney or liver problems. Ask a doctor\n before use if the patient is taking warfarin, blood thinning medicine. Stop use\n and ask a doctor if: new symptoms occur; symptoms do not get better; redness or\n swelling is present; fever gets worse or lasts more than 3 days; pain gets worse\n or lasts more than 10 days. If pregnant or breastfeeding, ask a doctor before\n use. Overdose Warning: If more than the recommended dosage has been given,\n  consult a doctor or contact a Poison Control Center right away. Quick medical\n attention is important even if you do not notice any signs or symptoms because\n of the risk of delayed, serious liver damage.",
    "Tuna flakes, water, soy protein concentrate,\n soya bean oil, spices, monosodium glutamate\n (flavor enhancer), iodized salt, chili powder,\n sugar, and bayleaf",
    "Fresh Cow's Milk"
]

allergensList = [
    "Wheat",
    "Soybeans",
    "Soybean and Wheat",
    "N/A",
    "Fish and Soy",
    "Milk",
]

expDateList = [
    "October 18, 2024",
    "April 7, 2025",
    "October 2026",
    "February 2028",
    "May 25, 2027",
    "March 11, 2025"
]

descTTS = ["1a", "2a", "3a","4a", "5a", "6a"]

nfTTS = ["1b", "2b", "3b","4b", "5b", "6b"]

nfPics = ["nf1", "nf2", "nf3", "nf4", "nf5", "nf6"]

ttsMode = 1


# window
window = tk.Tk()
window.attributes('-fullscreen', True)
window.title('Grid')
window.geometry('600x400')

# define a grid
window.columnconfigure((0,1,2,3), weight = 1)

window.rowconfigure((0,1,3), weight = 1)
window.rowconfigure(2, weight = 4)



def ttsFunc(aString,bString):

    if ttsMode == 1:
        os.system(f'mpg123 recordings/{aString}.mp3')
    else:
        os.system(f'mpg123 recordings/{bString}.mp3')

    


def nfFunc(nfInherit):
    global ttsMode
    
    if nfInherit == "nf5":
        nfDisplay = ImageTk.PhotoImage(Image.open(f"nfimg/{nfInherit}.PNG").resize((317,380)))
    else:
        nfDisplay = ImageTk.PhotoImage(Image.open(f"nfimg/{nfInherit}.PNG"))
    panel = tk.Label(window, image=nfDisplay)
    panel.image = nfDisplay
    panel.grid(column=0, row=2, columnspan = 4, sticky='nsew')
    ttsMode = 0
    


def labelChanger(a,b,c,d,e,f,g):
    # widgets 
    label0 = ttk.Label(window, text = g, anchor= 'center', borderwidth = '1', relief= "solid", font = ('Arial', 16))
    label1 = ttk.Label(window, text = a, anchor= 'center', borderwidth = '1', relief= "solid", font = ('Arial', 16))
    label2 = ttk.Label(window, text = b, anchor= 'center', borderwidth = '1', relief= "solid", font = ('Arial', 16))
    label3 = ttk.Label(window, text = c, anchor= 'center', borderwidth = '1', relief= "solid", font = ('Arial', 16))
    label4 = ttk.Label(window, text = d, anchor= 'center', borderwidth = '1', relief= "solid", font = ('Arial', 16))
    label5 = ttk.Label(window, text = e, anchor= 'center', borderwidth = '1', relief= "solid", font = ('Arial', 16))
    label6 = ttk.Label(window, text = f, anchor= 'center', borderwidth = '1', relief= "solid", font = ('Arial', 16))


    # place a widget
    label0.grid(row = 0, column = 1, columnspan = 2, sticky = 'nsew')
    label1.grid(row = 1, column = 0, sticky = 'nsew')
    label2.grid(row = 1, column = 1, columnspan = 2, sticky = 'nsew')
    label3.grid(row = 1, column = 3, sticky = 'nsew')
    label4.grid(row = 2, column = 0, columnspan = 4, sticky = 'nsew')
    label5.grid(row = 3, column = 0, columnspan = 2, sticky = 'nsew')
    label6.grid(row = 3, column = 2, columnspan = 2, sticky = 'nsew')


codeEntry = ttk.Entry(window)
codeEntry.focus_set()
codeEntry.grid(row = 4, column = 1, rowspan = 2, sticky = 'nsew')


#sample
def func(entry):
    global ttsMode
    global storedDesc
    global storedNF
    global storedPic
    ttsMode = 1
    sampleText = codeEntry.get()
    
    if sampleText == barCode[0]:
        print("prod1")
        labelChanger(categoryList[0], productList[0], priceList[0], ingridientList[0], allergensList[0], expDateList[0], barCode[0])
        storedDesc = descTTS[0]
        storedNF = nfTTS[0]
        storedPic = nfPics[0]

    if sampleText == barCode[1]:
        print("prod2")
        labelChanger(categoryList[1], productList[1], priceList[1], ingridientList[1], allergensList[1], expDateList[1], barCode[1] )
        storedDesc = descTTS[1]
        storedNF = nfTTS[1]
        storedPic = nfPics[1]

    if sampleText == barCode[2]:
        print("prod3")
        labelChanger(categoryList[2], productList[2], priceList[2], ingridientList[2], allergensList[2], expDateList[2], barCode[2])
        storedDesc = descTTS[2]
        storedNF = nfTTS[2]
        storedPic = nfPics[2]

    if sampleText == barCode[3]:
        print("prod4")
        labelChanger(categoryList[3], productList[3], priceList[3], ingridientList[3], allergensList[3], expDateList[3], barCode[3])
        storedDesc = descTTS[3]
        storedNF = nfTTS[3]
        storedPic = nfPics[5]

    if sampleText == barCode[4]:
        print("prod5")
        labelChanger(categoryList[4], productList[4], priceList[4], ingridientList[4], allergensList[4], expDateList[4], barCode[4])
        storedDesc = descTTS[4]
        storedNF = nfTTS[4]
        storedPic = nfPics[3]

    if sampleText == barCode[5]:
        print("prod6")
        labelChanger(categoryList[5], productList[5], priceList[5], ingridientList[5], allergensList[5], expDateList[5], barCode[5])
        storedDesc = descTTS[5]
        storedNF = nfTTS[5]
        storedPic = nfPics[4]

    codeEntry.delete(0, tk.END)
    
def nfEvent(pin):
    global storedPic
    nfFunc(storedPic)

def ttsEvent(pin):
    global storedDesc, storedNF
    ttsFunc(storedDesc, storedNF)

GPIO.add_event_detect(8, GPIO.RISING, callback=nfEvent, bouncetime= 500) 
GPIO.add_event_detect(10, GPIO.RISING, callback=ttsEvent, bouncetime= 500)

window.bind('<Return>', func)


# run
window.mainloop()

print(f"{GPIO.input(10)}|{GPIO.input(8)}")



