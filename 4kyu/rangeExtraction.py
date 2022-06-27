def solution(args):
    new_ans = []
    args.append('Going Back')
    rangeOfNum = [args[0]]
    for i in range(1,len(args)):
        if args[i] != args[i-1] + 1:
            if len(rangeOfNum) == 1:
                new_ans.append(str(rangeOfNum[0]))
                rangeOfNum.clear()
            elif len(rangeOfNum) == 2:
                new_ans.append(rangeOfNum[0])
                new_ans.append(rangeOfNum[1])
                rangeOfNum.clear()
            elif len(rangeOfNum) > 2:
                new_ans.append(str(rangeOfNum[0]) + '-' + str(rangeOfNum[-1]))
                rangeOfNum.clear()
            else:
                new_ans.append(args[i])
                rangeOfNum.clear()
        rangeOfNum.append(args[i])
    new_ans = [str(i) for i in new_ans]
    return ','.join(new_ans)
