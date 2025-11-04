import tkinter as tk
from tkinter import ttk, messagebox

def ler_dados_alunos():
    """Lê o arquivo alunos.txt e retorna uma lista de dicionários."""
    alunos = []
    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            aluno = {}
            for linha in arquivo:
                linha = linha.strip()
                if linha.startswith("Matricula:"):
                    aluno["matricula"] = linha.split(": ")[1]
                elif linha.startswith("Nome:"):
                    aluno["nome"] = linha.split(": ")[1]
                elif linha.startswith("CPF:"):
                    aluno["cpf"] = linha.split(": ")[1]
                elif linha.startswith("RG:"):
                    aluno["rg"] = linha.split(": ")[1]
                elif linha.startswith("Sexo:"):
                    aluno["sexo"] = linha.split(": ")[1]
                elif linha.startswith("Data de Nascimento:"):
                    aluno["data_nasc"] = linha.split(": ")[1]
                elif linha.startswith("------------------------"):
                    if aluno:
                        alunos.append(aluno)
                        aluno = {}
        return alunos
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo 'alunos.txt' não encontrado.")
        return []


def ler_notas():
    """Lê o arquivo notas.txt e retorna um dicionário com matrícula como chave."""
    notas = {}
    try:
        with open("notas.txt", "r", encoding="utf-8") as arquivo:
            matricula = None
            for linha in arquivo:
                linha = linha.strip()
                if linha.startswith("Matricula:"):
                    matricula = linha.split(": ")[1]
                    notas[matricula] = {}
                elif linha.startswith("NP1:"):
                    notas[matricula]["NP1"] = float(linha.split(": ")[1])
                elif linha.startswith("NP2:"):
                    notas[matricula]["NP2"] = float(linha.split(": ")[1])
                elif linha.startswith("PIM:"):
                    notas[matricula]["PIM"] = float(linha.split(": ")[1])
        return notas
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo 'notas.txt' não encontrado.")
        return {}


def calcular_media(np1, np2, pim):
    """Calcula a média ponderada e retorna o valor e a situação."""
    media = ((np1 * 4) + (np2 * 4) + (pim * 2)) / 10
    situacao = "Aprovado ✅" if media >= 5 else "Reprovado ❌"
    return round(media, 2), situacao


def exibir_dados():
    """Atualiza a tabela com os dados dos alunos e suas notas."""
    alunos = ler_dados_alunos()
    notas = ler_notas()

    # Limpa a tabela
    for item in tree.get_children():
        tree.delete(item)

    # Popula a tabela com os dados
    for aluno in alunos:
        matricula = aluno.get("matricula", "")
        dados_notas = notas.get(matricula, {})
        np1 = dados_notas.get("NP1", 0)
        np2 = dados_notas.get("NP2", 0)
        pim = dados_notas.get("PIM", 0)

        if matricula in notas:
            media, situacao = calcular_media(np1, np2, pim)
        else:
            media, situacao = "-", "-"

        tree.insert("", "end", values=(
            matricula,
            aluno.get("nome", ""),
            np1,
            np2,
            pim,
            media,
            situacao
        ))


# === INTERFACE GRÁFICA ===
janela = tk.Tk()
janela.title("Sistema Acadêmico — UNIKRAG")
janela.geometry("850x400")
janela.configure(bg="#f7f7f7")

titulo = tk.Label(
    janela, 
    text="📚 Sistema Acadêmico — UNIKRAG", 
    font=("Segoe UI", 16, "bold"), 
    bg="#f7f7f7"
)
titulo.pack(pady=10)

# Criando tabela
colunas = ("Matrícula", "Nome", "NP1", "NP2", "PIM", "Média", "Situação")
tree = ttk.Treeview(janela, columns=colunas, show="headings")

for coluna in colunas:
    tree.heading(coluna, text=coluna)
    tree.column(coluna, width=100, anchor="center")

tree.pack(padx=10, pady=10, fill="both", expand=True)

# Botão para atualizar dados
botao = tk.Button(
    janela, 
    text="🔄 Atualizar Dados", 
    command=exibir_dados, 
    bg="#4CAF50", 
    fg="white", 
    font=("Segoe UI", 10, "bold")
)
botao.pack(pady=10)

# Carrega dados automaticamente
exibir_dados()

janela.mainloop()