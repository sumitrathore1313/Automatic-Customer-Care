def get_simple_sentence_data(fname):
    """
    this function is used to create sentence data from aiml data files
    structure [inputs, outputs]
    :param fname: name of aiml file
    :return: return sentence data
    """
    with open(fname, 'r') as f:
        data = f.read().split()
        # print len(data), data[0:100], type(data[0])
        sentence_data = []
        inputs = []
        outputs = []
        temp = []
        i = 0
        ends = ['<category>', '</category>', '<pattern>', '</pattern>', '<template>', '</template>', '<random>',
                '</random>', '<li>', '</li>']
        while i < len(data):
            word = data[i]
            if word == '<category>':
                while word != '</category>':
                    if word == '<pattern>':
                        while word != '</pattern>':
                            if word not in ends:
                                temp.append(word)
                            i += 1
                            word = data[i]
                        inputs.append(" ".join(temp))
                        temp[:] = []

                    if word == '<template>':
                        while word != '</template>':
                            if word == '<random>':
                                while word != '</random>':
                                    if word == '<li>':
                                        while word != '</li>':
                                            if word not in ends:
                                                temp.append(word)
                                            i += 1
                                            word = data[i]
                                        outputs.append(" ".join(temp))
                                        temp[:] = []
                                    i += 1
                                    word = data[i]
                            if word not in ends:
                                temp.append(word)
                            i += 1
                            word = data[i]
                        outputs.append(" ".join(temp))
                        temp[:] = []
                    i += 1
                    word = data[i]
            else:
                i += 1
            for x in range(len(outputs)):
                sentence_data.append([inputs[0], outputs[x]])
            inputs = []
            outputs = []
    return sentence_data