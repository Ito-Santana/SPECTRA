# SPECTRA
## Sistema de Previsão e Controle Tático de Riscos e Alertas

![Logo do Projeto](https://github.com/Ito-Santana/SPECTRA/blob/main/Recursos/Logo/LOGO%20VERTICAL.png)

## Descrição
O **SPECTRA** é um sistema  desenvolvido como parte do currículo da disciplina de Projetos, oferecida no curso de Gestão de Tecnologia da Informação pela Cesar School. Seu principal propósito é mapear e analisar em tempo real os índices de criminalidade em ambientes urbanos, utilizando tecnologias avançadas de geolocalização e análise de dados.

O diferencial do SPECTRA está em sua capacidade de plotar pins no mapa, fornecendo uma representação visual imediata dos locais onde ocorreram crimes. Essa funcionalidade permite uma compreensão mais rápida e intuitiva da distribuição geográfica dos eventos criminais, facilitando a identificação de padrões, áreas de risco e necessidades específicas de intervenção.

Com uma interface intuitiva e poderosas ferramentas de visualização de dados, o SPECTRA capacita não apenas os gestores de segurança pública e planejadores urbanos, mas também a população em geral, a tomar decisões informadas e estratégicas para aprimorar a segurança e a qualidade de vida nas cidades. Além disso, sua capacidade de análise em tempo real possibilita uma resposta ágil a eventos emergentes, contribuindo para uma abordagem proativa na prevenção e combate à criminalidade.

O SPECTRA representa um avanço significativo na gestão da segurança urbana, integrando tecnologia, dados e conhecimento para enfrentar os desafios complexos do cenário urbano contemporâneo.


## Fluxograma e Pins

|  Fluxograma                                    | Descrição                                                                                       |
|------------------------------------------------|-------------------------------------------------------------------------------------------------|
| ![Fluxograma do Projeto](https://github.com/Ito-Santana/SPECTRA/blob/main/Recursos/Fluxograma.png) | Inicialmente, o usuário estará na página do mapa, onde poderá filtrar os crimes exibidos ou informar um novo crime.<br><br>Ao inserir um novo crime, o usuário fornecerá a localização, o período e o tipo de crime. Esses dados serão salvos previamente no banco de dados. Simultaneamente, a localização será pesquisada na API do Google para obter as coordenadas de latitude e longitude, que também serão armazenadas no banco de dados.<br><br>Com todas as informações reunidas, um novo marcador (pin) será adicionado à tela inicial. 🌟 |

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| Pins                               | Relação de Cores                                                                               |
|------------------------------------|------------------------------------------------------------------------------------------------|
| ![Fluxograma do Projeto](https://github.com/Ito-Santana/SPECTRA/blob/main/Recursos/pins.png) | Roxo : Assédio<br><br>Vermelho: Estupro<br><br>Cinza: Assalto<br><br>Verde: Crime de Trânsito<br><br>Azul: Arrastão<br><br>Laranja: Arrombamento<br><br>Preto: Homícidio

##Prótotipos
|WIREFRAME | MOCKUP | FINAL |
|----------|--------|-------|
|![wireframe](https://github.com/Ito-Santana/SPECTRA/blob/main/Recursos/Protótipos%20(Baixa%2C%20Média%20e%20Alta%20fidelidade)/Baixa_Fidelidade.jpeg)|![mockup](

### Recursos
- **Previsão de Riscos:** Algoritmos de previsão baseados em IA para identificar riscos potenciais.
- **Controle Tático:** Ferramentas de controle para gerenciar e mitigar riscos identificados.
- **Alertas em Tempo Real:** Notificações instantâneas de riscos emergentes.
- **Análise de Dados:** Painéis de controle interativos para visualização de dados e tendências.

### Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/spectra.git
