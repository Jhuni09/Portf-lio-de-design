// Script para filtrar projetos na página de projetos
document.addEventListener('DOMContentLoaded', function() {
    // Verificar se estamos na página de projetos
    const filterButtons = document.querySelectorAll('.filter-btn');
    if (filterButtons.length > 0) {
        filterButtons.forEach(button => {
            button.addEventListener('click', function() {
                // Remover classe active de todos os botões
                filterButtons.forEach(btn => btn.classList.remove('active'));
                
                // Adicionar classe active ao botão clicado
                this.classList.add('active');
                
                // Obter categoria selecionada
                const filterValue = this.getAttribute('data-filter');
                
                // Filtrar projetos
                const projetoCards = document.querySelectorAll('.projeto-card');
                projetoCards.forEach(card => {
                    if (filterValue === 'all') {
                        card.style.display = 'block';
                    } else {
                        if (card.getAttribute('data-category') === filterValue) {
                            card.style.display = 'block';
                        } else {
                            card.style.display = 'none';
                        }
                    }
                });
            });
        });
    }
    
    // Adicionar efeito de scroll suave para links de âncora
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
                
                // Fechar menu mobile se estiver aberto
                const menuToggle = document.getElementById('menu-toggle');
                if (menuToggle && menuToggle.checked) {
                    menuToggle.checked = false;
                }
            }
        });
    });
    
    // Adicionar classe active ao link do menu correspondente à seção visível
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('nav .menu li a');
    
    function highlightNavLink() {
        const scrollPosition = window.scrollY + 100;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}` || 
                        (link.getAttribute('href') === '/' && sectionId === 'home')) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }
    
    window.addEventListener('scroll', highlightNavLink);
    
    // Adicionar efeito de header transparente que muda ao rolar
    const header = document.querySelector('header');
    
    function toggleHeaderBackground() {
        if (window.scrollY > 50) {
            header.style.backgroundColor = 'rgba(0, 0, 0, 0.9)';
            header.style.padding = '15px 0';
        } else {
            header.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
            header.style.padding = '20px 0';
        }
    }
    
    window.addEventListener('scroll', toggleHeaderBackground);
    toggleHeaderBackground(); // Executar na carga inicial
});