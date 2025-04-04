import tkinter as tk

# Função para ajustar o tamanho da janela conforme a escala
def ajustar_tamanho_janela(escala):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    
    largura_janela = int(largura_tela * escala)
    altura_janela = int(altura_tela * escala)
    
    pos_x = int((largura_tela - largura_janela) / 2)
    pos_y = int((altura_tela - altura_janela) / 2)
    
    root.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')

# Criar a janela principal
root = tk.Tk()
root.title("Janela com Tamanho Ajustável")

# Definir a escala desejada (por exemplo, 0.5 para 50% do tamanho da tela)
escala = 0.5
ajustar_tamanho_janela(escala)

# Iniciar o loop principal da interface gráfica
root.mainloop()
