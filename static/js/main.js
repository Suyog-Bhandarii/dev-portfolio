(() => {
    const root = document.documentElement;
    const themeToggle = document.querySelector('[data-theme-toggle]');
    const menuToggle = document.querySelector('[data-menu-toggle]');
    const navLinks = document.querySelector('[data-nav-links]');
    const header = document.querySelector('[data-header]');
    const card = document.querySelector('[data-id-card]');
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const setTheme = (theme) => {
        root.dataset.theme = theme;
        localStorage.setItem('portfolio-theme', theme);
        if (themeToggle) {
            themeToggle.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
            themeToggle.innerHTML = `<i data-lucide="${theme === 'dark' ? 'sun' : 'moon'}"></i>`;
            window.lucide?.createIcons();
        }
    };

    const savedTheme = localStorage.getItem('portfolio-theme');
    const initialTheme = savedTheme || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    setTheme(initialTheme);
    themeToggle?.addEventListener('click', () => setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark'));

    menuToggle?.addEventListener('click', () => {
        const isOpen = navLinks.classList.toggle('open');
        menuToggle.setAttribute('aria-expanded', String(isOpen));
        menuToggle.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
        menuToggle.innerHTML = `<i data-lucide="${isOpen ? 'x' : 'menu'}"></i>`;
        window.lucide?.createIcons();
    });
    navLinks?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
        navLinks.classList.remove('open');
        menuToggle?.setAttribute('aria-expanded', 'false');
    }));

    const updateHeader = () => header?.classList.toggle('scrolled', window.scrollY > 20);
    updateHeader();
    window.addEventListener('scroll', updateHeader, { passive: true });

    if (card && !reducedMotion && window.matchMedia('(pointer: fine)').matches) {
        card.addEventListener('pointermove', (event) => {
            const bounds = card.getBoundingClientRect();
            const x = (event.clientX - bounds.left) / bounds.width - 0.5;
            const y = (event.clientY - bounds.top) / bounds.height - 0.5;
            card.style.transform = `perspective(900px) rotateY(${x * 8}deg) rotateX(${y * -8}deg) translateY(-4px)`;
        });
        card.addEventListener('pointerleave', () => { card.style.transform = ''; });
    }

    const revealItems = document.querySelectorAll('.reveal');
    if (!reducedMotion && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries, currentObserver) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    currentObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12 });
        revealItems.forEach((item) => observer.observe(item));
    } else {
        revealItems.forEach((item) => item.classList.add('visible'));
    }

    window.lucide?.createIcons();
})();
