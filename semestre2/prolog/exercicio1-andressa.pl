masculino(luis).
feminino(maria).
masculino(joao).
feminino(ana).
masculino(jose).
feminino(joana).
masculino(gabriel).

pai(luis, joao).
pai(luis, ana).
pai(luis, jose).
pai(jose, gabriel).

mae(maria, joao).
mae(maria, jose).
mae(maria, ana).
mae(joana, gabriel).

avó(maria, gabriel).

tia(ana, gabriel).

irmao(jose, ana).

pai(X, Y) :- masculino(X), pai(X, Y).
mae(X, Y) :- feminino(X), mae(X, Y).
avó(X, Y) :- feminino(X), mae(X, mae(M, Y)).
tia(X, Y) :- feminino(X), irmao(pai(P, Y), X).
irmao(X, Y) :- masculino(X), pai(P, X), pai(P, Y).
