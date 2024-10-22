def solution(sequence):
    l = len(sequence)
    seq1 = [sequence[i]*(-1)**(i%2) for i in range(l)]
    seq2 = [-sequence[i]*(-1)**(i%2) for i in range(l)]
    sum1 = seq1[0]
    sum2 = seq2[0]
    answer = max(sum1, sum2)
    for i in range(1, l):
        sum1 = max(seq1[i], sum1+seq1[i])
        sum2 = max(seq2[i], sum2+seq2[i])
        answer = max(sum1, sum2, answer)
    return answer