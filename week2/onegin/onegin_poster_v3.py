from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 4320, 7680
MARGIN = 260
WORK_WIDTH = WIDTH - MARGIN*2
LINE_HEIGHT = 21
FONT = ImageFont.truetype(
    "/System/Library/Fonts/Supplemental/Georgia.ttf",
    16
)
SPACE_LEN_IN_PX = FONT.getlength(" ") # длина одного пробела в пикселях

with open("data/onegin.txt", encoding="utf-8") as file:
    text = file.read()
    words = text.split() # эта переменная типа СПИСОК со всеми словами РОМАНА

print(f"Кол-во слов: {len(words)}")

lines = []
line = words[0]

for word in words[1:]:
    longer = line + " " + word
    longer_length_in_pixels = FONT.getlength(longer) # ДЛИНА СТРОКИ В ПИКСЕЛЯХ
    if longer_length_in_pixels <= WORK_WIDTH:
        line = longer
    else:
        lines.append(line) # cтрока полная - слово идёт в новую строку
        line = word # начинаем новую строку с этого слова
lines.append(line)
print(f"Кол-во строк на изображении: {len(lines)}")

image = Image.new("RGB", (WIDTH, HEIGHT), "#FFFFFF")
draw = ImageDraw.Draw(image)
######################################
evgenys = []
tatianas = []
######################################
y = MARGIN

for line in lines:
    #=====================================================================
    # Новый кусок кода, чтобы было выравнивание по ширине (неидеальное но плюс-минус 2 пикселя)
    cur_line_len = FONT.getlength(line)
    num_spaces_left = int(round((WORK_WIDTH - cur_line_len) / SPACE_LEN_IN_PX, 0))
    cur_spaces_counter = 0
    justified_line = ""
    for symbol in line:
        if symbol == " " and cur_spaces_counter < num_spaces_left:
            symbol = " " * 2
            cur_spaces_counter += 1
        justified_line += symbol
    print(f"New line width is not aligned: {abs(FONT.getlength(justified_line)-WORK_WIDTH)} px")
    #=====================================================================
    line = justified_line
    draw.text((MARGIN, y), line, font=FONT, fill="#3C3A34")
    ########################################################################
    x = MARGIN
    for word in line.split(" "):
        if "Евген" in word or "Онеги" in word:
            evgenys.append((x, y + LINE_HEIGHT))
        if "Татьян" in word or "Тан" in word:
            tatianas.append((x, y + LINE_HEIGHT))
        x += FONT.getlength(word + " ")
    #########################################################################
    y = y + LINE_HEIGHT


#################################
print(f"Кол-во Евгениев: {len(evgenys)}. Кол-во Татьян: {len(tatianas)}. Колв-во СВЯЗЕЙ: {len(evgenys) * len(tatianas)}")

pen = ImageDraw.Draw(image, "RGBA")
for evgeny in evgenys:
    for tatiana in tatianas:
        pen.line([evgeny, tatiana], fill=(190, 40, 40 ,40), width=3)


#################################

image.save("onegin_poster.png")
print("ВСЁ ГОТОВО!!!")
print("Hello world!")