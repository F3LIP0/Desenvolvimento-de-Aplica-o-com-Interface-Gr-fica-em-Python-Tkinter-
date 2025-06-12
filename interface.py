import tkinter as tk
from tkinter import ttk
from funcoes import comprimento, peso, temperatura, formatar_resultado

class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conversor de Unidades")
        self.geometry("500x400")
        self.resizable(False, False)
        
        # Centralizar a janela na tela
        self.center_window()
        
        # Mostrar tela inicial
        self.mostrar_tela_inicial()

    def center_window(self):
        """Centraliza a janela na tela"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def mostrar_tela_inicial(self):
        """Mostra a tela inicial com as opções de conversão"""
        # Limpa a tela atual
        for widget in self.winfo_children():
            widget.destroy()

        # Frame principal
        self.frame_principal = ttk.Frame(self, padding="20")
        self.frame_principal.pack(expand=True, fill="both")

        # Título
        self.label_titulo = ttk.Label(
            self.frame_principal, 
            text="Conversor de Unidades", 
            font=("Arial", 18, "bold")
        )
        self.label_titulo.pack(pady=(0, 10))

        # Subtítulo
        self.label_subtitulo = ttk.Label(
            self.frame_principal, 
            text="Escolha uma categoria de conversão:", 
            font=("Arial", 12)
        )
        self.label_subtitulo.pack(pady=(0, 20))

        # Frame para os botões
        self.frame_botoes = ttk.Frame(self.frame_principal)
        self.frame_botoes.pack(expand=True)

        # Botões das categorias
        self.btn_comprimento = ttk.Button(
            self.frame_botoes, 
            text="📏 Comprimento", 
            command=lambda: self.mostrar_tela_conversao("comprimento"),
            width=20
        )
        self.btn_comprimento.pack(pady=10)

        self.btn_peso = ttk.Button(
            self.frame_botoes, 
            text="⚖️ Peso", 
            command=lambda: self.mostrar_tela_conversao("peso"),
            width=20
        )
        self.btn_peso.pack(pady=10)

        self.btn_temperatura = ttk.Button(
            self.frame_botoes, 
            text="🌡️ Temperatura", 
            command=lambda: self.mostrar_tela_conversao("temperatura"),
            width=20
        )
        self.btn_temperatura.pack(pady=10)

    def mostrar_tela_conversao(self, categoria):
        """Mostra a tela de conversão específica para a categoria escolhida"""
        # Limpa a tela atual
        for widget in self.winfo_children():
            widget.destroy()

        # Frame principal
        self.frame_conversao = ttk.Frame(self, padding="20")
        self.frame_conversao.pack(expand=True, fill="both")

        # Título da categoria
        self.label_categoria = ttk.Label(
            self.frame_conversao, 
            text=f"Conversão de {categoria.capitalize()}", 
            font=("Arial", 16, "bold")
        )
        self.label_categoria.pack(pady=(0, 20))

        # Frame para os campos de entrada
        self.frame_entrada = ttk.LabelFrame(self.frame_conversao, text="Dados para conversão", padding="10")
        self.frame_entrada.pack(fill="x", pady=(0, 20))

        # Valor a ser convertido
        ttk.Label(self.frame_entrada, text="Valor:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_valor = ttk.Entry(self.frame_entrada, width=15)
        self.entry_valor.grid(row=0, column=1, padx=(10, 0), pady=5)

        # Unidade de origem
        ttk.Label(self.frame_entrada, text="De:").grid(row=1, column=0, sticky="w", pady=5)
        self.combo_origem = ttk.Combobox(self.frame_entrada, width=12, state="readonly")
        self.combo_origem.grid(row=1, column=1, padx=(10, 0), pady=5)

        # Unidade de destino
        ttk.Label(self.frame_entrada, text="Para:").grid(row=2, column=0, sticky="w", pady=5)
        self.combo_destino = ttk.Combobox(self.frame_entrada, width=12, state="readonly")
        self.combo_destino.grid(row=2, column=1, padx=(10, 0), pady=5)

        # Configurar as opções dos comboboxes baseado na categoria
        self.configurar_unidades(categoria)

        # Botão converter
        self.btn_converter = ttk.Button(
            self.frame_conversao, 
            text="Converter", 
            command=lambda: self.realizar_conversao(categoria)
        )
        self.btn_converter.pack(pady=10)

        # Frame para o resultado
        self.frame_resultado = ttk.LabelFrame(self.frame_conversao, text="Resultado", padding="10")
        self.frame_resultado.pack(fill="x", pady=(0, 20))

        self.label_resultado = ttk.Label(
            self.frame_resultado, 
            text="Insira os dados e clique em 'Converter'", 
            font=("Arial", 11)
        )
        self.label_resultado.pack()

        # Botão voltar
        self.btn_voltar = ttk.Button(
            self.frame_conversao, 
            text="← Voltar", 
            command=self.mostrar_tela_inicial
        )
        self.btn_voltar.pack(pady=(10, 0))

    def configurar_unidades(self, categoria):
        """Configura as opções dos comboboxes baseado na categoria"""
        if categoria == "comprimento":
            unidades = ["Metros", "Centímetros", "Milímetros", "Quilômetros"]
        elif categoria == "peso":
            unidades = ["Quilogramas", "Gramas", "Miligramas"]
        elif categoria == "temperatura":
            unidades = ["Celsius", "Fahrenheit", "Kelvin"]
        
        self.combo_origem['values'] = unidades
        self.combo_destino['values'] = unidades
        
        # Definir valores padrão
        if unidades:
            self.combo_origem.set(unidades[0])
            self.combo_destino.set(unidades[1] if len(unidades) > 1 else unidades[0])

    def realizar_conversao(self, categoria):
        """Realiza a conversão usando as funções do módulo funcoes"""
        try:
            valor = float(self.entry_valor.get())
            origem = self.combo_origem.get()
            destino = self.combo_destino.get()
            
            # Verificar se as unidades foram selecionadas
            if not origem or not destino:
                self.label_resultado.config(text="Por favor, selecione as unidades de origem e destino!")
                return
            
            # Realizar a conversão baseada na categoria
            if categoria == "comprimento":
                resultado = comprimento(valor, origem, destino)
            elif categoria == "peso":
                resultado = peso(valor, origem, destino)
            elif categoria == "temperatura":
                resultado = temperatura(valor, origem, destino)
            else:
                self.label_resultado.config(text="Categoria de conversão inválida!")
                return
            
            # Formatar e exibir o resultado
            resultado_formatado = formatar_resultado(resultado)
            resultado_texto = f"{formatar_resultado(valor)} {origem} = {resultado_formatado} {destino}"
            self.label_resultado.config(text=resultado_texto)
            
        except ValueError:
            self.label_resultado.config(text="Por favor, insira um valor numérico válido!")
        except Exception as e:
            self.label_resultado.config(text=f"Erro na conversão: {str(e)}")


