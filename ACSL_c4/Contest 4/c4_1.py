def buildTree(word):
    one_d_array = []

    current_len = 0
    for k in range(len(word)):
        current_len = (2 * current_len) + 2

    for r in range(current_len):
        one_d_array.append(None)

    for i, j in enumerate(word):
        if i == 0:
            one_d_array[0] = j
        else:
        
            trigger = False
            num = 0
            while not trigger:
                if j > one_d_array[num]:
                    if one_d_array[(2*num) + 2] == None:
                        one_d_array[(2*num) + 2] = j
                        trigger = True
                    else:
                        num = (2*num) + 2
                
                if j <= one_d_array[num]:
                    if one_d_array[(2*num) + 1] == None:
                        one_d_array[(2*num) + 1] = j
                        trigger = True 
                    else:
                        num = (2*num) + 1
    


    final_thing = ""
    space_counter = 0
    word_counter = 1

    while word_counter < len(word):
        for n in range(len(one_d_array)):
            if n != 0:
                if one_d_array[n] == None:
                    space_counter += 1
                else:
                    final_thing += str(space_counter) + " "
                    space_counter = 0
                    word_counter += 1

    print(final_thing)


if __name__ == "__main__":
    print("SAMPLE INPUT:")
    buildTree("GASTON")
    buildTree("DUMBO")
    buildTree("SIMBA")
    buildTree("PETERPAN")
    buildTree("RAPUNZEL")
    buildTree("PINOCCHIO")
    print("-----------------")
    print("TEST INPUT:")
    buildTree("ARIEL")
    buildTree("JASMINE")
    buildTree("CINDERELLA")
    buildTree("BUZZLIGHTYEAR")
    buildTree("SLEEPINGBEAUTY")
    buildTree("AA")