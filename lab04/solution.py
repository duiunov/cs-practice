

def winner(names: list[str], scores: list[float]) -> str:
    name_win = ''
    max_scores = 0
    for i in range(0,len(scores)):
        if  scores[i] >  max_scores:
             max_scores = scores[i]
             name_win = names[i]
    return name_win

def average(scores: list[float]) -> float:
    return( round(sum(scores)/len(scores),1))



def ranking(names: list[str], scores: list[float]) -> list[str]:
    a = []
    scores_cope = []

    for i in range(0,len(scores)):
        scores_cope += [scores[i]]

    max_score = max(scores_cope)
    index_max = scores_cope.index(max_score)

    for i in range(0,len(names)):
        a += [names[index_max]]
        
        scores_cope[index_max] = 0
        
        max_score = max(scores_cope)
        index_max = scores_cope.index(max_score)

    return a
        


def above_average(names: list[str], scores: list[float]) -> list[str]:
    sred = average(scores)
    a = []
    for i in range(0,len(names)):
        if scores[i] > sred:
            a += [names[i]]
    return a



##names =  ["Аня", "Боря", "Вика"]
##scores = [7.0,   9.0,    9.0]
##print( winner(names, scores), average(scores) )
##
##print(ranking(names, scores) )
##
##print(above_average(names, scores))



