from src import create_app
import socket

app = create_app()

def get_local_ip():
    """Obtém o IP local para acesso na rede"""
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except:
        return "127.0.0.1"

if __name__ == '__main__':
    # Configuração para desenvolvimento
    local_ip = get_local_ip()
    print(f"\n * Aplicação rodando:")
    print(f" * Local: http://127.0.0.1:5000")
    print(f" * Rede: http://{local_ip}:5000")
    print(" * CTRL+C para encerrar\n")
    
    # Rodar aplicação
    app.run(
        host='0.0.0.0',  # Aceita conexões de qualquer interface
        port=5000,
        debug=True,       # Modo desenvolvimento (desativar em produção)
        threaded=True     # Melhor para múltiplas conexões
    )