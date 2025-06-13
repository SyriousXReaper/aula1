class restaurante:
    def _init_(self):
        self.cardapio = {} #dicionario = porque queremos que os clientes chamem o nome do prato
        self.comanda = {} 
    
    def adicionar_prato(self):
        nome = input("nome do prato: ")
        preco = float(input("Preço: "))
        self.cardapio[nome]= preco
        print(f"{nome} foi adicionado ao sistema")
        
    def abrir_comanda(self):
        numero = int(input("insira numero da comanda: "))
        if numero in self.comanda:
            print("Comanda já existente")
            return
        self.comanda[numero]={"pratos":[], "total":0, "status":"aberta"}
        print(f"comanda {numero} aberta")
        
    def adicionar_pedido(self):
        numero= int(input("insira o numero da comanda: "))
        if numero not in self.comanda:
            print("comanda não encontrada")
            return
        print("Cardapio disponivel: ")
        for nome, preco in self.cardapio.items():
            print(f"{nome}, R${preco:.2f}")
        
        prato = input("nome do prato para adicionar: ")
        if prato in self.cardapio:
            self.comanda[numero]["pratos"].append(prato)    
            self.comanda[numero]["total"]+=self.cardapio[prato]
            self.comanda[numero]["status"]='sendo preparado'
            print(f"{prato} adicionado a comanda {numero}")
        else:
            print("Prato não esta no cardapio")
        
        
    def verificar_pedido(self):
        numero=int(input("numero da comanda: "))
        if numero not in self.comanda:
            print("comanda não encontrada")
            return 
        print(f"conta da comanda {numero} fechada")
        print(f"Status: {self.comanda[numero]}")
        print(f"total: R${self.comanda[numero]}['total']:.2f")
        
    def fechar_conta(self):
        numero=int(input("numero da comanda"))
        if numero not in self.comanda:
            print(f"comanda não encontrada")
            return 
        
        if self.comanda[numero]["status"] == "Aberto":
            print(f"o pedido esta em preparo")
            return
        
        print(f"conta da comanda {numero} fechada")
        print(f"total a pagar: R${self.comanda[numero]}['total']")
        del self.comanda[numero]
        
restaurante = restaurante()

while True:
    print("1- adicionar o cardapio")
    print("2- abrir comanda")
    print("3 adicionar pedido")
    print("4 verificar pedido")
    print("5 fechar conta")
    print("6 sair")
    opcao=input("escolha uma opção: ")
    if opcao == "1":
      restaurante.adicionar_prato()
    elif opcao == "2":
     restaurante.abrir_comanda()
    elif opcao == "3":    
     restaurante.adicionar_pedido()
    elif opcao == "4":
     restaurante.verificar_pedido()
    elif opcao == "5":
     restaurante.fechar_conta()
    elif opcao == "6":
     print("saindo")
     break
    else:
     print("opçao incorreta")