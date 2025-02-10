from search import Problem, astar_search

class TorresHanoi(Problem):
    def __init__(self, num_discos):
        initial_state = (tuple(range(num_discos, 0, -1)), (), ())
        goal_state = ((), (), tuple(range(num_discos, 0, -1)))
        super().__init__(initial_state, goal_state)
        self.num_discos = num_discos

    def actions(self, state):
        actions = []
        for origem in range(3):
            if state[origem]:
                disco = state[origem][-1]
                for destino in range(3):
                    if origem != destino:
                        if not state[destino] or state[destino][-1] > disco:
                            actions.append((origem, destino))
        return actions

    def result(self, state, action):
        origem, destino = action
        novo_estado = [list(torre) for torre in state]
        disco = novo_estado[origem].pop()
        novo_estado[destino].append(disco)
        return tuple(tuple(torre) for torre in novo_estado)

    def goal_test(self, state):
        return state == self.goal

    def h(self, node):
        return sum((i + 1) * len(torre) for i, torre in enumerate(node.state))

problema = TorresHanoi(3)
solucao = astar_search(problema)

print("Passos para solução:")
for passo, acao in enumerate(solucao.solution(), 1):
    print(f"Passo {passo}: Mover da torre {acao[0]} para {acao[1]}")
