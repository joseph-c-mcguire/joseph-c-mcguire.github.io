document.addEventListener('DOMContentLoaded', function() {
  // Y2K Animation effects
  const blinkElements = document.querySelectorAll('.blink');
  if (blinkElements.length > 0 && !CSS.supports('animation: blinker 1s linear infinite')) {
    // Fallback for browsers that don't support CSS animations
    setInterval(() => {
      blinkElements.forEach(el => {
        el.style.visibility = (el.style.visibility === 'hidden') ? 'visible' : 'hidden';
      });
    }, 800);
  }
  
  // Add cursor trail effect (Y2K style)
  const cursorTrail = document.createElement('div');
  cursorTrail.className = 'cursor-trail';
  document.body.appendChild(cursorTrail);
  
  document.addEventListener('mousemove', function(e) {
    cursorTrail.style.left = e.pageX + 'px';
    cursorTrail.style.top = e.pageY + 'px';
  });
  
  // Visitor counter fallback
  const visitorCounter = document.querySelector('.y2k-counter-digits');
  if (visitorCounter) {
    const randomVisitors = Math.floor(Math.random() * 9000) + 1000;
    const visitorDigits = randomVisitors.toString().split('');
    visitorCounter.innerHTML = '';
    
    visitorDigits.forEach(digit => {
      const span = document.createElement('span');
      span.textContent = digit;
      visitorCounter.appendChild(span);
    });
  }
  
  // Add CSS sparkles to cursor
  document.addEventListener('mousemove', function(e) {
    // Create a sparkle element
    const sparkle = document.createElement('div');
    sparkle.className = 'cursor-sparkle';
    sparkle.style.cssText = `
      position: fixed;
      width: 5px;
      height: 5px;
      background: #ffcc00;
      border-radius: 50%;
      left: ${e.clientX}px;
      top: ${e.clientY}px;
      pointer-events: none;
      z-index: 9999;
    `;
    
    document.body.appendChild(sparkle);
    
    // Animate and remove
    setTimeout(() => {
      sparkle.style.opacity = '0';
      sparkle.style.transform = 'scale(0)';
      setTimeout(() => document.body.removeChild(sparkle), 300);
    }, 100);
  });
  
  console.log('Y2K website initialized successfully!');
});
