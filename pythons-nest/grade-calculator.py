#Grade Calculator
user_mark = float(raw_input("Enter your grade: "))
# --------------> in order to do division in Python, one of the numbers has to be a float
subject = raw_input("Enter the  subject: ")
max = 22;
print("User got %s/%s in %s" % (user_mark, max, subject))
# ----------> type is Python equivalent of typeof()
print("Subject is a %s whilst the mark is a %s. Max is %s" % (type(subject), type(user_mark), type(max)))

# -------------> round and 2 at the end rounds it to two dp
mark_in_percent = round(float(user_mark / max) * 100, 0)

if mark_in_percent > 90:
    result = "great!"
elif mark_in_percent <= 89 and mark_in_percent >= 70:
    result = "dope"
elif mark_in_percent <= 69 and mark_in_percent >= 50 and "f" in subject:
    result = "press f"
elif mark_in_percent <= 69 and mark_in_percent >= 50:
    result = "rubbish"
else:
    result = "get out, you are only worth %s grains of rice" % (len(subject))

print("You got %s/%s in %s, which is %s percent. That is %s" % (user_mark, max, subject, mark_in_percent, result))
