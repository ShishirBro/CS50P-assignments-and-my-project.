import sys
from pyfiglet import Figlet

figlet = Figlet()
if len(sys.argv) == 1:
    figlet.setFont(font=figlet.getFonts()[0])
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    if sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
    else:
        print("Invalid usage")
        sys.exit(1)
else:
    print("Invalid usage")
    sys.exit(1)

text = input("Input text: ")
print(figlet.renderText(text))


