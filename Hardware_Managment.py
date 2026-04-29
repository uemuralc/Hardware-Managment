import psutil
import json
import time
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel

class MonitorHardware:
    def __init__(self):
        self.historico_alertas = []
        
    def capturar_dados(self):
        cpu_uso = psutil.cpu_percent(interval = 1)
        ram = psutil.virtual_memory()
        cpu_freq = psutil.cpu_freq(percpu = False)

        dados = {
            'timestamp': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            'cpu_percent': cpu_uso,
            'ram_percent': ram.percent,
            'ram_usada_gb': round(ram.used / (1024 ** 3), 2),
            'cpu_freq_ghz': round(cpu_freq.current / 1000, 2)        }
        return dados
    
    def verificar_alerta(self, dados):
        if dados['cpu_percent'] > 90:
            print(f'ALERTA: uso de CPU perigoso: {dados['cpu_percent']}%')
            self.salvar_alerta(dados)
        
        if dados['ram_percent'] > 90:
            print(f'ALERTA: uso de Memória perigosa: {dados['ram_percent']}%')
            self.salvar_alerta(dados)

    def salvar_alerta(self, dados):
        try:
            with open('alertas_sistema.json', 'r', encoding = 'utf-8') as f:
                logs = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            logs = []

        logs.append(dados)

        with open('alertas_sistema.json', 'w', encoding = 'utf-8') as f:
            json.dump(logs, f, indent = 4)

def criar_painel_visual(dados):
    tabela = Table(title = '[bold cyan] Monitor do Sistema', title_justify = 'center')

    tabela.add_column('Componente', style = 'bold magenta', width = 20)
    tabela.add_column('Uso atual', justify = 'right', style = 'cyan', width = 15)
    tabela.add_column('Status', justify = 'center', width = 20)

    cor_cpu = 'green'
    status_cpu = 'OK'

    if dados['cpu_percent'] > 90:
        cor_cpu = 'red'
        status_cpu = '[bold red]CRÍTICO[/]'
    elif dados['cpu_percent'] > 75:
        cor_cpu = 'yellow'
        status_cpu = '[bold yellow]ALTO[/]'

    cor_ram = 'green'
    status_ram = 'OK'

    if dados['ram_percent'] > 90:
        cor_ram = 'red'
        status_ram = '[bold red]CRÍTICO[/]'
    elif dados['ram_percent'] > 75:
        cor_ram = 'yellow'
        status_ram = '[bold yellow]ALTO[/]'

    tabela.add_row('CPU', f'[{cor_cpu}]{dados['cpu_percent']}%[/]', status_cpu)
    tabela.add_row('Frenquência CPU', f'[{cor_ram}]{dados['cpu_freq_ghz']} GHz[/]', status_cpu)
    tabela.add_row('RAM', f'[{cor_ram}]{dados['ram_percent']}%[/]', status_ram)
    tabela.add_row('RAM usada', f'[{cor_ram}]{dados['ram_usada_gb']} GB[/]', status_ram )

    return Panel(tabela, border_style = 'blue')

if __name__ == '__main__':
    monitor = MonitorHardware()
    console = Console()

    print('Iniciando monitoramento... (pressione Ctrl + C para parar)')

    try:
        info_inicial = monitor.capturar_dados()
        with Live(criar_painel_visual(info_inicial), refresh_per_second = 2) as Live:
            while True:
                info = monitor.capturar_dados()
                monitor.verificar_alerta(info)

                Live.update(criar_painel_visual(info))
    except KeyboardInterrupt:
        console.print('\n[bold red]✅ Monitoramento encerrado pelo usuário.[/bold red]\n')