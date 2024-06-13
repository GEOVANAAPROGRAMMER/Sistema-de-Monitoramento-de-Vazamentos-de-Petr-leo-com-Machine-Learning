# Sistema de Monitoramento de Vazamentos de Petróleo

**Este projeto desenvolve um sistema de monitoramento de vazamentos de petróleo nas plataformas da Petrobras, utilizando machine learning para análise de imagens em tempo real. O sistema oferece uma interface web desenvolvida com Flask, que permite ao usuário selecionar e monitorar plataformas específicas. Em caso de detecção de vazamento, o sistema envia alertas imediatos e armazena dados históricos para análise preditiva.**

## Índice
- [Funcionalidades do Projeto](#funcionalidades-do-projeto)
- [Requisitos](#requisitos)
- [Como Rodar Este Projeto](#como-rodar-este-projeto)
- [Contribuição](#contribuição)

## Funcionalidades do Projeto

- **Interface de Usuário:** Interface web intuitiva para seleção e monitoramento de plataformas.
- **Detecção em Tempo Real:** Análise contínua de imagens para detecção de vazamentos.
- **Sistema de Alerta:** Notificações imediatas em caso de detecção de vazamento.

## Requisitos

- **Python 3.x**
- **Flask**
- **OpenCV**
- **Pillow**
- **Keras**

## Como Rodar Este Projeto?

1. Clone este repositório:
    ```bash
    git clone https://github.com/GEOVANAAPROGRAMMER/Sistema-de-Monitoramento-de-Vazamentos-de-Petr-leo-com-Machine-Learning.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd sistema-monitoramento-vazamentos
    ```
3. Instale as dependências necessárias:
    ```bash
    pip install opencv-python Pillow Flask keras
    ```
4. Execute o aplicativo:
    ```bash
    python app.py
    ```
5. Acesse a interface web em `http://localhost:5000`.

## Contribuição

O projeto está aberto para contribuições e sugestões. Se você deseja contribuir, siga os passos abaixo:

1. Faça um fork do repositório e clone em sua máquina local.
2. Crie uma branch para sua contribuição:
    ```bash
    git checkout -b minha-contribuicao
    ```
3. Faça suas alterações e commit:
    ```bash
    git commit -m "Minha contribuição"
    ```
4. Faça push para a branch:
    ```bash
    git push origin minha-contribuicao
    ```
5. Abra um pull request no repositório original.

Se você encontrou algum bug ou deseja propor uma nova funcionalidade, sinta-se à vontade para abrir uma issue. Estou aberta a novas ideias e melhorias para tornar este projeto ainda mais eficaz e útil.
