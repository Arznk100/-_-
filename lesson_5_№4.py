def complementary(hex_color):
    h = hex_color.lstrip("#")
    r = int(h[0:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)

    r2 = 255 - r
    g2 = 255 - b
    b2 = 255 - g

    return f"#{r2:02x}{g2:02x}{b2:02x}"


color = input("Введи HEX-цвет: ").strip()
print(complementary(color))