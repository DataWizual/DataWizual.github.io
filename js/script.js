// Main script for DevOpsMonitor

console.log('DevOpsMonitor loaded');

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return;
        
        e.preventDefault();
        const targetElement = document.querySelector(href);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });
});

// Bank details modal
function showBankDetails() {
    const details = `
Bank Transfer Details:

Bank: Wise (USD account)
Account: 1234567890
Routing: 084009519
SWIFT: CMFGUS33
Amount: $49
Reference: MONITORING-[YOUR EMAIL]

After payment, email receipt to:
sales@devopsmonitor.com
    `;
    alert(details);
}

// Product buttons functionality
document.querySelectorAll('.btn-primary').forEach(button => {
    if (button.getAttribute('href') === '#buy') {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            showBankDetails();
        });
    }
});

// Simple form handling (for future)
function handleEmailOrder(product) {
    const subject = `Order: ${product}`;
    const body = `I would like to purchase: ${product}\n\nMy email: `;
    window.location.href = `mailto:sales@devopsmonitor.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
}
