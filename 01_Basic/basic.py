'''
print("Hello World")
print is the function in python 

1) MODULE
  Module is a file containing code written by somebody esle(usually) which can be imported and used in our programs.

  ex:-> 
      import pyjokes

        joke = pyjokes.get_joke()
        print(joke)

2) PIP
  Pip is the package manager for python, We can use pip to install a module on our system. 

3) Using Python as Calculator
  we can use python as a calculator by "python" + on the terminal
 this opens REPL (Read Evaluate Print Loop) it means it read the given condition and evaluate it and print the ans and goes to loop.


'''
# Step 1: Take inputs
load_kw = float(input("Enter load (kW): "))
pf = float(input("Enter power factor: "))
distance = float(input("Enter cable length (m): "))

# Step 2: Convert kW → kVA
kva = load_kw / pf

# Step 3: Transformer sizing
standard_sizes = [25, 63, 100, 160, 200, 250, 315, 500]
transformer = next(size for size in standard_sizes if size > kva)

# Step 4: Current calculation
I = kva * 1000 / (1.732 * 400)

# Step 5: Cable selection table (Ampacity)
cable_chart = {
    35: 90,
    50: 110,
    70: 140,
    95: 170,
    120: 200,
    150: 230,
}

# Step 6: Pick correct cable based on ampacity
selected_cable = next(size for size, amp in cable_chart.items() if amp > I)

# Step 7: Resistance table
resistance = {
    35: 0.524,
    50: 0.387,
    70: 0.268,
    95: 0.193,
    120: 0.153,
    150: 0.124
}

# Step 8: Voltage drop calculation
R = resistance[selected_cable]
VD = (1.732 * I * distance * R) / 1000  # Volts
VD_percent = (VD / 400) * 100

# Output
print("Transformer Size:", transformer, "kVA")
print("Current:", round(I, 2), "A")
print("Cable Selected:", selected_cable, "sqmm")
print("Voltage Drop:", round(VD, 2), "V")
print("Voltage Drop %:", round(VD_percent, 2), "%")

# Voltage Drop Warning
if VD_percent > 5:
    print("\n⚠ WARNING: Voltage drop is TOO HIGH! (More than 5%)")
    print("❌ Cable size is NOT acceptable for this distance.")
    print("👉 Consider:")
    print("- Using a larger cable size")
    print("- Installing transformer closer to load")
    print("- Using 11 kV distribution instead of 400 V")
elif VD_percent > 3:
    print("\n⚠ NOTICE: Voltage drop between 3% - 5%")
    print("✔ Acceptable only for power loads (NOT lighting)")
else:
    print("\n✔ Voltage drop is within safe limits")
