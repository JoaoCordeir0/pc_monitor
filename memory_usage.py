import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

xs = [0]
ys = [0]

# Incremento partindo dos últimos valores de cada lista
ram_use = 0
x = 0

#função para animar
def graphMemory(i, xs, ys):
    global ram_use
    global x

    # Pega o uso da memória
    ram_use = psutil.virtual_memory()[2]
    x = x + 1

    # Adiciona os novos índices x e uso da memória
    xs.append(x)
    ys.append(ram_use)

    if len(ys) > 40:
        xs.pop(0)
        ys.pop(0)
    
    # Limpa o gráfigo para receber nas novas posições
    ax.clear()

    # desenha x e y
    ax.plot(xs, ys, color='#00a9ff')

    # Seta o eixo Y com valores de 0 a 100
    plt.ylim(0, 100)    

    # Adiciona a legenda de utilização   
    plt.legend([f'Utilização: {round(ram_use)}%'], loc=9)

    # Adiciona título e descrição da coluna Y
    plt.title('Uso da memória em tempo real')
    plt.ylabel('Porcentagem')

# Chama a renderização do gráfico dentro da animação para ser renderizado dinamicamente a cada meio segundo
ani = animation.FuncAnimation(fig, graphMemory, fargs=(xs, ys), interval=500)
plt.show()