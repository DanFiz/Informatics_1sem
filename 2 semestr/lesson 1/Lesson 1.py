import os
import sys
def read_log(filename) -> list: #graphene_all_3351000..log
    with open(f'./Sem1_dimers_data/{filename}', 'r') as file:
        finded = False
        lines = file.readlines()
        #print(lines)
        for line in lines:
            words = line.split()
            if len(words) > 1:
                if words[0] == 'Atoms' and words[1] == 'Step':
                    finded = True
                    continue
            else:
                continue
            if finded:
                return words

#log_name = int(sys.argv[1])


data = read_log('graphene_all_3351000..log')

print(data)