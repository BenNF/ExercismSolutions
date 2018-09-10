class Allergies(object):

    def __init__(self, score):
        temp_list = ['eggs','peanuts','shellfish','strawberries','tomatoes','chocolate','pollen','cats']
        temp_list = temp_list[::-1]
        self.list = []
        print(temp_list)
        bin_val = '{0:08b}'.format(score)[-8:]
        print(len(bin_val))
        print(bin_val)
        for x in range(0,8):
            if bin_val[x] == '1':
                self.list.append(temp_list[x])
    def is_allergic_to(self, item):
        return item in self.list
    @property
    def lst(self):
        return self.list

