# Declaring the constant values of specific heat of solid water, liquid, and vapor in that order.
CPS = 2.180
CPL = 4.184
CPV = 1.996
# Declaring the constant values of latent heat of fusion and vaporization in that order.
LHF = 334
LHV = 2260

print("Welcome to this enthalpy calculator!")

while True: 
    m_r = float(input("Please enter your mass flow rate: "))
    if m_r < 0:
        print("Please enter a valid mass flow rate.")
        continue

    break


while True: 
    t_in = float(input("Please enter your starting temperature: "))
    if t_in < -273.15:
        print("Please enter a valid temperature.")
        continue

    break


while True: 
    t_out = float(input("Please enter your finishing temperature: "))
    if t_out < -273.15:
        print("Please enter a valid temperature.")
        continue

    break

Q_dot = m_r * CPL * (t_out - t_in)
print(Q_dot, "kW")