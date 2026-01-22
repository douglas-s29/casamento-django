// Scroll Animations

document.addEventListener('DOMContentLoaded', function() {
  // Intersection Observer for fade-in animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-in');
        // Optionally unobserve after animation
        // observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  // Observe all elements with fade-in class
  document.querySelectorAll('.fade-in').forEach(el => {
    observer.observe(el);
  });
});

// Parallax effect for background images
window.addEventListener('scroll', function() {
  const parallaxElements = document.querySelectorAll('.parallax');
  parallaxElements.forEach(element => {
    const scrolled = window.pageYOffset;
    const rate = scrolled * 0.5;
    element.style.transform = `translate3d(0, ${rate}px, 0)`;
  });
});
