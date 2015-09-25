read_files = open("bit_stream.data")

begin_change = False
trans = {}  # define the null trans rules
out = {}  # define the null out rules
for line in read_files.readlines():
    line_words = line.strip().split(' ')
    # print line_words

    if not begin_change:
        if line_words[0] == 'start':
            begin_change = True
            states = line_words[1]
        else:
            trans[line_words[0], line_words[1]] = line_words[2]
            out[line_words[0], line_words[1]] = line_words[3]
    else:
        print out[states, line_words[0]]
        states = trans[states, line_words[0]]
