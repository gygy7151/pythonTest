def solution(movie):
    answer = []
    temp = []
    movie_names = list(set(movie))
    for m_name in movie_names:
        viewer_num = movie.count(m_name)
        temp.append((viewer_num, m_name))
    temp.sort(key = lambda x : (-x[0], x))
    for viewer_num, movie_name in temp:
        answer.append(movie_name)
    return answer