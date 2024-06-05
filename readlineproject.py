with open("file handling.txt", "r") as f:
    while True:
        txt = f.readline()
        if not txt:  # If the line is empty, break the loop
            break

        parts = txt.strip().split(",")

        if len(parts) >= 3:
            m1 = parts[0]
            m2 = parts[1]
            m3 = parts[2]

            print(txt.strip())
            print(f"Marks of student in English: {m1}")
            print(f"Marks of student in Hindi: {m2}")
            print(f"Marks of student in Math: {m3}")
        else:
            print(f"Line does not have enough data: {txt.strip()}")
