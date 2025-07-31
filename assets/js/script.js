// ===== FASE 2: FUNCIONALIDADES AVANZADAS =====

// 1. TOGGLE DE TEMA OSCURO/CLARO
function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  
  // Animación suave del toggle
  const toggle = document.querySelector('.theme-toggle');
  toggle.style.transform = 'scale(0.9)';
  setTimeout(() => {
    toggle.style.transform = 'scale(1)';
  }, 150);
}

// Cargar tema guardado
function loadSavedTheme() {
  const savedTheme = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);
}

// 2. BARRA DE PROGRESO DE LECTURA
function updateReadingProgress() {
  const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
  const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  const scrolled = (scrollTop / scrollHeight) * 100;
  
  let progressBar = document.querySelector('.reading-progress');
  if (!progressBar) {
    progressBar = document.createElement('div');
    progressBar.className = 'reading-progress';
    document.body.appendChild(progressBar);
  }
  
  progressBar.style.width = scrolled + '%';
}

// 3. INDICADOR DE PROGRESO DE SCROLL
function updateScrollIndicator() {
  const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
  const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  const scrolled = (scrollTop / scrollHeight) * 100;
  
  let indicator = document.querySelector('.scroll-indicator');
  if (!indicator) {
    indicator = document.createElement('div');
    indicator.className = 'scroll-indicator';
    document.body.appendChild(indicator);
  }
  
  indicator.style.transform = `scaleX(${scrolled / 100})`;
}

// 4. FILTROS DE PROYECTOS Y BLOG
function initProjectFilters() {
  const filterButtons = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.proyecto-card');
  const blogPosts = document.querySelectorAll('.blog-post');
  const searchInput = document.getElementById('search-projects');
  const blogSearchInput = document.getElementById('search-blog');
  
  // Filtros por categoría para proyectos
  filterButtons.forEach(button => {
    button.addEventListener('click', () => {
      const filter = button.getAttribute('data-filter');
      
      // Actualizar botón activo
      filterButtons.forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');
      
      // Filtrar proyectos
      if (projectCards.length > 0) {
        projectCards.forEach(card => {
          const categories = card.getAttribute('data-categories') || '';
          
          if (filter === 'all' || categories.includes(filter)) {
            card.style.display = 'block';
            card.style.animation = 'fadeInUp 0.5s ease-out';
          } else {
            card.style.display = 'none';
          }
        });
      }
      
      // Filtrar posts del blog
      if (blogPosts.length > 0) {
        blogPosts.forEach(post => {
          const categories = post.getAttribute('data-categories') || '';
          
          if (filter === 'all' || categories.includes(filter)) {
            post.style.display = 'block';
            post.style.animation = 'fadeInUp 0.5s ease-out';
          } else {
            post.style.display = 'none';
          }
        });
      }
    });
  });
  
  // Búsqueda de texto para proyectos
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const searchTerm = e.target.value.toLowerCase();
      
      projectCards.forEach(card => {
        const title = card.querySelector('h3')?.textContent?.toLowerCase() || '';
        const subtitle = card.querySelector('h4')?.textContent?.toLowerCase() || '';
        const description = card.querySelector('p')?.textContent?.toLowerCase() || '';
        
        // Buscar en todo el contenido de texto de la tarjeta
        const allText = (title + ' ' + subtitle + ' ' + description).toLowerCase();
        
        if (allText.includes(searchTerm)) {
          card.style.display = 'block';
          card.style.animation = 'fadeInUp 0.5s ease-out';
        } else {
          card.style.display = 'none';
        }
      });
    });
  }
  
  // Búsqueda de texto para blog
  if (blogSearchInput) {
    blogSearchInput.addEventListener('input', (e) => {
      const searchTerm = e.target.value.toLowerCase();
      
      blogPosts.forEach(post => {
        const title = post.querySelector('h3')?.textContent?.toLowerCase() || '';
        const content = post.textContent?.toLowerCase() || '';
        const category = post.querySelector('.post-category')?.textContent?.toLowerCase() || '';
        
        if (title.includes(searchTerm) || content.includes(searchTerm) || category.includes(searchTerm)) {
          post.style.display = 'block';
          post.style.animation = 'fadeInUp 0.5s ease-out';
        } else {
          post.style.display = 'none';
        }
      });
    });
  }
}

// 5. TIMELINE INTERACTIVO
function createInteractiveTimeline() {
  const timelineContainer = document.querySelector('.learning-timeline');
  if (!timelineContainer) return;
  
  const weeks = [
    { week: 1, title: 'Fundamentos Web', tech: 'HTML, CSS, Protocolos' },
    { week: 2, title: 'HTML y CSS Avanzado', tech: 'Flexbox, Grid, Emmet' },
    { week: 3, title: 'CSS Frameworks', tech: 'Bootstrap, Tailwind' },
    { week: 4, title: 'JavaScript y TypeScript', tech: 'DOM, Canvas, Tipos' },
    { week: 5, title: 'React Framework', tech: 'Componentes, JSX, Props' },
    { week: 6, title: 'APIs en React', tech: 'Axios, Async/Await' },
    { week: 7, title: 'React Hooks', tech: 'useState, useEffect' },
    { week: 9, title: 'Backend - Arquitectura', tech: 'MVC, JWT, APIs' },
    { week: 10, title: 'Java Spring', tech: 'Spring Boot, JPA' },
    { week: 12, title: 'PHP Laravel', tech: 'Eloquent, Blade' },
    { week: 14, title: 'Python Flask', tech: 'Jinja2, SQLAlchemy' },
    { week: 15, title: 'Sistemas Inteligentes', tech: 'IA, ML, LLM' }
  ];
  
  let timelineHTML = '<div class="timeline-line"></div>';
  
  weeks.forEach((item, index) => {
    timelineHTML += `
      <div class="timeline-item" data-week="${item.week}" style="animation-delay: ${index * 0.1}s">
        <div class="timeline-marker">
          <span class="week-number">${item.week}</span>
        </div>
        <div class="timeline-content">
          <h4>${item.title}</h4>
          <p>${item.tech}</p>
          <a href="pages/semana${item.week}.html" class="timeline-link">Ver detalles</a>
        </div>
      </div>
    `;
  });
  
  timelineContainer.innerHTML = timelineHTML;
  
  // Animación al hacer scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-in');
      }
    });
  }, observerOptions);
  
  document.querySelectorAll('.timeline-item').forEach(item => {
    observer.observe(item);
  });
}

// 6. SISTEMA DE FEEDBACK
function initFeedbackSystem() {
  const ratingButtons = document.querySelectorAll('.rating-btn');
  const feedbackTextarea = document.querySelector('.feedback-section textarea');
  
  ratingButtons.forEach(button => {
    button.addEventListener('click', () => {
      const rating = button.getAttribute('data-rating');
      
      // Actualizar estado visual
      ratingButtons.forEach(btn => btn.classList.remove('selected'));
      button.classList.add('selected');
      
      // Guardar rating
      localStorage.setItem(`rating-${window.location.pathname}`, rating);
      
      // Mostrar mensaje de agradecimiento
      showNotification('¡Gracias por tu feedback!', 'success');
    });
  });
  
  // Guardar comentario
  if (feedbackTextarea) {
    feedbackTextarea.addEventListener('blur', () => {
      const comment = feedbackTextarea.value;
      if (comment.trim()) {
        localStorage.setItem(`comment-${window.location.pathname}`, comment);
        showNotification('Comentario guardado', 'info');
      }
    });
  }
}

// 7. SISTEMA DE NOTIFICACIONES
function showNotification(message, type = 'info') {
  const notification = document.createElement('div');
  notification.className = `notification notification-${type}`;
  notification.textContent = message;
  
  document.body.appendChild(notification);
  
  // Mostrar con animación
  setTimeout(() => notification.classList.add('show'), 100);
  
  // Ocultar después de 3 segundos
  setTimeout(() => {
    notification.classList.remove('show');
    setTimeout(() => notification.remove(), 300);
  }, 3000);
}

// 8. CALCULADORA DE TIEMPO DE LECTURA
function calculateReadingTime() {
  const content = document.querySelector('.contenido-semana, main');
  if (!content) return;
  
  const text = content.textContent || content.innerText;
  const wordsPerMinute = 200;
  const words = text.trim().split(/\s+/).length;
  const minutes = Math.ceil(words / wordsPerMinute);
  
  // Crear indicador de tiempo de lectura
  const readingTime = document.createElement('div');
  readingTime.className = 'reading-time';
  readingTime.innerHTML = `
    <i class="fas fa-clock"></i>
    <span>${minutes} min de lectura</span>
  `;
  
  const header = document.querySelector('.semana-header, header');
  if (header) {
    header.appendChild(readingTime);
  }
}

// Animaciones de entrada
function animateOnScroll() {
  const elements = document.querySelectorAll('.seccion, .semana, .blog-post, .skill-card');
  
  elements.forEach(element => {
    const elementTop = element.getBoundingClientRect().top;
    const elementVisible = 150;
    
    if (elementTop < window.innerHeight - elementVisible) {
      element.classList.add('animate-in');
    }
  });
}

// Smooth scroll para navegación
function smoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}

// Efecto de typing para el título
function typeWriter(element, text, speed = 100) {
  let i = 0;
  element.innerHTML = '';
  
  function type() {
    if (i < text.length) {
      element.innerHTML += text.charAt(i);
      i++;
      setTimeout(type, speed);
    }
  }
  
  type();
}

// Inicializar cuando carga la página
document.addEventListener('DOMContentLoaded', function() {
  // ===== INICIALIZAR TODAS LAS FUNCIONALIDADES FASE 2 =====
  
  // Cargar tema guardado
  loadSavedTheme();
  
  // Smooth scroll
  smoothScroll();
  
  // Inicializar filtros de proyectos
  initProjectFilters();
  
  // Crear timeline interactivo
  createInteractiveTimeline();
  
  // Inicializar sistema de feedback
  initFeedbackSystem();
  
  // Calcular tiempo de lectura
  calculateReadingTime();
  
  // Efecto typing en el título principal (opcional)
  const mainTitle = document.querySelector('header h1');
  if (mainTitle) {
    const originalText = mainTitle.textContent;
    typeWriter(mainTitle, originalText, 80);
  }
  
  // Animaciones iniciales
  setTimeout(() => {
    animateOnScroll();
  }, 300);
});

// Event listeners mejorados
window.addEventListener('scroll', () => {
  updateScrollIndicator();
  updateReadingProgress();
  animateOnScroll();
});

// Efecto parallax sutil para el header
window.addEventListener('scroll', () => {
  const scrolled = window.pageYOffset;
  const header = document.querySelector('header');
  if (header) {
    header.style.transform = `translateY(${scrolled * 0.3}px)`;
  }
});