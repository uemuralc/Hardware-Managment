**🖥️ Monitor de Hardware e Rede - CLI**
Um painel de monitoramento de sistema em tempo real construído em Python. Este projeto coleta dados telemétricos de hardware (CPU, RAM, Disco) e de tráfego de rede (I/O), exibindo-os em uma interface gráfica de linha de comando (CLI) e registrando alertas críticos em um arquivo JSON.

**🚀 O Problema que Resolve**
Desenvolvido para monitorar a saúde e o desempenho de máquinas de alta performance (como notebooks gamers/workstations), permitindo a detecção precoce de gargalos térmicos (Thermal Throttling via frequência da CPU) e vazamentos de memória (Memory Leaks), além de acompanhar o consumo de banda de internet em tempo real.

**✨ Funcionalidades (Features)**
Monitoramento em Tempo Real: Captura o uso percentual da CPU, RAM e uso lógico do disco.

**Telemetria de Rede:** Cálculo de Delta (Δ) para exibir as taxas de Download e Upload instantâneas em MB/s.

**Frequência do Processador:** Acompanhamento do clock atual (em GHz) para identificar oscilações de desempenho.

**Interface Rica (UI):** Painel dinâmico renderizado no terminal usando a biblioteca Rich, oferecendo feedback visual (cores de alerta para limites críticos).

**Persistência de Dados (Logging):** Sistema inteligente de logging em JSON codificado em UTF-8. Salva automaticamente um histórico (timestamp e métricas) sempre que a CPU ou a RAM ultrapassam 90% de uso.

**🛠️ Tecnologias Utilizadas:**
Python 3.x: Linguagem base.

**psutil:** Interação de baixo nível com o Sistema Operacional e sensores físicos.

**rich:** Construção do layout, tabelas e atualização do buffer de tela (Live) no terminal.

**json / datetime:** Estruturação e serialização dos dados de log.

**⚙️ Como Executar o Projeto**

**Clone o repositório:**

```Bash
git clone https://github.com/uemuralc/Hardware-Managment
cd Hardware_Managment
```

**Instale as dependências:**
É recomendado o uso de um ambiente virtual (venv).

```Bash
pip install psutil rich
```

**Execute o monitor:**

```Bash
python Hardware_Managment.py
```

**🏗️ Arquitetura do Software**

O projeto foi estruturado separando as responsabilidades (Backend/Frontend):

**MonitorHardware (Classe):** Lida exclusivamente com a captura de dados brutos (psutil), cálculos matemáticos (conversão de Bytes para GB/MB) e persistência de dados.

**criar_painel_visual (Função):** Lida exclusivamente com a interface gráfica, recebendo o dicionário de dados e montando a tabela Rich.

**🔮 Próximos Passos (Roadmap)**
[ ] Implementar listagem dos "Top 5 Processos" que mais consomem RAM.

[ ] Integrar notificações nativas do Windows/Linux via plyer.

[ ] Criar um script secundário de Data Visualization para gerar gráficos a partir do alertas_sistema.json.