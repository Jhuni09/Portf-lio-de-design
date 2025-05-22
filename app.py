from flask import Flask, render_template, request, redirect, url_for
import urllib.parse

app = Flask(__name__)

# Dados de exemplo para projetos
projects = [
    {
        "id": 1,
        "title": "Redesign de Marcas e empresas",
        "category": "Identidade Visual",
        "image": "/static/images/lash-foto.jpg",
        "description": "Redesign completo da identidade visual de uma empresa, incluindo logo, uniformes e material de marketing."
    },
    {
        "id": 2,
        "title": "Flyers Esportivos",
        "category": "Para atletas",
        "image": "/static/images/arthur-foto.jpg",
        "description": "Desenvolvimento de flyers esportivos personalizados para times, atletas e marcas esportivas."
    },
    {
        "id": 3,
        "title": "Promoção de eventos e produtos",
        "category": "Eventos",
        "image": "/static/images/copa-foto.jpg",
        "description": "Identidade visual completa para maratona anual, incluindo materiais promocionais e outros."
    },
    {
        "id": 4,
        "title": "Conteúdo para Redes Sociais",
        "category": "Social Media",
        "image": "/static/images/promo-foto.jpg",
        "description": "Pacote de templates para redes sociais."
    },
    {
        "id": 5,
        "title": "Cartões de visita",
        "category": "Identidade Visual",
        "image": "/static/images/image.png",
        "description": "Desenvolvimento de cartões de visita personalizados para times, atletas e empresas."
    },
    {
        "id": 6,
        "title": "Embalagens e materiais promocionais",
        "category": "Eventos",
        "image": "/static/images/embalagem-foto.jpg",
        "description": "Desenvolvimento de embalagens e materiais promocionais."
    }
]

# Dados de exemplo para serviços
services = [
    {
        "title": "Identidade Visual",
        "description": "Desenvolvimento de logos, cores e elementos visuais para times, atletas e marcas esportivas."
    },
    {
        "title": "Design de Uniformes",
        "description": "Criação de uniformes esportivos personalizados com foco em estética e funcionalidade."
    },
    {
        "title": "Social Media",
        "description": "Pacotes de templates e conteúdo visual para redes sociais de marcas e atletas."
    },
    {
        "title": "Eventos Esportivos",
        "description": "Identidade visual completa para eventos, incluindo materiais promocionais e sinalização."
    }
]

@app.route('/')
def index():
    # Mostrar apenas 3 projetos na página inicial
    featured_projects = projects[:3]
    return render_template('index.html', projects=featured_projects, services=services)

@app.route('/projetos')
def projetos():
    return render_template('projetos.html', projects=projects)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/enviar-contato', methods=['POST'])
def enviar_contato():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        assunto = request.form.get('assunto')
        mensagem = request.form.get('mensagem')
        
        # Número de WhatsApp (substitua pelo seu)
        whatsapp_number = "+5515998336415"
        
        # Criar mensagem formatada para o WhatsApp
        whatsapp_text = f"*Contato via Site*\n\n*Nome:* {nome}\n*Email:* {email}\n*Assunto:* {assunto}\n\n*Mensagem:*\n{mensagem}"
        
        # Codificar a mensagem para URL
        encoded_text = urllib.parse.quote(whatsapp_text)
        
        # Criar URL do WhatsApp
        whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_text}"
        
        # Redirecionar para o WhatsApp
        return redirect(whatsapp_url)

if __name__ == '__main__':
    app.run(debug=True)