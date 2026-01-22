// Countdown Timer

function initCountdown(targetDate) {
  const countdownEl = document.getElementById('countdown');
  if (!countdownEl) return;
  
  const daysEl = countdownEl.querySelector('.days .countdown-value');
  const hoursEl = countdownEl.querySelector('.hours .countdown-value');
  const minutesEl = countdownEl.querySelector('.minutes .countdown-value');
  const secondsEl = countdownEl.querySelector('.seconds .countdown-value');
  
  function updateCountdown() {
    const now = new Date().getTime();
    const target = new Date(targetDate).getTime();
    const diff = target - now;
    
    if (diff <= 0) {
      countdownEl.innerHTML = '<h2>O grande dia chegou!</h2>';
      return;
    }
    
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);
    
    if (daysEl) daysEl.textContent = days;
    if (hoursEl) hoursEl.textContent = String(hours).padStart(2, '0');
    if (minutesEl) minutesEl.textContent = String(minutes).padStart(2, '0');
    if (secondsEl) secondsEl.textContent = String(seconds).padStart(2, '0');
  }
  
  updateCountdown();
  setInterval(updateCountdown, 1000);
}

// Auto-initialize if data attribute exists
document.addEventListener('DOMContentLoaded', function() {
  const countdown = document.getElementById('countdown');
  if (countdown) {
    const targetDate = countdown.getAttribute('data-target');
    if (targetDate) {
      initCountdown(targetDate);
    }
  }
});
