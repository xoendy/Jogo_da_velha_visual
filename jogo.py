import tkinter as tk
from tkinter import messagebox

# ==========================
# 🧠 CONFIGURAÇÕES INICIAIS
# ==========================
root = tk.Tk()
root.title("Jogo da Velha")
root.resizable(False, False)

# Variáveis globais
jogador_atual = "X"
placar_x = 0
placar_o = 0
botoes = []
botoes_flat = []
tema_claro = True  # Tema inicial: claro

# ==========================
# 🧮 FUNÇÕES DO JOGO
# ==========================
def verificar_vencedor():
    """Verifica linhas, colunas e diagonais"""
    for i in range(3):
        # Linhas
        if botoes[i][0]["text"] != "" and botoes[i][0]["text"] == botoes[i][1]["text"] == botoes[i][2]["text"]:
            destacar_vencedor([botoes[i][0], botoes[i][1], botoes[i][2]])
            return botoes[i][0]["text"]
        # Colunas
        if botoes[0][i]["text"] != "" and botoes[0][i]["text"] == botoes[1][i]["text"] == botoes[2][i]["text"]:
            destacar_vencedor([botoes[0][i], botoes[1][i], botoes[2][i]])
            return botoes[0][i]["text"]

    # Diagonais
    if botoes[0][0]["text"] != "" and botoes[0][0]["text"] == botoes[1][1]["text"] == botoes[2][2]["text"]:
        destacar_vencedor([botoes[0][0], botoes[1][1], botoes[2][2]])
        return botoes[0][0]["text"]
    if botoes[0][2]["text"] != "" and botoes[0][2]["text"] == botoes[1][1]["text"] == botoes[2][0]["text"]:
        destacar_vencedor([botoes[0][2], botoes[1][1], botoes[2][0]])
        return botoes[0][2]["text"]
    return None

def clicar(botao):
    global jogador_atual, placar_x, placar_o
    if botao["text"] == "":
        botao.config(text=jogador_atual, fg="#003366" if tema_claro else "#ffffff")
        vencedor = verificar_vencedor()
        if vencedor:
            messagebox.showinfo("Fim de Jogo", f"🎉 O jogador {vencedor} venceu!")
            desativar_botoes()
            if vencedor == "X":
                placar_x += 1
                label_placar_x.config(text=f"Jogador X: {placar_x}")
            else:
                placar_o += 1
                label_placar_o.config(text=f"Jogador O: {placar_o}")
            return
        if all(b["text"] != "" for b in botoes_flat):
            messagebox.showinfo("Empate", "😐 O jogo terminou em empate!")
            desativar_botoes()
            return
        jogador_atual = "O" if jogador_atual == "X" else "X"

def desativar_botoes():
    for b in botoes_flat:
        b.config(state="disabled")

def reiniciar_partida():
    global jogador_atual
    jogador_atual = "X"
    for b in botoes_flat:
        b.config(text="", state="normal", bg="#ffffff" if tema_claro else "#555555", fg="#003366" if tema_claro else "#ffffff")

def zerar_placar():
    global placar_x, placar_o
    placar_x = 0
    placar_o = 0
    label_placar_x.config(text=f"Jogador X: {placar_x}")
    label_placar_o.config(text=f"Jogador O: {placar_o}")
    reiniciar_partida()

def mostrar_creditos():
    messagebox.showinfo(
        "Créditos",
        "🎮 Jogo da Velha\n\nDesenvolvido por: Alexandre da Silva de Jesus\nCurso Técnico em Informática\nAno: 2025"
    )

# -------------------------
# 🎨 Troca de tema
# -------------------------
def mudar_tema():
    global tema_claro
    tema_claro = not tema_claro
    if tema_claro:
        root.configure(bg="#f0f0f0")
        frame_placar.configure(bg="#f0f0f0")
        frame_controles.configure(bg="#f0f0f0")
        for b in botoes_flat:
            b.configure(bg="#ffffff", fg="#003366", activebackground="#d9eaff")
    else:
        root.configure(bg="#333333")
        frame_placar.configure(bg="#333333")
        frame_controles.configure(bg="#333333")
        for b in botoes_flat:
            b.configure(bg="#555555", fg="#ffffff", activebackground="#777777")
    # Atualiza labels e botões extras
    label_placar_x.configure(bg=root["bg"], fg="#004080" if tema_claro else "#ffffff")
    label_placar_o.configure(bg=root["bg"], fg="#004080" if tema_claro else "#ffffff")
    for btn in [botao_reiniciar, botao_zerar, botao_creditos, botao_mudar_tema]:
        btn.configure(bg="#dbe9ff" if tema_claro else "#777777", fg="#000000" if tema_claro else "#ffffff")

# -------------------------
# ✨ Destaque do vencedor
# -------------------------
def destacar_vencedor(lista_botoes):
    for b in lista_botoes:
        b.config(bg="#90ee90")  # verde suave

# ==========================
# 🎨 INTERFACE GRÁFICA
# ==========================
root.configure(bg="#f0f0f0")
# Placar
frame_placar = tk.Frame(root, bg="#f0f0f0")
frame_placar.grid(row=0, column=0, columnspan=3, pady=10)

label_placar_x = tk.Label(frame_placar, text=f"Jogador X: {placar_x}", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#004080")
label_placar_x.grid(row=0, column=0, padx=20)
label_placar_o = tk.Label(frame_placar, text=f"Jogador O: {placar_o}", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#004080")
label_placar_o.grid(row=0, column=2, padx=20)

# Tabuleiro
for i in range(3):
    linha = []
    for j in range(3):
        botao = tk.Button(root, text="", font=("Helvetica", 32), width=5, height=2,
                          bg="#ffffff", activebackground="#d9eaff", fg="#003366",
                          command=lambda b=None: None)
        botao.config(command=lambda b=botao: clicar(b))
        botao.grid(row=i+1, column=j, padx=5, pady=5)
        linha.append(botao)
        botoes_flat.append(botao)
    botoes.append(linha)

# Botões extras
frame_controles = tk.Frame(root, bg="#f0f0f0")
frame_controles.grid(row=4, column=0, columnspan=3, pady=15)

botao_reiniciar = tk.Button(frame_controles, text="🔁 Reiniciar Partida", font=("Helvetica", 12), width=18, command=reiniciar_partida, bg="#dbe9ff")
botao_reiniciar.grid(row=0, column=0, padx=5)
botao_zerar = tk.Button(frame_controles, text="🧮 Zerar Placar", font=("Helvetica", 12), width=15, command=zerar_placar, bg="#dbe9ff")
botao_zerar.grid(row=0, column=1, padx=5)
botao_creditos = tk.Button(frame_controles, text="👤 Créditos", font=("Helvetica", 12), width=12, command=mostrar_creditos, bg="#dbe9ff")
botao_creditos.grid(row=0, column=2, padx=5)
botao_mudar_tema = tk.Button(frame_controles, text="🎨 Mudar Tema", font=("Helvetica", 12), width=15, command=mudar_tema, bg="#dbe9ff")
botao_mudar_tema.grid(row=0, column=3, padx=5)

# ==========================
# 🚀 EXECUÇÃO PRINCIPAL
# ==========================
root.mainloop()
