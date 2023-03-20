class Grafo:
    TAM_MAX_DEFAULT = 100  # qtde de vértices máxima default

    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT, r=False):
        self.n = n  # número de vértices
        self.m = 0  # número de arestas
        self.rot = r  # booleano se rotulado
        # matrizes de adjacência
        self.adj = [[0 for i in range(n)] for j in range(n)]

    # Insere uma aresta no Grafo tal que
    # v é adjacente a w
    def insereA(self, v, w, p=None):
        if p is not None and (self.adj[v][w] == 0):
            if not self.rot:
                print("[insereA] Erro: uso de peso em grafo nao rotulado")
                return
            self.adj[v][w] = p
            self.m += 1  # atualiza qtd arestas
        elif p is not None and (self.adj[v][w] != 0):
            print("[insereA] Aviso: tentativa de inserir aresta duplicada")
        elif p is None and (self.adj[v][w] == 0):
            self.adj[v][w] = 1
            self.m += 1  # atualiza qtd arestas
        elif p is None and (self.adj[v][w] != 0):
            print("[insereA] Aviso: tentativa de inserir aresta duplicada")
        else:
            print("[insereA] Erro: argumentos invalidos")

    # remove uma aresta v->w do Grafo
    def removeA(self, v, w):
        # testa se temos a aresta
        if self.adj[v][w] != 0:
            self.adj[v][w] = 0
            self.m -= 1  # atualiza qtd arestas


    def inDegree(self, v, c=None):
        ideg = 0
        for i in range(self.n):
            if self.adj[i][v] != 0:
                ideg += 1
        if c is None:
            print(f"Grau de entrada: {ideg}")
        return ideg

    def outDegree(self, v, c=None):
        odeg = 0
        for i in range(self.n):
            if self.adj[v][i] != 0:
                odeg += 1
        if c is None:
            print(f"Grau de saida: {odeg}")
        return odeg

    def fonte(self, v):
        if (self.inDegree(v, 1) == 0) and (self.outDegree(v, 1) > 0):
            print(f"Vertice {v} e uma fonte")
            return 1
        print(f"Vertice {v} nao e uma fonte")
        return 0

    def sorvedouro(self, v):
        if (self.inDegree(v, 1) > 0) and (self.outDegree(v, 1) == 0):
            print(f"Vertice {v} e um sorvedouro")
            return 1
        print(f"Vertice {v} nao e um sorvedouro")
        return 0

    def simetrico(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] == self.adj[j][i]:
                    continue
                else:
                    print("O grafo nao e simetrico")
                    return 0
        print("\nO grafo e simetrico")
        return 1

    def lerMatriz(self, file):
        nlinha = 0
        # Abrir o arquivo para leitura
        with open(file, "r") as arquivo:
            # Loop pelas linhas do arquivo
            for linha in arquivo:
                if nlinha == 1:
                    narestas = int(linha)
                elif 1 < nlinha <= (narestas + 1):
                    # Quebrar a linha em palavras
                    palavras = linha.split()
                    npalavra = 0
                    # Loop pelas palavras da linha
                    for palavra in palavras:
                        if npalavra == 0:
                            vert1 = int(palavra)
                        elif npalavra == 1:
                            vert2 = int(palavra)
                        npalavra += 1
                    # Criar aresta com vertices encontrados
                    self.insereA(vert1, vert2)
                nlinha += 1

    def removeVertice(self, v):
        for j in range(0,self.n-1):
            for i in range(0,self.n-1):
                if (i >= v) and (i < (self.n-1)):
                    if j < v:
                        self.adj[j][i] = self.adj[j][i+1]
                    elif j < (self.n-1):
                        self.adj[j][i] = self.adj[j+1][i+1]
                    else:
                        self.adj[j][i] = 0
                elif i == (self.n-1):
                    self.adj[j][i] = 0
                elif j == v:
                    self.adj[j][i] = self.adj[j+1][i + 2]
        print(f"\nRemovido o vertice {v}")
        self.n -= 1

    def completo(self):
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    continue
                elif self.adj[i][j] != 0:
                    continue
                else:
                    print("O grafo nao e completo")
                    return 0
        print("O grafo e completo")
        return 1

    # Apresenta o Grafo contendo
    # número de vértices, arestas
    # e a matriz de adjacência obtida
    def show(self):
        print("\nGrafo direcionado")
        print(f"n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}")
        print(f"rotulado: {self.rot}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] != 0:
                    print(f"Adj[{i:2d},{w:2d}] = {self.adj[i][w]} ", end="")
                else:
                    print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
            print("\n")
        if self.rot:
            for i in range(self.n):
                for w in range(self.n):
                    if self.adj[i][w] != 0:
                        print(f"Peso ({i:2d},{w:2d}) = {self.adj[i][w]} ", end="")
                print("\n")
        print("\nfim da impressao do grafo.")

    # Apresenta o Grafo contendo
    # número de vértices, arestas
    # e a matriz de adjacência obtida
    # Apresentando apenas os valores 0 ou 1
    def showMin(self):
        print(f"\nn: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] != 0:
                    print(self.adj[i][w], "", end="")
                else:
                    print("0", "", end="")
            print("\n")
        print("\nfim da impressao do grafo.")


class GrafoND:
    TAM_MAX_DEFAULT = 100  # qtde de vértices máxima default

    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT, r=False):
        self.n = n  # número de vértices
        self.m = 0  # número de arestas
        self.rot = r  # booleano se rotulado
        # matrizes de adjacência
        self.adj = [[0 for i in range(n)] for j in range(n)]

    # Insere uma aresta no Grafo tal que
    # v é adjacente a w
    def insereA(self, v, w, p=None):
        if p is not None and (self.adj[v][w] == 0):
            if not self.rot:
                print("[insereA] Erro: uso de peso em grafo nao rotulado")
                return
            self.adj[v][w] = p
            self.adj[w][v] = p
            self.m += 1  # atualiza qtd arestas
        elif p is not None and (self.adj[v][w] != 0):
            print("[insereA] Aviso: tentativa de inserir aresta duplicada")
        elif p is None and (self.adj[v][w] == 0):
            self.adj[v][w] = 1
            self.adj[w][v] = 1
            self.m += 1  # atualiza qtd arestas
        elif p is None and (self.adj[v][w] != 0):
            print("[insereA] Aviso: tentativa de inserir aresta duplicada")
        else:
            print("[insereA] Erro: argumentos invalidos")

    # remove uma aresta v-w do Grafo
    def removeA(self, v, w):
        # testa se temos a aresta
        if self.adj[v][w] != 0:
            self.adj[v][w] = 0
            self.adj[w][v] = 0
            self.m -= 1  # atualiza qtd arestas

    def lerMatriz(self, file):
        nlinha = 0
        # Abrir o arquivo para leitura
        with open(file, "r") as arquivo:
            # Loop pelas linhas do arquivo
            for linha in arquivo:
                if nlinha == 1:
                    narestas = int(linha)
                elif 1 < nlinha <= (narestas + 1):
                    # Quebrar a linha em palavras
                    palavras = linha.split()
                    npalavra = 0
                    # Loop pelas palavras da linha
                    for palavra in palavras:
                        if npalavra == 0:
                            vert1 = int(palavra)
                        elif npalavra == 1:
                            vert2 = int(palavra)
                        npalavra += 1
                    # Criar aresta com vertices encontrados
                    self.insereA(vert1, vert2)
                nlinha += 1

    def removeVertice(self, v):
        for j in range(0,self.n-1):
            for i in range(0,self.n-1):
                if (i < v):
                    if j < v:
                        continue
                    else:
                        if (j < n-1):
                            self.adj[j][i] = self.adj[j+1][i]
                        else
                            self.adj[j][i] = 0
                 else:
                    if j < v:
                        self.adj[j][i] = self.adj[j][i+1]
                    else:
                        if (j < n-1):
                            if (i < n-1):
                                self.adj[j][i] = self.adj[j+1][i+1]
                            else
                                self.adj[j][i] = 0    
                        else
                            self.adj[j][i] = 0
                   
            print(f"\nRemovido o vertice {v}")
            self.n -= 1

    def completo(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.adj[i][j] != 0:
                    continue
                else:
                    print("O grafo nao e completo")
                    return 0
            print("O grafo e completo")
            return 1

    # Apresenta o Grafo contendo
    # número de vértices, arestas
    # e a matriz de adjacência obtida
    def show(self):
        print("\nGrafo nao direcionado")
        print(f"n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}")
        print(f"rotulado: {self.rot}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] != 0:
                    print(f"Adj[{i:2d},{w:2d}] = {self.adj[i][w]} ", end="")
                else:
                    print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
            print("\n")
        if self.rot:
            for i in range(self.n):
                for w in range(self.n):
                    if self.adj[i][w] != 0:
                        print(f"Peso ({i:2d},{w:2d}) = {self.adj[i][w]} ", end="")
                print("\n")
        print("\nfim da impressao do grafo.")

    # Apresenta o Grafo contendo
    # número de vértices, arestas
    # e a matriz de adjacência obtida
    # Apresentando apenas os valores 0 ou 1
    def showMin(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] != 0:
                    print(self.adj[i][w], "", end="")
                else:
                    print("0", "", end="")
            print("\n")
        print("\nfim da impressao do grafo.")
