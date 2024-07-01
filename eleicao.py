import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Biblioteca Pillow para lidar com imagens

class Eleicao:
    def __init__(self):
        self.turmas = {
            'Turma 601': ['Felipe Victor', 'Wylla Andresa'],
            'Turma 602': ['Giovana Lopes', 'Laysa de Melo', 'Mikaelly Gonçalves'],
            'Turma 603': ['Felipe Klem', 'Fellype Gabriel', 'Nicolas Machado'],
            'Turma 604': ['Jessé Poubel', 'Paula Macedo', 'Sophia Teté'],
            'Turma 605': ['Ícaro Ferreira', 'Myrella Prata', 'Sofia Martins'],
            'Turma 701': ['Júlia Dantas', 'Mariana Carvalho', 'Miguel Rodrigues'],
            'Turma 702': ['Juliana Diniz', 'Lara ALice'],
            'Turma 703': ['Laura Corrêa', 'Manuella Domingos', 'Tainá Vieira'],
            'Turma 704': ['André Luiz', 'Anna Sophya', 'Anne Elizy'],
            'Turma 705': ['Fernanda da Silva', 'Júlia Helloá', 'Washington dos Santos'],
            'Turma 801': ['Ágatha Carolliny', 'Clara Elena', 'Kathlen Gomes'],
            'Turma 802': ['Ana Clara', 'Rafaella Souza', 'Vitor dos Santos'],
            'Turma 803': ['Alanes Caldeira', 'Juliana Meloni', 'Maurício Conti'],
            'Turma 804': ['Natasha Bernardino'],
            'Turma 805': ['Ana Beatriz', 'Giovanna Ferreira', 'Isabella Santos', 'Rafael dos Reis'],
            'Turma 901': ['Ana Carolina', 'Breno da Silva', 'João Pedro Godoi'],
            'Turma 902': ['Nayara Ventura', 'Luani Almeida', 'Yago Silva'],
            'Turma 903': ['Júlia Maciel', 'Leticia Soares', 'Yasmin de Souza', 'Yasmin Ventura'],
            'Turma 904': ['Gustavo Telles', 'Kaylane de Freitas', 'Wallace da Silva'],
            'Turma 905': ['Evelyn Estefane', 'Gabriel Gelani'],
        }
        self.votos = {turma: {candidato: 0 for candidato in candidatos} for turma, candidatos in self.turmas.items()}
        self.root = tk.Tk()
        self.root.title("Eleição de Representantes de Turma")
        self.root.state('zoomed')  # Inicializa em modo maximizado

        # Carregar a imagem de fundo
        try:
            self.bg_image = Image.open("fundo.png")
            self.bg_image = self.bg_image.resize((1280, 720), Image.LANCZOS)  # Ajusta o tamanho para reduzir o zoom
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        except FileNotFoundError:
            messagebox.showerror("Erro", "Imagem de fundo não encontrada. Certifique-se de que o caminho está correto.")
            self.bg_photo = None

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        if self.bg_photo:
            # Adicionar a imagem de fundo
            self.background_label = tk.Label(self.main_frame, image=self.bg_photo)
            self.background_label.place(relwidth=1, relheight=1)

        self.frame_turma = tk.Frame(self.main_frame, bg="#f0f0f0", padx=10, pady=10, highlightthickness=1, highlightbackground="#cccccc")
        self.frame_candidato = tk.Frame(self.main_frame, bg="#f0f0f0", padx=10, pady=10, highlightthickness=1, highlightbackground="#cccccc")

        self.frame_turma.place(relx=0.5, rely=0.5, anchor="center")
        self.create_frame_turma_widgets()

    def create_frame_turma_widgets(self):
        tk.Label(self.frame_turma, text="Escolha a turma para realizar a votação:", font=("Open Sans", 14), bg="#f0f0f0").pack(pady=5)

        self.turma_var = tk.StringVar(self.root)
        self.turma_var.set("Selecione uma turma")

        style = ttk.Style()
        style.configure('TCombobox', fieldbackground='#ffffff', background='#ffffff', font=('Open Sans', 14))
        
        turma_menu = ttk.Combobox(self.frame_turma, textvariable=self.turma_var, values=list(self.turmas.keys()), font=("Open Sans", 14))
        turma_menu.pack(pady=5)
        turma_menu.bind("<Button-1>", lambda e: turma_menu.event_generate('<Down>'))  # Abre o menu ao clicar em qualquer lugar
        turma_menu.configure(state='readonly')  # Impede a edição do texto

        tk.Button(self.frame_turma, text="Selecionar Turma", command=self.mostrar_candidatos, font=("Open Sans", 14), bg="#008000", fg="#ffffff", activebackground="#45a049").pack(pady=5)
        tk.Button(self.frame_turma, text="Mostrar Resultados", command=self.mostrar_resultados, font=("Open Sans", 14), bg="#000080", fg="#ffffff", activebackground="#007bb5").pack(pady=5)

    def mostrar_candidatos(self):
        turma = self.turma_var.get()
        if turma in self.turmas:
            self.frame_turma.place_forget()

            for widget in self.frame_candidato.winfo_children():
                widget.destroy()

            tk.Label(self.frame_candidato, text=f"Candidatos da {turma}:", font=("Open Sans", 14), bg="#f0f0f0").pack(pady=5)
            
            self.candidato_var = tk.StringVar(self.root)
            self.candidato_var.set("Selecione um candidato")
            self.candidato_menu = ttk.Combobox(self.frame_candidato, textvariable=self.candidato_var, values=self.turmas[turma], font=("Open Sans", 14))
            self.candidato_menu.pack(pady=5)
            self.candidato_menu.bind("<Button-1>", lambda e: self.candidato_menu.event_generate('<Down>'))
            self.candidato_menu.configure(state='readonly')
            tk.Button(self.frame_candidato, text="Votar", command=self.votar, font=("Open Sans", 14), bg="#008000", fg="#ffffff", activebackground="#45a049").pack(pady=5)
            tk.Button(self.frame_candidato, text="Voltar", command=self.voltar_para_turmas, font=("Open Sans", 14), bg="#8b0000", fg="#ffffff", activebackground="#e53935").pack(pady=5)

            self.frame_candidato.place(relx=0.5, rely=0.5, anchor="center")

    def votar(self):
        turma = self.turma_var.get()
        candidato = self.candidato_var.get()
        if turma in self.turmas and candidato in self.turmas[turma]:
            self.votos[turma][candidato] += 1
            messagebox.showinfo("Voto Computado", f"Seu voto para {candidato} da {turma} foi computado!")

            self.candidato_var.set("Selecione um candidato")
 
        else:
            messagebox.showwarning("Erro", "Por favor, selecione uma turma e um candidato válidos.")

    def voltar_para_turmas(self):
        self.frame_candidato.place_forget()
        self.frame_turma.place(relx=0.5, rely=0.5, anchor="center")

    def mostrar_resultados(self):
        resultados = tk.Toplevel(self.root)
        resultados.title("Resultados da Eleição")
        resultados.geometry("800x600")

        # Criação do Canvas
        canvas = tk.Canvas(resultados)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Adição da Scrollbar
        scrollbar = tk.Scrollbar(resultados, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configuração do Canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        # Função para rolar com o mouse
        def _on_mouse_wheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

        # Frame que conterá os resultados
        results_frame = tk.Frame(canvas, padx=10, pady=10)
        canvas.create_window((0, 0), window=results_frame, anchor="nw")

        for turma, votos in self.votos.items():
            tk.Label(results_frame, text=f"Resultados para {turma}:", font=("Arial", 14, "bold")).pack(pady=5)
            sorted_votos = sorted(votos.items(), key=lambda item: item[1], reverse=True)
            for candidato, contagem in sorted_votos:
                tk.Label(results_frame, text=f"{candidato}: {contagem} votos", font=("Arial", 12)).pack()
            if len(sorted_votos) > 1:
                vencedor = sorted_votos[0][0]
                vice = sorted_votos[1][0]
                tk.Label(results_frame, text=f"Vencedor: {vencedor}", font=("Arial", 12, "italic")).pack()
                tk.Label(results_frame, text=f"Vice: {vice}", font=("Arial", 12, "italic")).pack()
            else:
                tk.Label(results_frame, text=f"Vencedor: {sorted_votos[0][0]}", font=("Arial", 12, "italic")).pack()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    eleicao = Eleicao()
    eleicao.run()