class loadFood:

    def __init__(self, filename):

        self.menu_list= []
        self.menu_str=""
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            menu = line.rstrip()
            self.menu_list.append(menu)
            self.count += 1

        for i in self.menu_list:
            self.menu_str+= str(i + "\n")



if __name__ == "__main__":
    practice =  loadFood('분식.txt')
    print(practice.menu_list)