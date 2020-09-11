G = 0
A = 0
T = 0
C = 0
with open ('Genomic sequence Mus musculus.fasta') as seq:
    datalist = []
    for line in seq:
        if line.startswith('>'):
            datalist.append([line.strip()[1:], ''])
        else:
            datalist[-1][1] += line.strip()
        for data in datalist:
            G = data[1].count('G')
            A = data[1].count('A')
            T = data[1].count('T')
            C = data[1].count('C')
            
            
            print("Guanine:", data[1].count('G'))
            print("Adenine:", data[1].count('A'))
            print("Thymine:", data[1].count('T'))
            print("Cytosine:", data[1].count('C'))
            
            lengte = G + A + T + C
            gc_count = data[1].count('G') + data[1].count('C') 
            if gc_count >1:
                gc_fraction = gc_count / lengte
                print("GC%: ", gc_fraction * 100)

