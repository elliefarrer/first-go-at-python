# Trying out some lists
tube_lines_ellie_hates = ["Metropolitan", "Bakerloo", "Central", "Piccadilly", "Northern"]

for line in tube_lines_ellie_hates:
    print("I hate the %s line" % line)

tube_lines_ellie_hates.append(raw_input("Which line do you hate today: "))
good_and_cool_line = tube_lines_ellie_hates.remove(raw_input("Which line is not that bad today: "))

tube_lines_ellie_hates.sort()

for line in tube_lines_ellie_hates:
    print("I really hate the %s line" % line)

for line in tube_lines_ellie_hates:
    if line[0] == "M":
        the_worst_line = line

print(("I hate the %s line so much!" % the_worst_line).upper())
