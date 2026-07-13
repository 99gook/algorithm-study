def solution(code):
    let = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i] != '1' and i % 2 == 0:
                let += code[i]
            elif code[i] == '1':
                mode = 1
        else :
            if code[i] != '1' and i % 2 == 1:
                let += code[i]
            elif code[i] == '1':
                mode = 0
    if let == '':
        return 'EMPTY'
    return let