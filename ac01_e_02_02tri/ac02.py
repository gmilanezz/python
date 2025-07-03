# a) Declaração de variáveis
dispositivos = ["Sensor de Temperatura", "Sensor de Umidade", "Câmera IP", "Atuador de Luz", "Sensor de Presença",
                "Controle de Portão", "Medidor de Energia", "Sensor de Gás", "Display OLED", "Sirene Inteligente"]
# Lista com 10 dispositivos IoT diferentes que podem ser instalados em ambientes conectados.

ambientes = []
# Lista vazia que armazenará os grupos de até 5 dispositivos por ambiente inteligente.

ambiente_atual = []
# Lista temporária para formar um ambiente com até 5 dispositivos.

# b) Agrupamento de dispositivos por ambiente
for dispositivo in dispositivos:
    ambiente_atual.append(dispositivo)
    # Adiciona o dispositivo ao ambiente atual

    if len(ambiente_atual) == 5:
        ambientes.append(ambiente_atual)
        # Se o ambiente tiver 5 dispositivos, armazena e reinicia a montagem do próximo
        ambiente_atual = []

if ambiente_atual:
    ambientes.append(ambiente_atual)
    # Adiciona o último grupo (com menos de 5 dispositivos, se houver)

# c) Verificação da quantidade de ambientes inteligentes formados
if len(ambientes) > 2:
    print("Mais de 2 ambientes inteligentes foram configurados!")
else:
    print("2 ou menos ambientes inteligentes foram configurados.")

# d) Exibição dos dispositivos em cada ambiente
for i, ambiente in enumerate(ambientes, 1):
    print(f"Ambiente {i}: {ambiente}")

# e) Função para contar total de dispositivos IoT
def contar_dispositivos():
    return len(dispositivos)

print(f"Total de dispositivos IoT configurados: {contar_dispositivos()}")