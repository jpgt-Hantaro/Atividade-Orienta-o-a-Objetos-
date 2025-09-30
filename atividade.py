import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacoes(self):
        return f"Modelo: {self.modelo}\nCor: {self.cor}\nPreço: R${self.preco:.2f}\nCategoria: {self.categoria.nome}"

    @abstractmethod
    def cadastrar(self):
        pass

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potencia_da_fonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potencia_da_fonte

    def getInformacoes(self):
        return f"{super().getInformacoes()}\nPotência da Fonte: {self._potenciaDaFonte}W"

    def cadastrar(self):
        return "Desktop cadastrado com sucesso!"

    @property
    def potenciaDaFonte(self):
        return self._potenciaDaFonte

    @potenciaDaFonte.setter
    def potenciaDaFonte(self, valor):
        self._potenciaDaFonte = valor

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempo_de_bateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempo_de_bateria

    def getInformacoes(self):
        return f"{super().getInformacoes()}\nTempo de Bateria: {self.__tempoDeBateria}h"

    def cadastrar(self):
        return "Notebook cadastrado com sucesso!"

    @property
    def tempoDeBateria(self):
        return self.__tempoDeBateria

    @tempoDeBateria.setter
    def tempoDeBateria(self, valor):
        self.__tempoDeBateria = valor

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro de Produtos")
        self.root.geometry("600x500")
        
        self.categorias = [
            Categoria(1, "Eletrônicos"),
            Categoria(2, "Informática"),
            Categoria(3, "Escritório")
        ]
        
        self.produtos = []
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True, fill='both')
        
        self.create_desktop_tab()
        self.create_notebook_tab()
        self.create_list_tab()

    def create_desktop_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Cadastrar Desktop")
        
        ttk.Label(frame, text="Modelo:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        ttk.Label(frame, text="Cor:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
        ttk.Label(frame, text="Preço:").grid(row=2, column=0, padx=10, pady=10, sticky='w')
        ttk.Label(frame, text="Categoria:").grid(row=3, column=0, padx=10, pady=10, sticky='w')
        ttk.Label(frame, text="Potência da Fonte:").grid(row=4, column=0, padx=10, pady=10, sticky='w')
        
        self.modelo_desktop = ttk.Entry(frame, width=30)
        self.cor_desktop = ttk.Entry(frame, width=30)
        self.preco_desktop = ttk.Entry(frame, width=30)
        self.categoria_desktop = ttk.Combobox(frame, values=[cat.nome for cat in self.categorias], width=27)
        self.potencia_desktop = ttk.Entry(frame, width=30)
        
        self.modelo_desktop.grid(row=0, column=1, padx=10, pady=10)
        self.cor_desktop.grid(row=1, column=1, padx=10, pady=10)
        self.preco_desktop.grid(row=2, column=1, padx=10, pady=10)
        self.categoria_desktop.grid(row=3, column=1, padx=10, pady=10)
        self.potencia_desktop.grid(row=4, column=1, padx=10, pady=10)
        
        ttk.Button(frame, text="Cadastrar Desktop", command=self.cadastrar_desktop).grid(row=5, column=0, columnspan=2, pady=20)

    def create_notebook_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Cadastrar Notebook")
        
        ttk.Label(frame, text="Modelo:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        ttk.Label(frame, text="Cor:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
        ttk.Label(frame, text="Preço:").grid(row=2, column=0, padx=10, pady=10, sticky='w')
        ttk.Label(frame, text="Categoria:").grid(row=3, column=0, padx=10, pady=10, sticky='w')
        ttk.Label(frame, text="Tempo de Bateria:").grid(row=4, column=0, padx=10, pady=10, sticky='w')
        
        self.modelo_notebook = ttk.Entry(frame, width=30)
        self.cor_notebook = ttk.Entry(frame, width=30)
        self.preco_notebook = ttk.Entry(frame, width=30)
        self.categoria_notebook = ttk.Combobox(frame, values=[cat.nome for cat in self.categorias], width=27)
        self.bateria_notebook = ttk.Entry(frame, width=30)
        
        self.modelo_notebook.grid(row=0, column=1, padx=10, pady=10)
        self.cor_notebook.grid(row=1, column=1, padx=10, pady=10)
        self.preco_notebook.grid(row=2, column=1, padx=10, pady=10)
        self.categoria_notebook.grid(row=3, column=1, padx=10, pady=10)
        self.bateria_notebook.grid(row=4, column=1, padx=10, pady=10)
        
        ttk.Button(frame, text="Cadastrar Notebook", command=self.cadastrar_notebook).grid(row=5, column=0, columnspan=2, pady=20)

    def create_list_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Lista de Produtos")
        
        self.lista_produtos = tk.Listbox(frame, width=80, height=20)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.lista_produtos.yview)
        self.lista_produtos.configure(yscrollcommand=scrollbar.set)
        
        self.lista_produtos.pack(side='left', padx=10, pady=10, fill='both', expand=True)
        scrollbar.pack(side='right', fill='y', pady=10)
        
        ttk.Button(frame, text="Atualizar Lista", command=self.atualizar_lista).pack(pady=10)

    def cadastrar_desktop(self):
        try:
            if not all([self.modelo_desktop.get(), self.cor_desktop.get(), self.preco_desktop.get(), 
                       self.categoria_desktop.get(), self.potencia_desktop.get()]):
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
                return
            
            categoria = next((cat for cat in self.categorias if cat.nome == self.categoria_desktop.get()), None)
            if not categoria:
                messagebox.showerror("Erro", "Categoria inválida!")
                return
            
            desktop = Desktop(
                self.modelo_desktop.get(),
                self.cor_desktop.get(),
                float(self.preco_desktop.get()),
                categoria,
                int(self.potencia_desktop.get())
            )
            
            resultado = desktop.cadastrar()
            self.produtos.append(desktop)
            self.limpar_campos_desktop()
            messagebox.showinfo("Sucesso", resultado)
            
        except ValueError:
            messagebox.showerror("Erro", "Preço e potência devem ser números válidos!")

    def cadastrar_notebook(self):
        try:
            if not all([self.modelo_notebook.get(), self.cor_notebook.get(), self.preco_notebook.get(), 
                       self.categoria_notebook.get(), self.bateria_notebook.get()]):
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
                return
            
            categoria = next((cat for cat in self.categorias if cat.nome == self.categoria_notebook.get()), None)
            if not categoria:
                messagebox.showerror("Erro", "Categoria inválida!")
                return
            
            notebook = Notebook(
                self.modelo_notebook.get(),
                self.cor_notebook.get(),
                float(self.preco_notebook.get()),
                categoria,
                int(self.bateria_notebook.get())
            )
            
            resultado = notebook.cadastrar()
            self.produtos.append(notebook)
            self.limpar_campos_notebook()
            messagebox.showinfo("Sucesso", resultado)
            
        except ValueError:
            messagebox.showerror("Erro", "Preço e tempo de bateria devem ser números válidos!")

    def limpar_campos_desktop(self):
        self.modelo_desktop.delete(0, tk.END)
        self.cor_desktop.delete(0, tk.END)
        self.preco_desktop.delete(0, tk.END)
        self.categoria_desktop.set('')
        self.potencia_desktop.delete(0, tk.END)

    def limpar_campos_notebook(self):
        self.modelo_notebook.delete(0, tk.END)
        self.cor_notebook.delete(0, tk.END)
        self.preco_notebook.delete(0, tk.END)
        self.categoria_notebook.set('')
        self.bateria_notebook.delete(0, tk.END)

    def atualizar_lista(self):
        self.lista_produtos.delete(0, tk.END)
        for i, produto in enumerate(self.produtos, 1):
            self.lista_produtos.insert(tk.END, f"Produto #{i}:")
            self.lista_produtos.insert(tk.END, produto.getInformacoes())
            self.lista_produtos.insert(tk.END, "-" * 50)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()