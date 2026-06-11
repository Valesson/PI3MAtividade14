class Usuario:
    def __init__(self, nome, email, matricula, senha):
        self.nome = nome
        self.email = email
        self.matricula = matricula
        self.senha = senha

    def fazer_login(self):
        print(f"{self.nome} realizou login no sistema.")

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        print("Senha alterada com sucesso.")

    def __str__(self):
        return f"Usuário: {self.nome} | Matrícula: {self.matricula} | Email: {self.email}"


class Cadeira:
    def __init__(self, numero, fileira, ocupada=False):
        self.numero = numero
        self.fileira = fileira
        self.ocupada = ocupada

    def ocupar(self):
        self.ocupada = True
        print(f"Cadeira {self.numero} ocupada.")

    def liberar(self):
        self.ocupada = False
        print(f"Cadeira {self.numero} liberada.")

    def __str__(self):
        status = "Ocupada" if self.ocupada else "Disponível"
        return f"Cadeira {self.numero} - Fileira {self.fileira} - {status}"


class Reserva:
    def __init__(self, usuario, cadeira, data, ativa=True):
        self.usuario = usuario
        self.cadeira = cadeira
        self.data = data
        self.ativa = ativa

    def confirmar_reserva(self):
        if not self.cadeira.ocupada:
            self.cadeira.ocupar()
            self.ativa = True
            print("Reserva confirmada.")
        else:
            print("Não foi possível reservar. Cadeira ocupada.")

    def cancelar_reserva(self):
        self.cadeira.liberar()
        self.ativa = False
        print("Reserva cancelada.")

    def __str__(self):
        status = "Ativa" if self.ativa else "Cancelada"
        return (f"Reserva de {self.usuario.nome} "
                f"na cadeira {self.cadeira.numero} "
                f"em {self.data} - {status}")


# ==========================
# TESTES DAS CLASSES
# ==========================

# Usuários
usuario1 = Usuario("João Silva", "joao@escola.edu", "2025001", "1234")
usuario2 = Usuario("Maria Souza", "maria@escola.edu", "2025002", "5678")

print(usuario1)
print(usuario2)

usuario1.fazer_login()
usuario2.alterar_senha("9999")

print()

# Cadeiras
cadeira1 = Cadeira(1, "A")
cadeira2 = Cadeira(2, "A")

print(cadeira1)
print(cadeira2)

cadeira1.ocupar()
cadeira1.liberar()

print()

# Reservas
reserva1 = Reserva(usuario1, cadeira1, "08/06/2026")
reserva2 = Reserva(usuario2, cadeira2, "08/06/2026")

print(reserva1)
print(reserva2)

reserva1.confirmar_reserva()
reserva2.confirmar_reserva()

print()

reserva1.cancelar_reserva()
reserva2.cancelar_reserva()

print()

print(reserva1)
print(reserva2)