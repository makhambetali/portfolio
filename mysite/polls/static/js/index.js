const fadeElements = document.querySelectorAll('.fade-in');

    const fadeIn = (entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    };

    const options = {
      root: null,
      rootMargin: '0px',
      threshold: 0.3
    };

    const observer = new IntersectionObserver(fadeIn, options);

    fadeElements.forEach((element) => {
      observer.observe(element);
    });