// ── Highlight active sidebar nav link on scroll ──────────────────────
const sections = document.querySelectorAll('section[id]');
const navLinks  = document.querySelectorAll('.side-nav a');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      navLinks.forEach(l => l.classList.remove('active'));
      const active = document.querySelector(`.side-nav a[href="#${e.target.id}"]`);
      if (active) active.classList.add('active');
    }
  });
}, { rootMargin: '-30% 0px -60% 0px' });

sections.forEach(s => sectionObserver.observe(s));

// ── Animate language bars on scroll into view ─────────────────────────
const bars = document.querySelectorAll('.lang-bar-fill');

const barObserver = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.style.transition = 'width 1s ease';
      barObserver.unobserve(e.target);
    }
  });
});

bars.forEach(b => {
  const target = b.style.width;
  b.style.width = '0';
  barObserver.observe(b);
  setTimeout(() => { b.style.width = target; }, 300);
});
