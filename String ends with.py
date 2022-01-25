def solution(string, ending):
    len_end = len(ending)

    if len_end == 0:
        return True
    else:
        if string[len_end*-1:] == ending:
            return True
        else:
            return False






print(solution('abcde', ''))