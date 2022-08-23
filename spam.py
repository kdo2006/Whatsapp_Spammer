import pywhatkit
import pyfiglet


ascii_banner = pyfiglet.figlet_format("Whatsapp Spammer by K.D.O")
print(ascii_banner)




print("\n")
print("Enter Target Number with Country code:",end=""),
number=(input())

# Asks for user to type a message
print("\n")
print("Enter message:",end=""),
message=str(input())


print("Enter massage amount:",end=""),
tim = int(input())

for i in range(tim):
    pywhatkit.sendwhatmsg_instantly(number, message, 10)


