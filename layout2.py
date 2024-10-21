import tkinter as tk
from tkinter import ttk

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
    "40.5",
    "10.75",
    "19.25",
    "47.50",
    "33",
    "105.25",
]


ingridientList = [
    "Wheat Flour (with Vit. A and Iron),\n Purified Water, Washed Sugar, Pure Vegetable Shortening\n (contains Palm Oil and/or Coconut Oil), Baker's Yeast,\n Iodized Salt, Dough Improver and Calcium Propionate.",
    "Water, Sugar, Banana, Modified Starch\n as Stabilizer, Iodized Salt, Spices, Vinegar, Sodium Benzoate\n as Preservative, Artificial Colors and Artificial\n Flavor added.",
    "Water, Blend of Hydrolyzed and Naturally\n Fermented Soybean, Wheat, Iodized Salt, Caramel, and Spices.\n Contains Preservatives: Monosodium Glutamate (MSG),\n Sodium Benzoate as preservative, Monosodium Glutamate\n (flavor enhancer) and Sodium Guanylate as flavor enhancers, and Yeast Extract.",
    "INSTRUCTIONS Liver Warning. This product contains\n paracetamol. Severe liver damage may occur if: an adult\n or child 12 years old and above takes more than\n 4g of paracetamol in 24 hours, which is the maximum daily\n amount; taken with other medicines containing paracetamol\n (or acetaminophen); an adult has 3 or more alcoholic drinks everyday\n while using this product. Do not use with any other medicine containing\n paracetamol (prescription or nonprescription). Ask a doctor before use\n if the patient has kidney or liver problems. Ask a doctor before use if\n the patient is taking warfarin, blood thinning medicine. Stop use\n and ask a doctor if: new symptoms occur; symptoms do not get better; redness or swelling is\n present; fever gets worse or lasts more than 3 days; pain gets worse or lasts more than 10\n days. If pregnant or breastfeeding, ask a doctor before use. Overdose\n Warning: If more than the recommended dosage has been given, consult a doctor\n or contact a Poison Control Center right away. Quick medical attention is important even if you do not\n notice any signs or symptoms because of the risk of delayed, serious liver damage.",
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

# window
window = tk.Tk()
window.attributes('-fullscreen', True)
window.title('Grid')
window.geometry('600x400')

# define a grid
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 1)
window.columnconfigure(3, weight = 1)
window.columnconfigure(4, weight = 1)
window.columnconfigure(5, weight = 1)
window.columnconfigure(6, weight = 3)

window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 2)
window.rowconfigure(3, weight = 2)
window.rowconfigure(4, weight = 1)
window.rowconfigure(5, weight = 1)

def labelChanger(a,b,c,d,e,f,g):
    # widgets 
    label0 = ttk.Label(window, text = g, anchor= 'center', borderwidth = '1', relief= "solid")
    label1 = ttk.Label(window, text = a, anchor= 'center', borderwidth = '1', relief= "solid")
    label2 = ttk.Label(window, text = b, anchor= 'center', borderwidth = '1', relief= "solid")
    label3 = ttk.Label(window, text = c, anchor= 'center', borderwidth = '1', relief= "solid")
    label4 = ttk.Label(window, text = d, anchor= 'center', borderwidth = '1', relief= "solid")
    label5 = ttk.Label(window, text = e, anchor= 'center', borderwidth = '1', relief= "solid")
    label6 = ttk.Label(window, text = f, anchor= 'center', borderwidth = '1', relief= "solid")


    # place a widget
    label0.grid(row = 0, column = 2, columnspan = 2, sticky = 'nsew')
    label1.grid(row = 1, column = 1, sticky = 'nsew')
    label2.grid(row = 1, column = 2, columnspan = 2, sticky = 'nsew')
    label3.grid(row = 1, column = 4, sticky = 'nsew')
    label4.grid(row = 2, column = 1, rowspan = 2, columnspan = 4, sticky = 'nsew')
    label5.grid(row = 4, column = 1, columnspan = 2, sticky = 'nsew')
    label6.grid(row = 4, column = 3, columnspan = 2, sticky = 'nsew')

label7 = ttk.Button(window, text = 'Text to Speech')
label8 = ttk.Button(window, text = 'Display Nutrition Facts')

codeEntry = ttk.Entry(window)

label7.grid(row = 0, column = 6, rowspan = 3, sticky = 'nsew')
label8.grid(row = 3, column = 6, rowspan = 3, sticky = 'nsew')
codeEntry.grid(row = 5, column = 2, rowspan = 2)

#sample
def func(entry):

    sampleText = codeEntry.get()
    
    if sampleText == barCode[0]:
        print("prod1")
        labelChanger(categoryList[0], productList[0], priceList[0], ingridientList[0], allergensList[0], expDateList[0], barCode[0])
    if sampleText == barCode[1]:
        print("prod2")
        labelChanger(categoryList[1], productList[1], priceList[1], ingridientList[1], allergensList[1], expDateList[1], barCode[1] )
    if sampleText == barCode[2]:
        print("prod3")
        labelChanger(categoryList[2], productList[2], priceList[2], ingridientList[2], allergensList[2], expDateList[2], barCode[2])
    if sampleText == barCode[3]:
        print("prod4")
        labelChanger(categoryList[3], productList[3], priceList[3], ingridientList[3], allergensList[3], expDateList[3], barCode[3])
    if sampleText == barCode[4]:
        print("prod5")
        labelChanger(categoryList[4], productList[4], priceList[4], ingridientList[4], allergensList[4], expDateList[4], barCode[4])
    if sampleText == barCode[5]:
        print("prod6")
        labelChanger(categoryList[5], productList[5], priceList[5], ingridientList[5], allergensList[5], expDateList[5], barCode[5])


    codeEntry.delete(0, tk.END)



window.bind('<Return>', func)

# run
window.mainloop()




