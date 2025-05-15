with open("27B.txt") as f:
    f.readline() # читаем первую строку "в пустоту"
    data = [] # список точек
    for s in f:
        s = s.replace(",", ".") # если файл "кривой"
        p = [float(c) for c in s.split()] # читаем координаты x и y
        data.append(p)
    
    # ф-ла в условии     
    def dist(p1, p2):
        x1, y1, x2, y2 = *p1, *p2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # автоматическое разделение на кластеры
    def getCluster(p0):
        cluster = [p for p in data if dist(p0, p) < 0.3] # список из точек, которые находятся в ближайшей окрестности от p0
        #  P.S если рассматривать файл B, то возможно расстояние м-у кластерами < 1, следовательно диапазон нужно уменьшить
        if len(cluster) > 0:
            for p in cluster: data.remove(p) # удаляем точки из общ.списка, чтобы повторно их не брать
            next_cluster = [getCluster(p) for p in cluster] # для тех точек, которых мы нашли, ищем соседей 
            cluster += sum(next_cluster, [])
        return cluster
    
    clusters = [] 
    while len(data) > 0: # пока точки в списке есть
        p0 = data.pop() 
        cluster = [p0] + getCluster(p0) # берем первую точку и находим для нее класиер
#       print(len(cluster))
        clusters.append(cluster)
        
    k = len(clusters) 
        
    def centr(kl):
        m = []
        for p in kl:
            s = sum(dist(p, p1) for p1 in kl) # посчитали расстояние точки до каждой из точек кластора и сложили
            m.append([s, p])
        return min(m)[1]
        
    centroid = [centr(kl) for kl in clusters] # находим центроид для каждого из кластеров
    
    px = sum(x for x, y in centroid)
    py = sum(y for x, y in centroid)
    print(int(px / k * 10000), int(py / k * 10000))
