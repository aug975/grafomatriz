# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:01:03 2023

@author: icalc
"""


# Grafo como uma lista de adjacência
class GrafoL:
    TAM_MAX_DEFAULT = 100  # qtde de vértices máxima default

    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n  # número de vértices
        self.m = 0  # número de arestas
        # lista de adjacência
        self.listaAdj = [[] for i in range(self.n)]

    # Insere uma aresta no Grafo tal que
    # v é adjacente a w
    def insereA(self, v, w):
        self.listaAdj[v].append(w)
        self.m += 1

    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        self.listaAdj[v].remove(w)
        self.m -= 1

    def igual(self, g):
        temp = []
        j = 0
        if self.n != g.n:
            print("\nOs grafos nao sao iguais")
            return 0
        elif self.m != g.m:
            print("\nOs grafos nao sao iguais")
            return 0
        for i in range(self.n):
            for w in self.listaAdj[i]:
                temp.append(w)
        for i in range(self.n):
            for w in g.listaAdj[i]:
                if w != temp[j]:
                    print("\nOs grafos nao sao iguais")
                    return 0
                j += 1
        print("\nOs grafos sao iguais")
        return 1

    def matToList(self,g):
        for i in range(g.n):
            for j in range(g.n):
                if g.adj[i][j] != 0:
                    self.listaAdj[i].append(j)

    # Apresenta o Grafo contendo
    # número de vértices, arestas
    # e a LISTA de adjacência obtida
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}")
        for i in range(self.n):
            print(f"\n{i:2d}: ", end="")
            for w in range(len(self.listaAdj[i])):
                val = self.listaAdj[i][w]
                print(f"{val:2d}", end="")

        print("\n\nfim da impressao do grafo.")
