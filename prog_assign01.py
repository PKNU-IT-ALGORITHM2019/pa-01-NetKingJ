# 단어 찾기(순환검색)
def fi_search(words, target, begin, end):
    if begin > end:
        if words[end]:
            return end
        else:
            return -1
    else:
        middle = int((begin + end) / 2)
        if words[middle] == target:
            return middle
        elif words[middle] > target:
            return fi_search(words, target, begin, middle - 1)
        else:
            return fi_search(words, target, middle + 1, end)


if __name__ == "__main__":
    word_lines = []
    word_list = []
    pos = []
    while True:
        cmd = input("$ ")

        if len(cmd.split()) == 2:
            cmd2 = cmd.split()[1]

        cmd1 = cmd.split()[0]
        
        if cmd1 == "size":
            print(len(word_lines))

        if cmd1 == "read":
            fi = open(cmd2, 'r', encoding='utf-8')
            while True:
                word_line = fi.readline()
                if not word_line:
                    break
                if word_line == '\n':
                    continue
                word_lines.append(word_line.split('\n')[0])

            for i in word_lines:
                word_list.append(i.split()[0].lower())
                pos.append(i.split()[1])

        if cmd1 == "find":
            word = cmd2.lower()
            temp = fi_search(word_list, word, 0, len(word_list) - 1)
            
            if word in word_list:
                print(word_lines[temp])
                count = 1
                while True:
                    temp = temp + 1
                    if word in word_list[temp]:
                        count = count + 1
                        print(word_lines[temp])
                    else:
                        break
                print("Found",count,"items")
            else:
                print("Not Found.")
                print(word_lines[temp].split()[0],word_lines[temp].split()[1])
                print("- - -")
                print(word_lines[temp + 1].split()[0],word_lines[temp+1].split()[1])

        if cmd1 == "exit":
            break
