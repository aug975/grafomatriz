from grafoMatriz import Grafo,GrafoND
from grafoLista import GrafoL

g = Grafo(4)
# insere as arestas do grafo
# A={(0,1),(0,2),(2,1),(2,3),(1,3)}
g.insereA(0,1)
g.insereA(0,2)
g.insereA(2,1)
g.insereA(2,3)
g.insereA(1,3)
# testes de main
g.inDegree(1)
g.outDegree(0)
g.fonte(0)
g.fonte(1)
g.sorvedouro(2)
g.sorvedouro(3)
g.completo()
# mostra o grafo preenchido
g.show()
g.showMin()

g2 = Grafo(4,True)
# insere as arestas do grafo
# A={(0,3),(3,1),(1,2),(2,0)}
# pesos 30, 40, 50, 60
g2.insereA(0,3,30)
g2.insereA(3,1,40)
g2.insereA(1,2,50)
g2.insereA(2,0,60)
# mostra o grafo preenchido
g2.show()
g2.showMin()

g3 = Grafo(4)
# insere as arestas do grafo
# A={(0,1),(1,0),(0,2),(2,0),(2,1),(1,2),(2,3),(3,2),(1,3),(3,1)}
g3.insereA(0,1)
g3.insereA(1,0)
g3.insereA(0,2)
g3.insereA(2,0)
g3.insereA(0,3)
g3.insereA(3,0)
g3.insereA(2,1)
g3.insereA(1,2)
g3.insereA(2,3)
g3.insereA(3,2)
g3.insereA(1,3)
g3.insereA(3,1)
g3.simetrico()
g3.completo()
# mostra o grafo preenchido
g3.show()
g3.showMin()

g4 = Grafo(6)
g4.lerMatriz("arquivo.txt")
g4.show()
g4.showMin()
g4.removeVertice(1)
g4.show()
g4.showMin()

g5 = GrafoND(6)
g5.lerMatriz("arquivo.txt")
g5.show()
g5.showMin()
g5.removeVertice(1)
g5.show()
g5.showMin()

g6 = GrafoND(4,True)
# insere as arestas do grafo
# A={(0,3),(3,1),(1,2),(2,0)}
# pesos 30, 40, 50, 60
g6.insereA(0,3,93)
g6.insereA(3,1,101)
g6.insereA(1,2,85)
g6.insereA(2,0,61)
# mostra o grafo preenchido
g6.show()
g6.showMin()

g7 = GrafoL(4)
#insere as arestas do grafo
#A={(0,1),(0,2),(2,1),(2,3),(1,3)}
g7.insereA(0,1)
g7.insereA(0,2)
g7.insereA(2,1)
g7.insereA(2,3)
g7.insereA(1,3)
# mostra o grafo preenchido
g7.show()
g7.removeA(0,1)
g7.show()

g8 = GrafoL(4)
#insere as arestas do grafo
#A={(0,1),(0,2),(2,1),(2,3),(1,3)}
g8.insereA(0,2)
g8.insereA(2,1)
g8.insereA(2,3)
g8.insereA(1,3)

g8.igual(g7)
# mostra o grafo preenchido
g8.show()

g9 = Grafo(4)

g9.insereA(0,2)
g9.insereA(1,3)
g9.insereA(2,1)
g9.insereA(2,3)

g9.showMin()

g10 = GrafoL(4)
g10.matToList(g9)
g10.show()