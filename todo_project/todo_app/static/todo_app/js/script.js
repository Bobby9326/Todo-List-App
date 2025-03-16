document.addEventListener('DOMContentLoaded', function() {
    // เพิ่ม Animation สำหรับการแสดงรายการ
    const listItems = document.querySelectorAll('.list-group-item');
    listItems.forEach((item, index) => {
        item.style.animation = `fadeIn 0.3s ease forwards ${index * 0.1}s`;
        item.style.opacity = '0';
    });

    // Animation keyframes
    const style = document.createElement('style');
    style.innerHTML = `
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    `;
    document.head.appendChild(style);
});