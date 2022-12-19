# 221006 수업
# 복습
#def open(filename, type)
    # filenmae 이 있냐
    # if type == 'w':
        # 글쓰기모드

# fr = open("./8888.txt",'r', encoding="UTF-8")
# lines = fr.readlines()
# for line in lines:
#     print(lines)
# fr.close()

# fw = open("./8888.txt", "w", encoding="UTF-8")
# print(lines)

# for line in lines:
#     if lines[0] == line:
#         print(lines[0])
#         a = input("바꿀 문장, 취소는 c ")
#         if a != "c":
#             fw.write(f"{a}\n")
#         elif a == "c":
#             fw.write(line)

#     elif lines[1] == line:
#         print(lines[1])
#         a = input("바꿀 문장, 취소는 c ")
#         if a != "c":
#             fw.write(f"{a}\n")
#         elif a == "c":
#             fw.write(line)

#     elif lines[2] == line:
#         print(lines[2])
#         a = input("바꿀 문장, 취소는 c ")
#         if a != "c":
#             fw.write(f"{a}\n")
#         elif a == "c":
#             fw.write(line)

#     elif lines[3] == line:
#         print(lines[3])
#         a = input("바꿀 문장, 취소는 c ")
#         if a != "c":
#             fw.write(f"{a}\n")
#         elif a == "c":
#             fw.write(line)
# fw.close()

fr = open("./8888.txt", 'r', encoding="UTF-8")
lines = fr.readlines()
fr.close

fw = open("./8888.txt", 'w', encoding="UTF-8")
for line in lines:
    update_text = input(f"전 문장 : {line} 바꿀 문장(c는 취소) : ")
    if update_text == "c":
        fw.write(line.strip())
    else:
        fw.write(update_text)
    fw.write("\n")
fw.close()



