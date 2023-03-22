import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

xs = [0]
ys = [0]

# Incremento partindo dos últimos valores de cada lista
cpu_use = 0
x = 0

#função para animar
def graphCPU(i, xs, ys):
    global cpu_use
    global x

    # Pega o uso da CPU com intervalos de meio segundo
    cpu_use = psutil.cpu_percent(interval=0.5) 
    x = x + 1

    # Adiciona os novos índices x e uso da cpu
    xs.append(x)
    ys.append(cpu_use)

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
    plt.legend([f'Utilização: {round(cpu_use)}%'], loc=9)

    # Adiciona título e descrição da coluna Y
    plt.title('Uso do processador em tempo real')
    plt.ylabel('Porcentagem')

# Chama a renderização do gráfico dentro da animação para ser renderizado dinamicamente a cada meio segundo
ani = animation.FuncAnimation(fig, graphCPU, fargs=(xs, ys), interval=500)
plt.show()