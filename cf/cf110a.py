s = input()
print("YES" if set(str(s.count("4") + s.count("7"))) <= {"4", "7"} else "NO")
