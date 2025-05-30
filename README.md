# Nexxera_WebApp
Transposição da automação do Nexxera. Antes a automação era programada para uma aplicação Desktop, agora que o microsiga migrou para o Web, essa é a nova versão da automação compatível com o novo microsiga

# Automação Nexxera

## 📌 Descrição
Este script automatiza o processo de inserção de arquivos CNAB no Microsiga. A automação faz isso coletando esses arquivos na plataforma **Nexxera SkylineWeb**, extraindo dados do nome dos arquivos e, destinando-os corretamente no **Microsiga** a partir destes dados.
A automação garante que os arquivos sejam baixados, descompactados e lançados corretamente no sistema.

---

## 🚀 Tecnologias Utilizadas
- **Python**
- **Selenium** → Automação de navegador  
- **PyAutoGUI** → Automação de teclado e mouse  
- **EasyOCR** → Reconhecimento óptico de caracteres  
- **Shutil & ZipFile** → Manipulação de arquivos  
- **WebDriver Manager** → Gerenciamento do ChromeDriver  
- **Pathlib & OS** → Operações com diretórios  

---

## ⚙️ Funcionalidades
✅ Acessa a plataforma **Nexxera SkylineWeb** e realiza login automaticamente  
✅ Filtra os arquivos disponíveis por **período especificado**  
✅ Baixa e **descompacta** os arquivos CNAB  
✅ Lança os arquivos no **ERP Microsiga**  
✅ Utiliza **OCR** para garantir a correta **data de lançamento**  

---

## 🛠️ Instalação:

1. Clone o repositório ou baixe o arquivo ZIP do programa:
```bash
https://github.com/git-financeiro-eqs/Automacao_Nexxera.git
```

2. Instale as dependências
```bash
pip install -r requirements.txt
```

3. Execute o script:
```bash
python gui.py
```
<br/>

##  Como Usar

1. Informe o período desejado na interface da automação e clique no botão "Acionar".

2. Aguarde até que ela abra o microsiga webapp. Nesse momento, insira as credenciais do usuário bot.contabil e acesse
   o módulo Compras -> Atualizações -> Contas a Pagar -> Funções Ctas a Pag.

3. Quando aberta a Rotina, aguarde até que a automação finalize o trabalho. Isso ocorre quando não há mais nenhuma interação
   por da automação com a interface web do Siga. 
