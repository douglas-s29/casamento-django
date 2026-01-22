// Admin Dashboard JavaScript

document.addEventListener('DOMContentLoaded', function() {
  // Sidebar toggle for mobile
  const sidebarToggle = document.querySelector('[data-sidebar-toggle]');
  const sidebar = document.querySelector('.sidebar');
  
  if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener('click', function() {
      sidebar.classList.toggle('open');
    });
  }
  
  // Filter buttons
  const filterButtons = document.querySelectorAll('.filter-btn');
  filterButtons.forEach(btn => {
    btn.addEventListener('click', function() {
      filterButtons.forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      
      const filter = this.getAttribute('data-filter');
      filterTable(filter);
    });
  });
  
  // Copy to clipboard
  const copyButtons = document.querySelectorAll('[data-copy]');
  copyButtons.forEach(btn => {
    btn.addEventListener('click', function() {
      const text = this.getAttribute('data-copy');
      navigator.clipboard.writeText(text).then(() => {
        showToast('Copiado para área de transferência!');
      });
    });
  });
  
  // Delete confirmation
  const deleteButtons = document.querySelectorAll('[data-delete]');
  deleteButtons.forEach(btn => {
    btn.addEventListener('click', function(e) {
      if (!confirm('Tem certeza que deseja excluir este item?')) {
        e.preventDefault();
      }
    });
  });
});

// Filter table rows
function filterTable(filter) {
  const rows = document.querySelectorAll('tbody tr');
  rows.forEach(row => {
    if (filter === 'all' || row.getAttribute('data-status') === filter) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });
}

// Show toast notification
function showToast(message, duration = 3000) {
  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.textContent = message;
  toast.style.cssText = `
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: var(--dark);
    color: white;
    padding: 1rem 1.5rem;
    border-radius: 8px;
    box-shadow: var(--shadow-lg);
    z-index: 9999;
    animation: slideIn 0.3s ease;
  `;
  
  document.body.appendChild(toast);
  
  setTimeout(() => {
    toast.style.animation = 'slideOut 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, duration);
}
