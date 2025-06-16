clubes = {}
jogadores = {}

class NoLesao:
    def __init__(self, tipo_lesao, data_lesao, duracao_lesao): 
        self.tipo_lesao = tipo_lesao
        self.data_lesao = data_lesao
        self.duracao_lesao = duracao_lesao
        self.proximo = None

class ListaEncadeadaLesoes:
    def __init__(self):
        self.inicio = None

    def adicionar_lesao(self, tipo_lesao, data_lesao, duracao_lesao):
        novo_no = NoLesao(tipo_lesao, data_lesao, duracao_lesao)
        if not self.inicio:
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo: 
                atual = atual.proximo
            atual.proximo = novo_no

    def exibir_lesoes(self):
        atual = self.inicio
        if not atual:
            print("Nenhuma lesão registrada.")
            return
        print("Histórico de lesões:")
        while atual:
            print(f"- {atual.tipo_lesao} em {atual.data_lesao}, duração: {atual.duracao_lesao}")
            atual = atual.proximo

class Jogador:
    def __init__(self, nome_jogador, idade_jogador, posicao_jogador):
        self.nome_jogador = nome_jogador
        self.idade_jogador = idade_jogador
        self.posicao_jogador = posicao_jogador
        self.clube_atual = None
        self.historico_transferencias = []
        self.lesoes = ListaEncadeadaLesoes()

class Clube:
    def __init__(self, nome_clube):
        self.nome_clube = nome_clube
        self.elenco = set()
        self.valor_mercado = 0

def cadastrar_clube():
    nome_clube = input("Nome do clube: ")
    if nome_clube in clubes:
        print("Clube já cadastrado.")
    else:
        clubes[nome_clube] = Clube(nome_clube)
        print(f"Clube '{nome_clube}' cadastrado.")

def cadastrar_jogador():
    nome_jogador = input("Nome do jogador: ")
    if nome_jogador in jogadores:
        print("Jogador já cadastrado.")
        return
    idade_jogador = int(input("Idade do jogador: "))
    posicao_jogador = input("Posição do jogador: ")
    jogadores[nome_jogador] = Jogador(nome_jogador, idade_jogador, posicao_jogador)
    print(f"Jogador '{nome_jogador}' cadastrado.")

def associar_jogador_clube():
    nome_jogador = input("Nome do jogador: ")
    nome_clube = input("Nome do clube: ")
    if nome_jogador not in jogadores or nome_clube not in clubes:
        print("Jogador ou clube não encontrado.")
        return
    jogador = jogadores[nome_jogador]
    clube = clubes[nome_clube]
    if jogador.clube_atual:
        print(f"Jogador já pertence ao clube '{jogador.clube_atual}'")
        return
    jogador.clube_atual = nome_clube
    clube.elenco.add(nome_jogador)
    clube.valor_mercado += 10
    print(f"Jogador '{nome_jogador}' agora joga no '{nome_clube}'.")

def transferir_jogador():
    nome_jogador = input("Nome do jogador: ")
    clube_destino = input("Clube destino: ")
    if nome_jogador not in jogadores or clube_destino not in clubes:
        print("Jogador ou clube não encontrado.")
        return
    valor_transferencia = float(input("Valor da transferência: "))
    jogador = jogadores[nome_jogador]
    clube_origem = jogador.clube_atual
    if clube_origem == clube_destino:
        print("Jogador já pertence a esse clube.")
        return
    if clube_origem:
        clubes[clube_origem].elenco.discard(nome_jogador)
        clubes[clube_origem].valor_mercado -= 10
    clubes[clube_destino].elenco.add(nome_jogador)
    clubes[clube_destino].valor_mercado += 10
    jogador.clube_atual = clube_destino
    jogador.historico_transferencias.append((clube_origem, clube_destino, valor_transferencia))
    print(f"Transferência: {nome_jogador} de {clube_origem} para {clube_destino} por R${valor_transferencia:.2f}")

def listar_elenco():
    nome_clube = input("Nome do clube: ")
    if nome_clube not in clubes:
        print("Clube não encontrado.")
        return
    print(f"Elenco do {nome_clube}:")
    for nome_jogador in clubes[nome_clube].elenco:
        print("-", nome_jogador)

def exibir_historico_transferencias():
    print("\nHistórico de transferências:")
    for nome_jogador, jogador in jogadores.items():
        if jogador.historico_transferencias:
            print(f"\nTransferências de {nome_jogador}:")
            for origem, destino, valor in jogador.historico_transferencias:
                print(f"  {origem} -> {destino} por R${valor:.2f}")
        else:
            print(f"\n{nome_jogador} não possui transferências.")

def registrar_lesao():
    nome_jogador = input("Nome do jogador: ")
    if nome_jogador not in jogadores:
        print("Jogador não encontrado.")
        return
    tipo_lesao = input("Tipo da lesão: ")
    data_lesao = input("Data (AAAA-MM-DD): ")
    duracao_lesao = input("Tempo estimado de recuperação: ")
    jogadores[nome_jogador].lesoes.adicionar_lesao(tipo_lesao, data_lesao, duracao_lesao)
    print(f"Lesão registrada para {nome_jogador}.")

def mostrar_lesoes():
    nome_jogador = input("Nome do jogador: ")
    if nome_jogador not in jogadores:
        print("Jogador não encontrado.")
        return
    jogadores[nome_jogador].lesoes.exibir_lesoes()

def buscar_jogadores_por_clube_e_posicao():
    nome_clube = input("Nome do clube: ")
    posicao = input("Posição desejada: ")
    
    if nome_clube not in clubes:
        print("Clube não encontrado.")
        return
    
    clube = clubes[nome_clube]
    jogadores_filtrados = []
    
    for nome_jogador in clube.elenco:
        jogador = jogadores[nome_jogador]
        if jogador.posicao_jogador.lower() == posicao.lower():
            jogadores_filtrados.append(jogador)
    
    if not jogadores_filtrados:
        print(f"Nenhum jogador encontrado na posição {posicao} no {nome_clube}.")
    else:
        print(f"Jogadores do {nome_clube} na posição {posicao}:")
        for jogador in jogadores_filtrados:
            print(f"- {jogador.nome_jogador} (Idade: {jogador.idade_jogador})")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar clube")
        print("2. Cadastrar jogador")
        print("3. Associar jogador a clube")
        print("4. Transferir jogador")
        print("5. Listar elenco de um clube")
        print("6. Exibir histórico de transferências")
        print("7. Registrar lesão")
        print("8. Mostrar lesões")
        print("9. Buscar jogadores por clube e posição")  
        print("0. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            cadastrar_clube()
        elif opcao == "2":
            cadastrar_jogador()
        elif opcao == "3":
            associar_jogador_clube()
        elif opcao == "4":
            transferir_jogador()
        elif opcao == "5":
            listar_elenco()
        elif opcao == "6":
            exibir_historico_transferencias()
        elif opcao == "7":
            registrar_lesao()
        elif opcao == "8":
            mostrar_lesoes()
        elif opcao == "9":
            buscar_jogadores_por_clube_e_posicao()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
